#!/usr/bin/python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    day4_part1.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: Dawnaur <dawnaur@42l.fr>                   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/12/04 06:02:54 by Dawnaur           #+#    #+#              #
#    Updated: 2023/12/04 06:17:12 by Dawnaur          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

result = 0

with open(sys.argv[1], "r") as input_file:
	for line in input_file:
		if (len(line) > 1):
			line_exp = 0
			input_datas = line.split(':')[1].replace("  ", " ").split('|')
			winning_numbers = input_datas[0].strip().split(' ')
			own_numbers = input_datas[1].strip().split(' ')
			for wn in winning_numbers:
				for on in own_numbers:
					if wn == on:
						line_exp += 1
			if (line_exp > 0):
				result += (2**(line_exp - 1))
	print(result)
