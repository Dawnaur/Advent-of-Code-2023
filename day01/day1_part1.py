#!/usr/bin/python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    day1_part1.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: Dawnaur <dawnaur@outlook.fr>               +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/12/01 06:00:44 by Dawnaur           #+#    #+#              #
#    Updated: 2023/12/01 06:20:38 by Dawnaur          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

total_value = 0

fd = open(sys.argv[1], "r")
for line in fd.readlines():
	if (len(line) > 1):
		actual_value = ""
		for c in line:
			if c.isdigit():
				actual_value = actual_value + c
		total_value = total_value + int(actual_value[0] + actual_value[-1])
print(total_value)
