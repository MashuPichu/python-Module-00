# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_harvest_total.py                               :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: klucchin <klucchin@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/03 17:52:57 by klucchin        #+#    #+#               #
#  Updated: 2026/02/03 17:53:15 by klucchin        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def ft_harvest_total():
    Day1 = int(input("Day 1 harvest: "))
    Day2 = int(input("Day 2 harvest: "))
    Day3 = int(input("Day 3 harvest: "))
    print(f"Total harvest: {Day1 + Day2 + Day3}")


ft_harvest_total()
