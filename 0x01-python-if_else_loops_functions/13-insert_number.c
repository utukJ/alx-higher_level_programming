#include "lists.h"

/**
* insert_node - inserts  node in a sorted singly linked list
* @head: head of the linked list.
* @number: data in the new node.
* Return: address of the new node.
*/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node;
	listint_t *new_node;
	listint_t *prev;

	prev = NULL;
	new_node = malloc(sizeof(listint_t));
	new_node->n = number;
	for (node = *head; node != NULL; node = node->next)
	{
		if (node->n >= number)
		{
			new_node->next = node;
			if (prev != NULL)
				prev->next = new_node;
			else
				head = &new_node;
			return new_node;
		}

		prev = node;
	}
	
	prev->next = new_node;
	return new_node;
}
