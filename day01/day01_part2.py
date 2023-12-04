#!/usr/bin/python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    day1_part2.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: Dawnaur <dawnaur@42l.fr>                   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/12/01 06:22:52 by Dawnaur           #+#    #+#              #
#    Updated: 2023/12/02 04:39:37 by Dawnaur          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

total_value = 0
table = [ ("zero", 0), ("one", 1), ("two", 2), ("three", 3), ("four", 4),
		  ("five", 5), ("six", 6), ("seven", 7), ("eight", 8), ("nine", 9) ]

fd = open(sys.argv[1], "r")
for line in fd.readlines():
	if (len(line) > 1):
		actual_value = ""
		for l in range(0, len(line)):
			if line[l].isdigit():
				actual_value = actual_value + line[l]
			else:
				for pattern in table:
					if line[l:].startswith(pattern[0]):
						actual_value = actual_value + str(pattern[1])
		total_value = total_value + int(actual_value[0] + actual_value[-1])
print(total_value)
