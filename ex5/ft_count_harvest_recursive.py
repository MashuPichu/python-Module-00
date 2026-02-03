# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_count_harvest_recursive.py                     :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: klucchin <klucchin@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/03 17:58:16 by klucchin        #+#    #+#               #
#  Updated: 2026/02/03 18:35:50 by klucchin        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def ft_count_harvest_recursive(days, count=1):
    if count > days:
        print("Harvest time!")
        return
    print(f"Day {count}")
    ft_count_harvest_recursive(days, count + 1)


days = int(input("Days until harvest: "))
ft_count_harvest_recursive(days)
