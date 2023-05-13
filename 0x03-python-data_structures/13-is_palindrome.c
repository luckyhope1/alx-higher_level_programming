#include "lists.h"

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: double pointer to the linked list
 *
 * Return: 1 if it is, 0 if not
 */

int is_palindrome(listint_t **head)
{
	if (*head == NULL)
	{
		return (1);
	}

	listint_t *slow = *head;
	listint_t *fast = *head;

	while (fast->next != NULL && fast->next->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
	}

	listint_t *prev = NULL;
	listint_t *curr = slow->next;

	while (curr != NULL)
	{
		listint_t *next = curr->next;

		curr->next = prev;
		prev = curr;
		curr = next;
	}

	listint_t *p1 = *head;
	listint_t *p2 = prev;

	while (p2 != NULL)
	{
		if (p1->n != p2->n)
		{
			return (0);
		}
		p1 = p1->next;
		p2 = p2->next;
	}
	return (1);
}
