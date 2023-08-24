#include "main.h"
/**
 * _strchr -function to locates a character in a string
 *
 * @s: pointer to string
 *
 * @c: character to find
 *
 * Return: pointer
 */
char *_strchr(char *s, char c)
{
	char *pointer;

	pointer = strchr(s, c);
	return (pointer);
}
