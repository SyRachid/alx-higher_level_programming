#include "main.h"
/**
 * _strpbrk -function locates the first occurence in the string s of an
 * y of the bytes in the string accept
 *
 * @s:string
 *
 * @accept:character
 *
 * Return: pointer to the byte
 */
char *_strpbrk(char *s, char *accept)
{
	char *pointer;

	pointer = strpbrk(s, accept);
	return (pointer);
}
