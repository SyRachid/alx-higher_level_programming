#include "main.h"
/**
 * _strncpy - function to copy strings into another
 *
 * @dest: first string
 *
 * @src:source string
 *
 * @n: number
 *
 * Return: str
 */
char *_strncpy(char *dest, char *src, int n)
{
	char *str;

	str = strncpy(dest, src, n);

	return (str);
}
