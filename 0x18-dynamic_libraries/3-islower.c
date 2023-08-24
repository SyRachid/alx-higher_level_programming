#include "main.h"
/**
 * _islower - determine the if character is lowercase or uppercase
 *
 * @c : - character
 *
 * Return: 1 if the character is lowercase and 0 else.
 */

int _islower(int c)
{
	if (islower(c))
	{
		return (1);
	}
	else
	{
		return (0);
	}
}
