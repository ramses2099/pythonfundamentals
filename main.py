# import module
import random

# write file mode
# 'w' for write
# 'r' for read
# 'a' for append
sales_log = open('spam_orders.txt', 'w')
sales_log.write('test test')
sales_log.close()

# create list
menu = ['Knackered Spam', 'Pip pip Spam', 'Squidgy Spam', 'Smashing Spam']
# create dictionary
menu_price = {}


def fill_menu():
    price = 0.5
    for item in menu:
        menu_price[item] = price
        price = price + 1


def print_menu():
    for name, price in menu_price.items():
        print(name, ': $', format(price, '.2f'), sep='')


def average(prices):
    avg = 0
    total = 0
    for price in prices:
        total = total + price
    avg = total/len(prices)
    return avg


def main():
    fill_menu()
    print_menu()
    print('avg :$', format(average(menu_price.values()), '.2f'), sep='')


if __name__ == '__main__':
    main()
