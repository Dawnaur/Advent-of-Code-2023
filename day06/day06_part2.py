#!/usr/bin/python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    day06_part2.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: Dawnaur <dawnaur@42l.fr>                   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/12/06 06:19:41 by Dawnaur           #+#    #+#              #
#    Updated: 2023/12/06 06:52:13 by Dawnaur          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import math

task = 0

with open(sys.argv[1], "r") as input_file:
	for line in input_file:
		if (len(line) > 1):
			if (task == 0):
				str_time = "".join(list(filter(None, line.split(":")[1][1:-1].strip().split(" "))))
			elif (task == 1):
				str_distance = "".join(list(filter(None, line.split(":")[1][1:-1].strip().split(" "))))
			task += 1
	ref_distance = int(str_distance)
	time = int(str_time)
	# i * (time - i) > ref_distance -> looking for ((i * (time - i)) == ref_distance)
	# -> resolving: 0 = i² - time i + ref_distance
	delta =(-time)**2 - 4 * ref_distance
	b1 = (time - math.sqrt(delta)) / 2
	b2 = (time + math.sqrt(delta)) / 2
	print(1 + math.floor(b2) - math.ceil(b1))
