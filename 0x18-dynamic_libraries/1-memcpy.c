#include "main.h"
/**
 * _memcpy -function to copy n bytes from memory area src to memory area
 * dest
 *
 * @dest : char pointer to have bytes
 *
 * @src: char pointer containing bytes to copy
 *
 * @n: the length of byte to copy
 *
 * Return: pointer to dest
 */
char *_memcpy(char *dest, char *src, unsigned int n)
{
	char *pointer;

	pointer = memcpy(dest, src, n);
	return (pointer);
}
