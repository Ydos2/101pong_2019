##
## EPITECH PROJECT, 2019
## COMPILATION
## File description:
## Makefile
##

PY	=	101pong.py
NEW	=	101pong

all	: make

make:
		cp $(PY) $(NEW)

fclean:
		rm -f $(NEW)

re: fclean make