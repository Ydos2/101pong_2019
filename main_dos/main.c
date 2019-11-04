/*
** EPITECH PROJECT, 2019
** main
** File description:
** main
*/

#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include "../include/my.h"

int main(int ac, char **av)
{

    my_putstr(my_printf(av));
    return (0);
}