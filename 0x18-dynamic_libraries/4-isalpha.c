#include "main.h"
/**
 * _isalpha - to determine if the input is alpha type
 *
 * @c: the input of function
 *
 * Return: 1 if the input is alpha and 0 else
 */

int _isalpha(int c)
{
	if (isalpha(c))
	{
		return (1);
	}
	else
	{
		return (0);
	}
}
