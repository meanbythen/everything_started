#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Foods:
    """Foods class"""
    def __init__(self):
        self.foods_list = [
            ["Item", "Price"],
            ["apple", '5'],
            ["banana", '3'],
            ["orange", '4']
        ]

    def foods_list(self):
        """Print the list of foods items"""
        index_width = 5
        width = 35
        price_width = 10
        item_width = width - price_width - index_width
        header_format = "{{:<{}}}{{:<{}}}{{:>{}}}".format(index_width, item_width, price_width)
        fmt = "{{:<{}}}{{:<{}}}{{:>{}.2f}}".format(index_width, item_width, price_width)
        print("=" * width)
        for index, item in enumerate(self.foods_list):
            if index == 0:
                print(header_format.format(index, item[0], item[1]))
            else:
                print(fmt.format(index, item[0], float(item[1])))


class Cart:
    pass


class Pay:
    pass


class Menu:
    # def __int__(self):
    #     self.choice = ["Show Food List", "Add to Cart", "Remove from Cart", "Pay", "Exit"]

    def show_food_list(self, menu_list):
        """Show the list of food items"""
        for index, item in enumerate(menu_list):
            print(index + 1, item)


# foods_list = [
#     ["Item", "Price"],
#     ["apple", '5'],
#     ["banana", '3'],
#     ["orange", '4']
#     ]
menu_list = ["Show Food List", "Add to Cart", "Remove from Cart", "Pay", "Exit"]

foods = Foods()
menu = Menu()

view_menu = True

while view_menu:
    menu.show_food_list(menu_list)
    choice = int(input("Please input your choice: "))
    if choice == 1:
        foods.foods_list()
    # elif choice == 2: