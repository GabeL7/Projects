// Libraries for I/O, memory management, string handling, 
// file operations, threading, and timing functions
#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/stat.h>
#include <time.h>
#include <string.h>

#define FILENAME "Java.txt"  // The input file to be processed
#define MAX_THREADS 128       // Maximum number of threads
#define MAX_WORD_LENGTH 100   // Maximum length of a word

// Structure to hold data for each thread
typedef struct {
    int thread_id;            // Thread ID
    off_t start_offset;       // Start offset for the thread
    off_t end_offset;         // End offset for the thread
    int word_count;           // Word count for this segment
    char first_word[MAX_WORD_LENGTH]; // First word fragment (if split between segments)
    char last_word[MAX_WORD_LENGTH];  // Last word fragment (if split between segments)
} thread_data_t;

pthread_mutex_t lock;         // Mutex to protect shared data
int total_word_count = 0;     // Global word count

// Function to check if a character is a word delimiter
int is_delimiter(char ch) {
    return (ch == ' ' || ch == '\n' || ch == '\t' || 
            ch == ',' || ch == '.' || ch == ';' || 
            ch == ':' || ch == '!' || ch == '?' || 
            ch == '"' || ch == '\'' || ch == '(' || 
            ch == ')' || ch == '{' || ch == '}' || 
            ch == '[' || ch == ']' || ch == '&' || 
            ch == '#' || ch == '-' || ch == '/' || 
            ch == '=' || ch == '+');
}

// Function that each thread will run to count words in its segment
void* count_words(void* arg) {
    thread_data_t* data = (thread_data_t*)arg;
    int fd = open(FILENAME, O_RDONLY);
    if (fd < 0) {
        perror("Error opening file");
        pthread_exit(NULL);
    }

    lseek(fd, data->start_offset, SEEK_SET);

    int in_word = 0;           // Flag to track if inside a word
    char ch;                  // Character being processed
    off_t current_offset = data->start_offset; // Current position in the file
    char word_buffer[MAX_WORD_LENGTH]; // Buffer to store the current word
    int word_idx = 0;        // Index for the current word buffer

    // Handle partial word at the start of the segment
    if (data->start_offset != 0) {
        char prev_char;
        lseek(fd, data->start_offset - 1, SEEK_SET); // Check the character before the segment
        read(fd, &prev_char, 1);
        if (!is_delimiter(prev_char)) {
            // Skip the first word fragment
            while (read(fd, &ch, 1) == 1 && !is_delimiter(ch)) {
                current_offset++;
            }
        }
    }

    // Process the segment
    while (current_offset < data->end_offset && read(fd, &ch, 1) == 1) {
        if (is_delimiter(ch)) {
            if (in_word) {
                word_buffer[word_idx] = '\0'; // End the current word
                if (data->word_count == 0) {
                    strcpy(data->first_word, word_buffer); // Store the first word
                }
                data->word_count++;  // Increment word count
                word_idx = 0;        // Reset the word buffer
                in_word = 0;
            }
        } else {
            if (word_idx < MAX_WORD_LENGTH - 1) { // Store characters of the word
                word_buffer[word_idx++] = ch;
            }
            in_word = 1;
        }
        current_offset++;
    }

    // Handle a word at the end of the segment
    if (in_word) {
        word_buffer[word_idx] = '\0';
        strcpy(data->last_word, word_buffer); // Store the last word
    } else {
        data->last_word[0] = '\0'; // No last word if ended on delimiter
    }

    // Safely add this thread's count to the total count
    pthread_mutex_lock(&lock);
    total_word_count += data->word_count;
    pthread_mutex_unlock(&lock);

    close(fd);
    pthread_exit(NULL);
}

// Function to partition the file and create threads
void partition_file(int num_threads) {
    struct stat file_stat;
    int fd = open(FILENAME, O_RDONLY);
    if (fd < 0) {
        perror("Error opening file");
        exit(1);
    }

    if (fstat(fd, &file_stat) < 0) {
        perror("Error getting file size");
        close(fd);
        exit(1);
    }

    off_t file_size = file_stat.st_size;  // Get the total size of the file
    off_t segment_size = file_size / num_threads; // Calculate size of each segment
    close(fd);

    pthread_t threads[MAX_THREADS];
    thread_data_t thread_data[MAX_THREADS];

    // Reset total count before starting
    total_word_count = 0;

    // Create threads for each segment
    for (int i = 0; i < num_threads; i++) {
        thread_data[i].thread_id = i;
        thread_data[i].start_offset = i * segment_size; // Start offset for this segment
        thread_data[i].end_offset = (i == num_threads - 1) ? file_size : (i + 1) * segment_size; // End offset for this segment
        thread_data[i].word_count = 0; // Initialize word count to 0
        thread_data[i].first_word[0] = '\0'; // Initialize first word
        thread_data[i].last_word[0] = '\0'; // Initialize last word

        pthread_create(&threads[i], NULL, count_words, (void*)&thread_data[i]); // Create the thread
    }

    // Wait for all threads to finish
    for (int i = 0; i < num_threads; i++) {
        pthread_join(threads[i], NULL);
    }

    // Join results and adjust for boundary words
    for (int i = 0; i < num_threads - 1; i++) {
        if (strlen(thread_data[i].last_word) > 0 && strlen(thread_data[i + 1].first_word) > 0) {
            if (strcmp(thread_data[i].last_word, thread_data[i + 1].first_word) == 0) {
                total_word_count--;  // Decrement to avoid double counting split word
            }
        }
    }

    printf("Total word count: %d\n", total_word_count);
}

// Main program to test with 8, 32, 64, 128 segments
int main() {
    pthread_mutex_init(&lock, NULL);

    int num_threads[] = {8, 32, 64, 128};  // Test with different number of segments
    clock_t start, end;
    double execution_time;

    for (int i = 0; i < 4; i++) {
        start = clock();       // Start the clock
        partition_file(num_threads[i]);  // Partition and count words
        end = clock();         // End the clock
        execution_time = ((double)(end - start)) / CLOCKS_PER_SEC;
        printf("Execution time for %d segments: %f seconds\n", num_threads[i], execution_time);
    }

    pthread_mutex_destroy(&lock);
    return 0;
}
