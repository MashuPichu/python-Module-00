# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_garden_summary.py                              :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: klucchin <klucchin@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/03 17:59:36 by klucchin        #+#    #+#               #
#  Updated: 2026/02/03 17:59:41 by klucchin        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def ft_garden_summary():
    Name = str(input("Enter garden name: "))
    Plants = int(input("Enter number of plants: "))
    print(f"Garden: {Name}")
    print(f"Plants: {Plants}")
    print("Status: Growing well!")


ft_garden_summary()
