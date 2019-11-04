/*
** EPITECH PROJECT, 2019
** criterion
** File description:
** criterion
*/

#include <criterion/criterion.h>
#include <criterion/redirect.h>
#include "../include/my.h"

void redirect_all_std(void)
{
    cr_redirect_stdout();
    cr_redirect_stderr();
}

Test(sum_stdarg, return_correct_when_i_is_zero)
{
    int ret = sum_stdarg(0, 3, 21, 25, -4);

    cr_assert_eq(ret, 42);
}

Test(my_printf, simple_string, .init = redirect_all_std)
{
    my_printf("hello world");
    cr_assert_stdout_eq_str("hello world");
}