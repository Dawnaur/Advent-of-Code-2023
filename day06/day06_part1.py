#!/usr/bin/python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    day06_part1.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: Dawnaur <dawnaur@42l.fr>                   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/12/06 06:05:10 by Dawnaur           #+#    #+#              #
#    Updated: 2023/12/06 06:18:24 by Dawnaur          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

result = 1
task = 0

with open(sys.argv[1], "r") as input_file:
	for line in input_file:
		if (len(line) > 1):
			if (task == 0):
				times = list(filter(None, line.split(":")[1][1:-1].strip().split(" ")))
			elif (task == 1):
				distances = list(filter(None, line.split(":")[1][1:-1].strip().split(" ")))
			task += 1
	for race in range(len(times)):
		race_wins = 0
		ref_distance = int(distances[race])
		time = int(times[race])
		for i in range(int(times[race])):
			if (i * (time - i) > ref_distance):
				race_wins += 1
		result *= race_wins
	print(result)
