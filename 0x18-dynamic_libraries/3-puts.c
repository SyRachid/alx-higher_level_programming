#include "main.h"
/**
 * _puts - function thats prints a string
 *
 * @str: pointer of string to print
 * return: void
 */

void _puts(char *str)
{
	int i;
	int len = strlen(str);

	for (i = 0; i < len; i++)
	{
		_putchar(str[i]);
	}
	_putchar('\n');
}
