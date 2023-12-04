#!/usr/bin/python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    day4_part2.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: Dawnaur <dawnaur@42l.fr>                   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/12/04 06:20:51 by Dawnaur           #+#    #+#              #
#    Updated: 2023/12/04 06:20:52 by Dawnaur          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

result = 0
winning_cards = [ 0 ]
card_id = 0

with open(sys.argv[1], "r") as input_file:
	for line in input_file:
		if (len(line) > 1):
			line_exp = 0
			card_id += 1
			if card_id <= len(winning_cards):
				winning_cards[card_id - 1] += 1
			else:
				winning_cards.append(1)
			input_datas = line.split(':')[1].replace("  ", " ").split('|')
			winning_numbers = input_datas[0].strip().split(' ')
			own_numbers = input_datas[1].strip().split(' ')
			for wn in winning_numbers:
				for on in own_numbers:
					if wn == on:
						line_exp += 1
			if (line_exp > 0):
				for i in range(card_id, card_id + line_exp):
					if i < len(winning_cards):
						winning_cards[i] += winning_cards[card_id - 1]
					else:
						winning_cards.append(winning_cards[card_id - 1])


for nb in winning_cards:
	result += nb
print(result)
