#include "main.h"
/**
 * _memset - function to print the first n bytes of the memory area poin
 * ed by s with the constant byte b
 *
 * @s: a pointer
 *
 * @b: a constant byte
 *
 * @n: the fisrt n bytes
 *
 * Return: pointer
 *
 */
char *_memset(char *s, char b, unsigned int n)
{
	char *pointer;


	pointer = memset(s, b, n);
	return (pointer);
}
