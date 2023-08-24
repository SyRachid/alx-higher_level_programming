#include "main.h"
/**
 * _strncat - function to concatenates two strings
 *
 * @dest: first string;
 *
 * @src:second string;
 *
 * @n:the number of src bytes
 *
 * Return:str which is the value of concatenation
 */

char *_strncat(char *dest, char *src, int n)
{
	char *str;

	str = strncat(dest, src, n);

	return (str);
}
