# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_count_harvest_iterative.py                     :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: klucchin <klucchin@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/03 17:56:22 by klucchin        #+#    #+#               #
#  Updated: 2026/02/03 18:23:00 by klucchin        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def ft_count_harvest_iterative():
    Days = int(input("Days until harvest: "))
    count = 1
    while (count <= Days):
        print(f"Day {count}")
        count += 1
    print("Harvest time!")


ft_count_harvest_iterative()
