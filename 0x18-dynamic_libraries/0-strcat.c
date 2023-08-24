#include "main.h"
/**
 * _strcat - function to concatenates two strings
 *
 * @dest: first string
 *
 * @src: second string
 *
 * Return: str pointer to string
 */

char *_strcat(char *dest, char *src)
{
	char *str;

	str = strcat(dest, src);
	return (str);
}
