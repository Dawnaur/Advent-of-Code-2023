#!/usr/bin/python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    day3_part1.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: Dawnaur <dawnaur@42l.fr>                   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/12/03 05:59:24 by Dawnaur           #+#    #+#              #
#    Updated: 2023/12/03 07:30:35 by Dawnaur          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

result = 0
actual_symbols = []
previous_symbols = []
previous_line = ""

def get_number(str):
	i = 0
	while str[i].isdigit():
		i += 1
	return (int(str[:i]))

def	get_values(line, symbols_list):
	values_list = []
	i = 0
	print(symbols_list)
	while line[i] != '\n':
		if line[i].isdigit():
			end = i + 1
			while line[end].isdigit():
				end += 1
			min = i - 1 if i > 1 else 0
			max = end if end < len(line) else len(line)
			for symbol in symbols_list:
				if (int(symbol) >= min) and (int(symbol) <= max):
					values_list.append(i)
					break
			i = end - 1
		i += 1
	return (values_list)

with open(sys.argv[1], "r") as input_file:
	for line in input_file:
		if (len(line) > 1):
			previous_previous_symbols = previous_symbols
			previous_symbols = actual_symbols
			actual_symbols = []
			for i in range(len(line) - 1):
				if (not line[i].isdigit()) and (line[i] != '.'):
					actual_symbols.append(i)
			if (len(previous_line) > 1):
				values_list = get_values(previous_line, previous_previous_symbols)
				values_list += get_values(previous_line, previous_symbols)
				values_list += get_values(previous_line, actual_symbols)
				for index in list(set(values_list)):
					result += get_number(previous_line[index:])
			previous_line = line

	values_list = get_values(line, previous_symbols) + get_values(line, actual_symbols)
	for index in list(set(values_list)):
		result += get_number(previous_line[index:])
	print(result)
