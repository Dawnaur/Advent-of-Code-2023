#!/usr/bin/python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    day2_part2.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: Dawnaur <dawnaur@42l.fr>                   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/12/02 06:37:37 by Dawnaur           #+#    #+#              #
#    Updated: 2023/12/02 06:42:27 by Dawnaur          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

result = 0

with open(sys.argv[1], "r") as input_file:
	for line in input_file:
		if (len(line) > 1):
			input_table = line[:-1].split(':')
			game_samples_str = input_table[1][1:].replace("; ", ";").split(';')
			max_red = 0
			max_green = 0
			max_blue = 0
			for game_samples in game_samples_str:
				sample = game_samples.replace(", ", ",").split(',')
				for cube_str in sample:
					cube = cube_str.split(' ')
					value = int(cube[0])
					if (cube[1] == "red") and (value > max_red):
						max_red = value
					if (cube[1] == "green") and (value > max_green):
						max_green = value
					if (cube[1] == "blue") and (value > max_blue):
						max_blue = value
			result += max_red * max_green * max_blue
	print(result)
