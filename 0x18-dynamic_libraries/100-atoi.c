#include "main.h"
#include <stdlib.h>
/**
 * _atoi - function to transform string to int
 *
 * @s: string to convert
 *
 * Return: nume -pointer to int
 */
int *_atoi(char *s)
{
	int num = atoi(s);
	int *nume = &num;

	return (nume);
}
