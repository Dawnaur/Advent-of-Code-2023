#!/usr/bin/python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    day2_part1.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: Dawnaur <dawnaur@42l.fr>                   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/12/01 06:03:15 by Dawnaur           #+#    #+#              #
#    Updated: 2023/12/01 06:36:57 by Dawnaur          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

nb_red_cubes = int(sys.argv[2])
nb_green_cubes = int(sys.argv[3])
nb_blue_cubes = int(sys.argv[4])
result = 0

with open(sys.argv[1], "r") as input_file:
	for line in input_file:
		if (len(line) > 1):
			input_table = line[:-1].split(':')
			game_id = int(input_table[0].split(' ')[1])
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
			if (max_red <= nb_red_cubes) and (max_green <= nb_green_cubes) and (max_blue <= nb_blue_cubes):
				result += game_id
	print(result)
