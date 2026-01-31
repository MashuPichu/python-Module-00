# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_age.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: klucchin <klucchin@student.42nice.fr>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/31 22:25:13 by klucchin          #+#    #+#              #
#    Updated: 2026/01/31 23:40:52 by klucchin         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def	ft_plant_age():
	Age = int(input("Enter plant age in days: "))
	if (Age > 60):
		print("Plant is ready to harvest!")
	else:
		print("Plant needs more time to grow")
ft_plant_age()