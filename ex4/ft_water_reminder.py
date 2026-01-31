# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_water_reminder.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: klucchin <klucchin@student.42nice.fr>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/31 22:29:34 by klucchin          #+#    #+#              #
#    Updated: 2026/01/31 23:44:00 by klucchin         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def	ft_water_reminder():
	Watering = int(input("Days since last watering: "))
	if (Watering > 2):
		print("Water the plants!")
	else:
		print("Plants are fine")
ft_water_reminder()