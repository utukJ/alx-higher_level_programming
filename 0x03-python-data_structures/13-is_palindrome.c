#include "lists.h"
#include <stdlib.h>

/**
 * reversed_linked_list - returns a reversed copy of a linked list 
 * 
 * @h: pointer to linked list 
 * Return: reversed linked_list pointer
 */
listint_t *reversed_linked_list(const listint_t *h)
{
    listint_t *tmp, *prev;

    prev = NULL;

    for (; h != NULL; h = h->next)
    {
        // create new node from current node in h
        tmp = malloc(sizeof(listint_t));
        tmp->n = h->n;

        // point the node to prev
        tmp->next = prev;

        // set prev as current node
        prev = tmp;
    }
    
    return tmp;
}

/**
 * compare_linked_lists - returns 1 if both linked lists are equal else 0 
 * 
 * @h1: pointer to linked list 
 * @h2: pointer to other linked lists 
 * Return: int 
 */
int compare_linked_lists(const listint_t *h1, const listint_t *h2)
{
    for (; h1 != NULL && h2 != NULL; h1 = h1->next, h2 = h2->next)
    {
        if (h1->n != h2->n)
            return 0;
    }
    return (h1 == NULL && h2 == NULL);
}

int is_palindrome(listint_t **head)
{
    listint_t *reversed = reversed_linked_list(*head);
    int result = compare_linked_lists(*head, reversed);
    free_listint(reversed);

    return result;
}