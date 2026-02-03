# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_water_reminder.py                              :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: klucchin <klucchin@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/03 17:55:00 by klucchin        #+#    #+#               #
#  Updated: 2026/02/03 17:55:23 by klucchin        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def ft_water_reminder():
    Watering = int(input("Days since last watering: "))
    if (Watering > 2):
        print("Water the plants!")
    else:
        print("Plants are fine")


ft_water_reminder()
