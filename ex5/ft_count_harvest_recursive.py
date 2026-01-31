# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_recursive.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: klucchin <klucchin@student.42nice.fr>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/31 22:33:21 by klucchin          #+#    #+#              #
#    Updated: 2026/01/31 22:57:35 by klucchin         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def harvest(days, count=1):
    if count > days:
        print("Harvest time!")
        return
    print(f"Day {count}")
    harvest(days, count + 1)

Days = int(input("Days until harvest: "))
harvest(Days)
