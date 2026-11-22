//libraries for basic functions with linked lists
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stddef.h>

#define FRAME_SIZE 3 // Memory frame size
#define MAX_PAGE_REFERENCES 100 // Maximum number of page references per line

// Node for LRU using doubly-linked list
typedef struct LRU_Node 
{
    int page;
    struct LRU_Node *prev, *next;
} LRU_Node;

// Node for Clock using circular doubly-linked list
typedef struct Clock_Node 
{
    int page;
    int second_chance;
    struct Clock_Node *prev, *next;
} Clock_Node;

LRU_Node *lru_head = NULL, *lru_tail = NULL;
Clock_Node *clock_head = NULL, *clock_hand = NULL;

// Function to create a new LRU node
LRU_Node* create_LRU_node(int page) 
{
    LRU_Node* new_node = (LRU_Node*)malloc(sizeof(LRU_Node));
    new_node->page = page;
    new_node->prev = new_node->next = NULL;
    return new_node;
}

// insert a page in LRU stack
void insert_page_LRU(int page) 
{
    LRU_Node* current_node = lru_head;
    while (current_node != NULL) 
    {
        if (current_node->page == page) 
        {
            if (current_node != lru_head) 
            {
                if (current_node->next) current_node->next->prev = current_node->prev;
                if (current_node->prev) current_node->prev->next = current_node->next;
                if (current_node == lru_tail) lru_tail = current_node->prev;

                current_node->next = lru_head;
                lru_head->prev = current_node;
                lru_head = current_node;
                current_node->prev = NULL;
            }
            return;
        }
        current_node = current_node->next;
    }

    LRU_Node* new_node = create_LRU_node(page);
    new_node->next = lru_head;
    if (lru_head) lru_head->prev = new_node;
    lru_head = new_node;
    if (!lru_tail) lru_tail = new_node;

    int nodeCount = 0;
    for (current_node = lru_head; current_node != NULL; current_node = current_node->next) nodeCount++;
    if (nodeCount > FRAME_SIZE) 
    {
        LRU_Node* old_tail = lru_tail;
        if (lru_tail->prev) lru_tail->prev->next = NULL;
        lru_tail = lru_tail->prev;
        free(old_tail);
    }
}

// display the LRU stack (3 pages per line)
void display_LRU_stack() 
{
    LRU_Node* current_node = lru_head;
    int nodeCount = 0;
    while (current_node && nodeCount < FRAME_SIZE) 
    {
        printf("%d", current_node->page);
        if (nodeCount < FRAME_SIZE - 1) printf(" ");
        current_node = current_node->next;
        nodeCount++;
    }
    printf("\n");
}

// create a new Clock node
Clock_Node* create_clock_node(int page) 
{
    Clock_Node* new_node = (Clock_Node*)malloc(sizeof(Clock_Node));
    new_node->page = page;
    new_node->second_chance = 1;
    new_node->prev = new_node->next = NULL;
    return new_node;
}

// insert a page in Clock list
void insert_page_clock(int page) 
{
    if (!clock_head) return;

    Clock_Node* current_node = clock_head;
    do 
    {
        if (current_node->page == page) 
        {
            current_node->second_chance = 1;
            return;
        }
        current_node = current_node->next;
    } while (current_node && current_node != clock_head);

    while (clock_hand->second_chance) 
    {
        clock_hand->second_chance = 0;
        clock_hand = clock_hand->next;
    }

    clock_hand->page = page;
    clock_hand->second_chance = 1;
    clock_hand = clock_hand->next;
}

// display the Clock list (3 pages per line)
void display_clock_list() 
{
    if (!clock_head) return;

    Clock_Node* current_node = clock_head;
    int nodeCount = 0;
    do {
        printf("%d", current_node->page);
        if (current_node->second_chance) printf("*");
        nodeCount++;
        if (nodeCount < FRAME_SIZE) printf(" ");
        if (nodeCount == FRAME_SIZE) break;
        current_node = current_node->next;
    } while (current_node && current_node != clock_head);
    printf("\n");
}

// initialize the Clock list
void initialize_clock_list() 
{
    clock_head = NULL;
    clock_hand = NULL;

    for (int i = 0; i < FRAME_SIZE; i++) 
    {
        Clock_Node* new_node = create_clock_node(-1);
        if (!clock_head) 
        {
            clock_head = new_node;
            clock_hand = new_node;
            clock_head->next = clock_head;
            clock_head->prev = clock_head;
        } else 
        {
            Clock_Node* tail = clock_head->prev;
            tail->next = new_node;
            new_node->prev = tail;
            new_node->next = clock_head;
            clock_head->prev = new_node;
        }
    }
}

// free LRU list
void free_LRU_list() 
{
    while (lru_head != NULL) 
    {
        LRU_Node* current_node = lru_head;
        lru_head = lru_head->next;
        free(current_node);
    }
    lru_tail = NULL;
}

// free Clock list
void free_clock_list() 
{
    if (!clock_head) return;
    Clock_Node* current_node = clock_head;
    do 
    {
        Clock_Node* temp_node = current_node;
        current_node = current_node->next;
        free(temp_node);
    } while (current_node != clock_head);
    clock_head = clock_hand = NULL;
}

// read pages from file and process each line of references
void read_pages_from_file(const char *filename) 
{
    FILE *file = fopen(filename, "r");
    if (!file) 
    {
        perror("Failed to open file"); // file error checking
        exit(1);
    }

    char line[256];
    int page_references[MAX_PAGE_REFERENCES];

    int line_number = 0;
    while (fgets(line, sizeof(line), file)) 
    {
        line_number++;
        printf("\nProcessing reference line %d:\n", line_number);

        int refCount = 0;
        char *token = strtok(line, ",");
        while (token && refCount < MAX_PAGE_REFERENCES) 
        {
            page_references[refCount++] = atoi(token);
            token = strtok(NULL, ",");
        }

        printf("LRU Replacement:\n");
        free_LRU_list();
        for (int i = 0; i < refCount; i++) 
        {
            insert_page_LRU(page_references[i]);
            display_LRU_stack();
        }

        free_clock_list();
        initialize_clock_list();
        printf("Clock Replacement:\n");
        for (int i = 0; i < refCount; i++) 
        {
            insert_page_clock(page_references[i]);
            display_clock_list();
        }
    }
    fclose(file); // close file 
}

int main() 
{
    read_pages_from_file("Pages.txt"); // input.txt file
    return 0;
}
