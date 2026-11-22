//preprocessor directives for threads/semaphores/etc.
#include <pthread.h>
#include <semaphore.h>
#include <stdlib.h>
#include <stdio.h>

#define MaxOperations 5 // Each producer or consumer will perform 5 operations
#define BufferSize 5    // Size of the shared buffer

sem_t emptySlots; // Counts empty slots in the buffer
sem_t fullSlots;  // Counts filled slots in the buffer
int in = 0;       // Index to insert into buffer
int out = 0;      // Index to remove from buffer
int buffer[BufferSize]; // Shared buffer
pthread_mutex_t mutex;  // Mutex lock for mutual exclusion

void* producer(void* id)
{
    int item;
    for (int i = 0; i < MaxOperations; i++) 
    {
        item = rand(); // Produce some data
        sem_wait(&emptySlots); // Wait if buffer is full
        pthread_mutex_lock(&mutex); // Enter critical section

        buffer[in] = item; // Place item into buffer
        printf("Producer %d: Inserted %d at %d\n", *((int*)id), buffer[in], in);
        in = (in + 1) % BufferSize;

        pthread_mutex_unlock(&mutex); // Exit critical section
        sem_post(&fullSlots); // Signal that a new item is available
    }
}

void* consumer(void* id)
{
    for (int i = 0; i < MaxOperations; i++) 
    {
        sem_wait(&fullSlots); // Wait if buffer is empty
        pthread_mutex_lock(&mutex); // Enter critical section

        int item = buffer[out]; // Consume item from buffer
        printf("Consumer %d: Removed %d from %d\n", *((int*)id), item, out);
        out = (out + 1) % BufferSize;

        pthread_mutex_unlock(&mutex); // Exit critical section
        sem_post(&emptySlots); // Signal that a slot is free
    }
}

int main()
{
    pthread_t producers[5], consumers[5];
    pthread_mutex_init(&mutex, NULL);

    sem_init(&emptySlots, 0, BufferSize); // Buffer starts empty
    sem_init(&fullSlots, 0, 0);           // No filled slots at start

    int ids[5] = { 1, 2, 3, 4, 5 };

    for (int i = 0; i < 5; i++) 
    {
        pthread_create(&producers[i], NULL, producer, (void*)&ids[i]);
        pthread_create(&consumers[i], NULL, consumer, (void*)&ids[i]);
    }

    for (int i = 0; i < 5; i++) 
    {
        pthread_join(producers[i], NULL);
        pthread_join(consumers[i], NULL);
    }

    pthread_mutex_destroy(&mutex);
    sem_destroy(&emptySlots);
    sem_destroy(&fullSlots);

    return 0;
}
