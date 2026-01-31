# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_iterative.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: klucchin <klucchin@student.42nice.fr>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/31 22:33:39 by klucchin          #+#    #+#              #
#    Updated: 2026/01/31 22:53:08 by klucchin         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

Days = int(input("Days until harvest: "))
count = 1

while (count <= Days):
	print(f"Day {count}")
	count += 1
print("Harvest time!")