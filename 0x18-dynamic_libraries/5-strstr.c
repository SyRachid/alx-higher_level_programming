#include "main.h"
/**
 * _strstr -function to locates a substring
 *
 * @haystack: string
 *
 * @needle: substring
 *
 * Return: pointer
 */
char *_strstr(char *haystack, char *needle)
{
	char *pointer;

	pointer = strstr(haystack, needle);
	return (pointer);
}
