#include "main.h"
/**
 * *_strcpy -function to copy the string pointed by src including \0
 *
 * @dest: pointer of buffer
 *
 * @src: string to copy
 *
 * Return: dest
 */

char *_strcpy(char *dest, char *src)
{
	strcpy(dest, src);
	return (dest);
}
