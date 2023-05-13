#include "lists.h"

#include <stddef.h>

/**
 * is_palindrome- Checks if a singly linked list is a palindrome.
 * @head: Head pointer
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome.
 */
int is_palindrome(listint_t **head)
{
	listint_t *node;
	int values[9999], k = 0, p = 0;

	if ((!*head) || (!head))
	{
		return (1);
	}
	node = *head;
	if (!node->next)
	{
		return (1);
	}
	while (node)
	{
		values[k] = node->n;
		node = node->next;
		k++;
	}
	k--;
	while (k >= 0 && p <= k)
	{
		if (values[k] != values[p])
		{
			return (0);
		}
		k--;
		p++;
	}
	return (1);
}
