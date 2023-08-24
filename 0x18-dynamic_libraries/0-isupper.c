#include "main.h"
/**
 * _isupper - function to determine if a character is uppercase or not
 *
 * @c: the input character
 *
 * Return:1 if is uppercase and 0 else
 */

int _isupper(int c)
{
	int type;

	if (isupper(c))
	{
		type = 1;
	}
	else
	{
		type = 0;
	}
	return (type);
}
