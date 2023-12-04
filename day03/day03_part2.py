#!/usr/bin/python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    day3_part2.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: Dawnaur <dawnaur@42l.fr>                   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/12/04 08:02:17 by Dawnaur           #+#    #+#              #
#    Updated: 2023/12/04 08:33:52 by Dawnaur          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

result = 0
actual_symbols = []
previous_symbols = []
previous_line = ""
actual_line = ""

def get_number(str):
	i = 0
	while str[i].isdigit():
		i += 1
	return (int(str[:i]))

def	get_values(line, symbol):
	values_list = []
	i = 0
	while line[i] != '\n':
		if line[i].isdigit():
			end = i + 1
			while line[end].isdigit():
				end += 1
			min = i - 1 if i > 1 else 0
			max = end if end < len(line) else len(line)
			if (int(symbol) >= min) and (int(symbol) <= max):
				values_list.append([i, get_number(line[i:])])
			i = end - 1
		i += 1
	return (values_list)

with open(sys.argv[1], "r") as input_file:
	for line in input_file:
		if (len(line) > 1):
			previous_previous_line = previous_line
			previous_line = actual_line
			actual_line = line
			previous_symbols = actual_symbols
			actual_symbols = []
			for i in range(len(line) - 1):
				if (not line[i].isdigit()) and (line[i] != '.'):
					actual_symbols.append(i)
			if (len(previous_line) > 1):

				for symbol in previous_symbols:
					nb_symbol_match = get_values(previous_previous_line, symbol)
					nb_symbol_match += get_values(previous_line, symbol)
					nb_symbol_match += get_values(actual_line, symbol)
					if (len(nb_symbol_match) == 2):
						result += (nb_symbol_match[0][1] * nb_symbol_match[1][1])
	print(result)
