#!/usr/bin/python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    day05_part1.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: Dawnaur <dawnaur@42l.fr>                   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/12/05 06:26:13 by Dawnaur           #+#    #+#              #
#    Updated: 2023/12/05 07:44:28 by Dawnaur          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

result = []
task = 0
soil_map = []
fertilizer_map = []
water_map = []
light_map = []
temperature_map = []
humidity_map = []
location_map = []

def map_from_elem(elem, map):
	ret_list = []
	for map_elem in map:
		if (elem >= map_elem[0] and elem < map_elem[1]):
			ret_list.append(elem + map_elem[2] - map_elem[0])
	if (len(ret_list) == 0):
		ret_list.append(elem)
	return (ret_list)

def map_from_list(list, map):
	ret_list = []
	for elem in list:
		for map_elem in map:
			if (elem >= map_elem[0] and elem < map_elem[1]):
				ret_list.append(elem + map_elem[2] - map_elem[0])
		if (len(ret_list) == 0):
			ret_list.append(elem)
	return (ret_list)

def resolve(seed):
	soils = map_from_elem(seed, soil_map)
	fertilizers = map_from_list(soils, fertilizer_map)
	waters = map_from_list(fertilizers, water_map)
	lights = map_from_list(waters, light_map)
	temperatures = map_from_list(lights, temperature_map)
	humidities = map_from_list(temperatures, humidity_map)
	positions = map_from_list(humidities, location_map)
	return (positions)

with open(sys.argv[1], "r") as input_file:
	for line in input_file:
		if (len(line) > 1):
			if (task == 0):
				# get seeds
				seeds = line.split(":")[1][1:-1].split(" ")
			else:
				if line[0].isdigit():
					line_split = line.split(" ")
					if (task == 1):
						# get soil map
						soil_map.append([int(line_split[1]), int(line_split[1]) + int(line_split[2]), int(line_split[0])])
					elif (task == 2):
						# get fertilizer map
						fertilizer_map.append([int(line_split[1]), int(line_split[1]) + int(line_split[2]), int(line_split[0])])
					elif (task == 3):
						# get water map
						water_map.append([int(line_split[1]), int(line_split[1]) + int(line_split[2]), int(line_split[0])])
					elif (task == 4):
						# get light map
						light_map.append([int(line_split[1]), int(line_split[1]) + int(line_split[2]), int(line_split[0])])
					elif (task == 5):
						# get temperature map
						temperature_map.append([int(line_split[1]), int(line_split[1]) + int(line_split[2]), int(line_split[0])])
					elif (task == 6):
						# get humidity map
						humidity_map.append([int(line_split[1]), int(line_split[1]) + int(line_split[2]), int(line_split[0])])
					elif (task == 7):
						# get location map
						location_map.append([int(line_split[1]), int(line_split[1]) + int(line_split[2]), int(line_split[0])])
		else:
			task += 1
	for seed in seeds:
		result += resolve(int(seed))
	print(sorted(result)[0])
