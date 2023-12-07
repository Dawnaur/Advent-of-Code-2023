#!/usr/bin/python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    day07_part1.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: Dawnaur <dawnaur@42l.fr>                   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/12/07 08:24:13 by Dawnaur           #+#    #+#              #
#    Updated: 2023/12/07 09:10:37 by Dawnaur          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

result = 0
hands = []

def compute_score(hand):
	values = [ 0 ] * 15
	hex_str = hand.replace('A', 'E').replace('K', 'D').replace('Q', 'C').replace('J', 'B').replace('T', 'A')
	score = int(hex_str[0], 16)
	tmp = sorted(hex_str)
	for card in tmp:
		values[int(card, 16)] += 1
	higher_card_nb = sorted(values)[-1]
	if (higher_card_nb == 5):
		score += 700
	elif (higher_card_nb == 4):
		score += 600
	elif (higher_card_nb == 3):
		if (sorted(values)[-2] == 2):
			score += 500
		else:
			score += 400
	elif (higher_card_nb == 2):
		if (sorted(values)[-2] == 2):
			score += 300
		else:
			score += 200
	elif (higher_card_nb == 1):
		score += 100
	return (str(score) + hex_str)

def order_hands(hands):
	for hand in hands:
		hand.append(compute_score(hand[0]))
	hands.sort(key=lambda x: x[2])

with open(sys.argv[1], "r") as input_file:
	for line in input_file:
		hands.append(line[:-1].split(" "))
	order_hands(hands)
	for i in range(len(hands)):
		result += (int(hands[i][1]) * (i + 1))
	print(result)