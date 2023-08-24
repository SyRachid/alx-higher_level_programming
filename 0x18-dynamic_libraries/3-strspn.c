#include "main.h"
/**
 * _strspn - function that gets the length of a prefix substring
 *
 * @s:  the string
 *
 * @accept: the substring
 *
 * Return:len
 */
unsigned int _strspn(char *s, char *accept)
{
	unsigned int len;

	len = strspn(s, accept);
	return (len);
}
