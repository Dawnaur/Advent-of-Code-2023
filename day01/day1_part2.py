#!/usr/bin/python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    day1_part2.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: Dawnaur <dawnaur@42l.fr>                   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/12/01 06:22:52 by Dawnaur           #+#    #+#              #
#    Updated: 2023/12/01 07:01:12 by Dawnaur          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

total_value = 0
table = [ ("zero", 0), ("one", 1), ("two", 2), ("three", 3), ("four", 4),
		  ("five", 5), ("six", 6), ("seven", 7), ("eigh", 8), ("nine", 9) ]

fd = open(sys.argv[1], "r")
for line in fd.readlines():
	if (len(line) > 1):
		reversed_line = line
		for l in range(0, len(line)):
			for pattern in table:
				if line[l:].startswith(pattern[0]):
					line = line.replace(pattern[0], str(pattern[1]))
		for l in reversed(range(0, len(reversed_line))):
			for pattern in table:
				if reversed_line[l:].startswith(pattern[0]):
					reversed_line = reversed_line.replace(pattern[0], str(pattern[1]))
		first_digit = ""
		last_digit = ""
		for i in reversed(range(0, len(line))):
			if line[i].isdigit():
				first_digit = line[i]
		for i in range(0, len(reversed_line)):
			if reversed_line[i].isdigit():
				last_digit = reversed_line[i]
		total_value = total_value + int(first_digit + last_digit)
print(total_value)
