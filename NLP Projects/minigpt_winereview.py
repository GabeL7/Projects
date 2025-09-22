"""
MiniGPT for Wine Review Generation
Trains a small GPT-style model on wine review descriptions
Includes tokenization, vocabulary building, sequence padding, and sampling
Token generation with temperature, top-k, and top-p (nucleus) sampling

├── data/
│   └── winemag-data-130k-v2.json          # Raw wine review dataset (JSON)
├── wine_dataset.pt                        # Preprocessed padded tensor dataset
├── wine_vocab.pkl                         # Vocabulary mapping token -> ID
├── main.py                                # Main program: loads data, builds vocab, trains sampling demo
|
│   ├── Imports: json, re, torch, pickle, collections, PyTorch utilities
│   ├── Parameters: MAX_VOCAB_SIZE, MAX_SEQ_LEN, embedding size, model layers, epochs
│   ├── Load & clean data: extract wine descriptions
│   ├── Tokenize text & build vocabulary
│   ├── Convert token lists to ID tensors & pad sequences
│   ├── Save dataset and vocab
│   ├── Define Dataset class & DataLoader
│   ├── Sample batch check
│   ├── Decode helper function
│   ├── Test model for sampling demo
│   └── Sampling function with temperature, top-k, top-p
├── sample outputs                            
"""

import json
import re
from collections import Counter
import torch
import pickle
from torch.nn.utils.rnn import pad_sequence
from torch.utils.data import Dataset, DataLoader

# === Parameters ===
# Define file paths and hyperparameters for vocab size, sequence length, embedding, model layers, and training epochs.
DATA_PATH = "data/winemag-data-130k-v2.json"
SAVE_PATH = "wine_dataset.pt"
VOCAB_PATH = "wine_vocab.pkl"
MAX_VOCAB_SIZE = 10000
MIN_FREQ = 2
MAX_SEQ_LEN = 128
embed_size = 128
n_heads = 4
ff_dim = 256
N_LAYERS = 4
epochs = 10

# === Load and Clean Data ===
# Load wine review JSON data and extract non-empty descriptions.
with open(DATA_PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

print("Wine descriptions:")
descriptions = [
    item['description'].strip()
    for item in data
    if 'description' in item and item['description']
]

# === Tokenization ===
# Define a simple tokenizer that lowercases text and separates punctuation.
def tokenize(text):
    text = text.lower()
    text = re.sub(r"([.,!?;:])", r" \1", text)
    return text.split()

tokenized_texts = [tokenize(desc) for desc in descriptions]
print(tokenized_texts[:2])

# === Build Vocabulary ===
# Count token frequencies and create a vocabulary mapping tokens to IDs, including special tokens.
counter = Counter()
for tokens in tokenized_texts:
    counter.update(tokens)

vocab = {"<PAD>": 0, "<UNK>": 1, "<BOS>": 2, "<EOS>": 3}
for word, freq in counter.most_common(MAX_VOCAB_SIZE):
    if freq >= MIN_FREQ and word not in vocab:
        vocab[word] = len(vocab)

vocab_size = len(vocab)
word2idx = vocab
idx2word = {i: w for w, i in word2idx.items()}
indlist = [(i, idx2word[i]) for i in range(6)]
print(indlist)

# === Convert to IDs ===
# Convert tokenized text to tensor sequences of token IDs with <BOS> and <EOS>, truncated to MAX_SEQ_LEN.
def tokens_to_ids(tokens):
    ids = [vocab.get(token, vocab["<UNK>"]) for token in tokens]
    ids = [vocab["<BOS>"]] + ids + [vocab["<EOS>"]]
    # Truncate to MAX_SEQ_LEN
    if len(ids) > MAX_SEQ_LEN:
        ids = ids[:MAX_SEQ_LEN]
    return torch.tensor(ids)

indexed_seqs = [tokens_to_ids(tokens) for tokens in tokenized_texts]
print("\nIndexed sequences:\n", indexed_seqs[:2])

# === Padding ===
# Pad sequences to the maximum length using the PAD token to ensure uniform tensor shapes.
padded_seqs = torch.full((len(indexed_seqs), MAX_SEQ_LEN), vocab["<PAD>"], dtype=torch.long)
for i, seq in enumerate(indexed_seqs):
    seq_len = min(len(seq), MAX_SEQ_LEN)
    padded_seqs[i, :seq_len] = seq[:seq_len]

print("\nPadded sequences:\n", padded_seqs[:2])

# === Save Dataset and Vocabulary ===
# Save padded sequences and vocabulary dictionary to disk for later use.
torch.save(padded_seqs, SAVE_PATH)
with open(VOCAB_PATH, "wb") as f:
    pickle.dump(vocab, f)

print(f"\nSaved {len(padded_seqs)} samples to {SAVE_PATH}")

# === Dataset Class ===
# PyTorch Dataset that returns input-target pairs for language modeling from saved tensor data.
class WineReviewDataset(Dataset):
    def __init__(self, data_path):
        self.data = torch.load(data_path)

    def __len__(self):
        return self.data.size(0)

    def __getitem__(self, idx):
        x = self.data[idx]
        return x[:-1], x[1:]

# === Load DataLoader ===
# Instantiate the Dataset and DataLoader with batching and shuffling.
dataset = WineReviewDataset(SAVE_PATH)
dataloader = DataLoader(dataset, batch_size=32, shuffle=True)

# === Batch Check ===
# Fetch one batch and print shapes and token index statistics for verification.
x_batch, y_batch = next(iter(dataloader))
print("\nSample batch check:")
print(f"x_batch shape: {x_batch.shape}")
print(f"y_batch shape: {y_batch.shape}")
print(f"Max token index in x_batch: {x_batch.max().item()}")
print(f"Min token index in x_batch: {x_batch.min().item()}")
print(f"\nx_batch [:2]: {x_batch[:2]}")
print(f"\ny_batch [:2]: {y_batch[:2]}")

# === Decode Helper ===
# Convert sequences of token IDs back to human-readable text.
def decode(ids, idx2word):
    words = []
    for id in ids:
        if id.item() in (vocab["<PAD>"], vocab["<BOS>"]):
            continue
        if id.item() == vocab["<EOS>"]:
            break
        words.append(idx2word.get(id.item(), "<UNK>"))
    return " ".join(words)

# === Dummy Model Placeholder ===
# Define a test model that outputs random logits for sampling demonstration.
class TestModel:
    def eval(self): pass
    def __call__(self, x):
        batch_size, seq_len = x.size()
        logits = torch.randn(batch_size, seq_len, vocab_size)
        return logits

model = TestModel()

# === Sampling Function ===
# Sample tokens from the model with temperature, top-k, and top-p (nucleus) filtering.
@torch.no_grad()
def sample(model, start, max_new_tokens=50, top_k=50, top_p=0.9, temperature=1.0):
    model.eval()
    tokens = tokenize(start)
    ids = [vocab.get("<BOS>")] + [vocab.get(t, vocab["<UNK>"]) for t in tokens]
    input_ids = torch.tensor(ids, dtype=torch.long).unsqueeze(0)

    for _ in range(max_new_tokens):
        logits = model(input_ids)[:, -1, :] / temperature
        logits = logits.squeeze(0)
        probs = torch.softmax(logits, dim=-1)

        # Top-k filtering
        if top_k > 0:
            topk_vals, topk_indices = torch.topk(probs, top_k)
            probs_filtered = torch.zeros_like(probs).scatter_(0, topk_indices, topk_vals)
            probs = probs_filtered

        # Top-p filtering
        sorted_probs, sorted_indices = torch.sort(probs, descending=True)
        cum_probs = torch.cumsum(sorted_probs, dim=-1)
        cutoff = cum_probs > top_p
        cutoff[1:] = cutoff[:-1].clone()
        cutoff[0] = False
        sorted_probs[cutoff] = 0
        probs = torch.zeros_like(probs).scatter(0, sorted_indices, sorted_probs)

        probs /= probs.sum()
        next_id = torch.multinomial(probs, num_samples=1)
        input_ids = torch.cat([input_ids, next_id.unsqueeze(0)], dim=1)

        if next_id.item() == vocab["<EOS>"]:
            break

    return decode(input_ids[0], idx2word)

# === Output Demonstration ===
# Print sample tokenized reviews, vocab, sequences, padded tensors, batch info, and sampling examples.
print("\nTokenized sample reviews:")
print(tokenized_texts[:2])  # show first 2 tokenized samples
print()

print("Vocabulary size:", vocab_size)
print()

print("Sample vocabulary entries:")
print(indlist)  # first 6 vocab items
print()

print("Indexed sequences:")
for seq in indexed_seqs[:2]:  # print first 2 sequences
    print(seq)
print()

print("Padded sequences tensor:")
print(padded_seqs[:2])  # show first 2 padded sequences
print()

print(f"Saved {len(padded_seqs)} samples to {SAVE_PATH}")
print()

print("Sample batch check:")
print(f"x_batch shape: {x_batch.shape}")
print(f"y_batch shape: {y_batch.shape}")
print(f"Max token index in x_batch: {x_batch.max().item()}")
print(f"Min token index in x_batch: {x_batch.min().item()}")
print()

print("x_batch [:2]:")
print(x_batch[:2])
print()

print("y_batch [:2]:")
print(y_batch[:2])
print()

print("=== Sampling Examples from Test Model ===\n")

print("Example 1: Italy wine review, temperature=0.5")
print("Prompt: 'wine review : italy : '")
print(sample(model, "wine review : italy : ", temperature=0.5))
print()

print("Example 2: Italy wine review, temperature=0.8")
print("Prompt: 'wine review : italy : '")
print(sample(model, "wine review : italy : ", temperature=0.8))
print()

print("Example 3: Bright acidity start, temperature=0.9")
print("Prompt: 'bright acidity ,'")
print(sample(model, "bright acidity ,", temperature=0.9))
print()

print("Example 4: US wine review, temperature=1.0")
print("Prompt: 'wine review : us : '")
print(sample(model, "wine review: us : ", temperature=1.0))
print()

print("Example 5: Germany wine review, temperature=1.0")
print("Prompt: 'wine review : germany : '")
print(sample(model, "wine review : germany : ", temperature=1.0))
print()
