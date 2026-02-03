# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_plant_age.py                                   :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: klucchin <klucchin@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/03 17:53:29 by klucchin        #+#    #+#               #
#  Updated: 2026/02/03 17:54:49 by klucchin        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def ft_plant_age():
    Age = int(input("Enter plant age in days: "))
    if (Age > 60):
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow")


ft_plant_age()
