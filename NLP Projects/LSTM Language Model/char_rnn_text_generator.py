"""
Character-level language model using multi-layer LSTM to generate text in the style of 'Anna Karenina'
Loads raw text, builds vocabulary mappings, encodes sequences, and trains an RNN with dropout regularization
Supports sampling text from the trained model with adjustable creativity via top-k sampling
Saves and reloads model checkpoints for later use or continued training

├── data/
│   └── anna.txt                  # raw text corpus from 'Anna Karenina'
|
│── rnn_reference.model         # pre-trained RNN checkpoint for sampling
|
├──rnn_20_epoch.model          # generated after training
|
├── main.py
│   ├── Imports: numpy, torch, torch.nn, torch.optim, and functional utils
│   ├── Builds character to integer mappings and one-hot encodings
│   ├── Defines CharRNN class: multi-layer LSTM with dropout + fully connected output
│   ├── Implements train loop with mini-batches, gradient clipping, validation splits
│   ├── Provides sampling with prime text and top-k probabilistic sampling
│   ├── Saves model state dict and hyperparameters to file
│   └── Loads model checkpoint and generates new text samples

Imports for array operations, tensor computations, neural nets, optimization, and GPU support
"""

import numpy as np
import torch
from torch import nn
import torch.nn.functional as F
import torch.optim as optim

# load text data and encode unique characters
with open('data/anna.txt', 'r') as f:
    text = f.read()
chars = sorted(set(text))
int2char = {i: ch for i, ch in enumerate(chars)}
char2int = {ch: i for i, ch in enumerate(chars)}
encoded = np.array([char2int[ch] for ch in text])

# one-hot encoding function for integer sequences
def one_hot_encode(arr, n_labels):
    one_hot = np.zeros((arr.size, n_labels), dtype=np.float32)
    one_hot[np.arange(one_hot.shape[0]), arr.flatten()] = 1.
    one_hot = one_hot.reshape((*arr.shape, n_labels))
    return one_hot

# create generator that yields batches for training
def get_batches(arr, batch_size, seq_length):
    batch_size_total = batch_size * seq_length
    n_batches = len(arr) // batch_size_total
    arr = arr[:n_batches * batch_size_total]
    arr = arr.reshape((batch_size, -1))
    for n in range(0, arr.shape[1], seq_length):
        x = arr[:, n:n+seq_length]
        y = np.zeros_like(x)
        try:
            y[:, :-1], y[:, -1] = x[:, 1:], arr[:, n+seq_length]
        except IndexError:
            y[:, :-1], y[:, -1] = x[:, 1:], arr[:, 0]
        yield x, y

# check if training on GPU is possible
train_on_gpu = torch.cuda.is_available()

# character-level RNN model using LSTM
class CharRNN(nn.Module):
    def __init__(self, tokens, n_hidden=256, n_layers=2, drop_prob=0.5, lr=0.001):
        super().__init__()
        self.drop_prob = drop_prob
        self.n_layers = n_layers
        self.n_hidden = n_hidden
        self.lr = lr
        self.chars = tokens
        self.int2char = dict(enumerate(self.chars))
        self.char2int = {ch: ii for ii, ch in self.int2char.items()}
        self.lstm = nn.LSTM(input_size=len(self.chars), hidden_size=self.n_hidden,
                            num_layers=self.n_layers, dropout=self.drop_prob, batch_first=True)
        self.dropout = nn.Dropout(self.drop_prob)
        self.fc = nn.Linear(self.n_hidden, len(self.chars))

    # forward pass through network
    def forward(self, x, hidden):
        r_output, hidden = self.lstm(x, hidden)
        out = self.dropout(r_output)
        out = out.contiguous().view(-1, self.n_hidden)
        out = self.fc(out)
        return out, hidden

    # initialize hidden state
    def init_hidden(self, batch_size):
        device = next(self.parameters()).device
        hidden = (torch.zeros(self.n_layers, batch_size, self.n_hidden, device=device),
                  torch.zeros(self.n_layers, batch_size, self.n_hidden, device=device))
        return hidden

# training loop for model
def train(model, data, epochs=10, batch_size=10, seq_length=50, lr=0.001, clip=5, val_frac=0.1, print_every=10):
    model.train()
    val_idx = int(len(data)*(1-val_frac))
    data, val_data = data[:val_idx], data[val_idx:]
    if(train_on_gpu):
        model.cuda()
    counter = 0
    n_chars = len(model.chars)
    for e in range(epochs):
        h = model.init_hidden(batch_size)
        for x, y in get_batches(data, batch_size, seq_length):
            counter += 1
            x = one_hot_encode(x, n_chars)
            inputs, targets = torch.from_numpy(x), torch.from_numpy(y)
            if(train_on_gpu):
                inputs, targets = inputs.cuda(), targets.cuda()
            h = tuple([each.detach() for each in h])
            model.zero_grad()
            output, h = model(inputs, h)
            loss = criterion(output, targets.view(batch_size*seq_length).long())
            loss.backward()
            nn.utils.clip_grad_norm_(model.parameters(), clip)
            opt.step()
            if counter % print_every == 0:
                val_h = model.init_hidden(batch_size)
                val_losses = []
                model.eval()
                for x, y in get_batches(val_data, batch_size, seq_length):
                    x = one_hot_encode(x, n_chars)
                    inputs, targets = torch.from_numpy(x), torch.from_numpy(y)
                    if(train_on_gpu):
                        inputs, targets = inputs.cuda(), targets.cuda()
                    val_h = tuple([each.detach() for each in val_h])
                    output, val_h = model(inputs, val_h)
                    val_loss = criterion(output, targets.view(batch_size*seq_length).long())
                    val_losses.append(val_loss.item())
                model.train()
                print("Epoch: {}/{}...".format(e+1, epochs),
                      "Step: {}...".format(counter),
                      "Loss: {:.4f}...".format(loss.item()),
                      "Val Loss: {:.4f}".format(np.mean(val_losses)))

# set hyperparameters and initialize model, optimizer, loss
n_hidden = 256
n_layers = 2
model = CharRNN(chars, n_hidden, n_layers)
print(model)
opt = optim.Adam(model.parameters())
criterion = nn.CrossEntropyLoss()
batch_size = 128
seq_length = 100
n_epochs = 1

# train the character-level RNN
train(model, encoded, epochs=n_epochs, batch_size=batch_size, seq_length=seq_length, lr=0.0001, print_every=40)

# predict next character given a character input
def predict(model, char, h=None, top_k=None):
    x = np.array([[model.char2int[char]]])
    x = one_hot_encode(x, len(model.chars))
    inputs = torch.from_numpy(x)
    if(train_on_gpu):
        inputs = inputs.cuda()
    h = tuple([each.detach() for each in h])
    out, h = model(inputs, h)
    p = F.softmax(out, dim=1).detach()
    if(train_on_gpu):
        p = p.cpu()
    if top_k is None:
        top_ch = np.arange(len(model.chars))
    else:
        p, top_ch = p.topk(top_k)
        top_ch = top_ch.numpy().squeeze()
    p = p.numpy().squeeze()
    char = np.random.choice(top_ch, p=p/p.sum())
    return model.int2char[char], h

# sample a sequence of characters from the trained model
def sample(model, size, prime='The', top_k=None):
    if(train_on_gpu):
        model.cuda()
    else:
        model.cpu()
    model.eval()
    chars = [ch for ch in prime]
    h = model.init_hidden(1)
    for ch in prime:
        char, h = predict(model, ch, h, top_k)
    for _ in range(size):
        char, h = predict(model, char, h, top_k)
        chars.append(char)
    return ''.join(chars)

print(sample(model, 1000, prime='Anna', top_k=5))

# save the trained model checkpoint
model_name = 'rnn_20_epoch.model'
checkpoint = {'n_hidden': model.n_hidden,
              'n_layers': model.n_layers,
              'state_dict': model.state_dict(),
              'tokens': model.chars}
with open(model_name, 'wb') as f:
    torch.save(checkpoint, f)

# load a saved model checkpoint and generate text
with open('rnn_reference.model', 'rb') as f:
    checkpoint = torch.load(f)
loaded_model = CharRNN(checkpoint['tokens'],
                       n_hidden=checkpoint['n_hidden'],
                       n_layers=checkpoint['n_layers'])
loaded_model.load_state_dict(checkpoint['state_dict'])
loaded_model.eval()
print(sample(loaded_model, 5000, top_k=5, prime="And Levin said"))
