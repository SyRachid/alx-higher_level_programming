#include "main.h"
/**
 * _isdigit - to determine if the input is a digit or not
 *
 * @c:th input of the function
 *
 * Return: 1 if the input is a digit or not
 */

int _isdigit(int c)
{
	int response;

	if (isdigit(c))
	{
		response = 1;
	}
	else
	{
		response = 0;
	}
	return (response);
}
