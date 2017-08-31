import random

#def add_to_inventory(inventory, added_items):
#    inventory.update(added_items)
#    return inventory


def print_table(inventory):
    longest_item_name = max(len(x) for x in inventory)  # length of max keys in inventory
    frame = longest_item_name + 30
    print('{0:>7}\t{1:>{longest}} '.format('count', 'item name', longest=longest_item_name))
    print('-' * frame)
    for key, value in sorted(inventory.items(), key=lambda x: x[1], reverse=True):   # lambda return x[1]
        print('{0:>7}{1:>{longest}}{2}{3}'.format(value[1], key, value[2], value[0], longest=longest_item_name))
    print('-' * frame)


def add_to_inventory(inventory, added_item):
    if added_item[0] in inventory:
        inventory[added_item[0]][2]  += added_item[3]
        inventory[added_item[0]][1] = inventory[added_item[0]][2] * added_item[2]
    else:
        inventory[added_item[0]] = [added_item[1], added_item[2], added_item[3]]
    return inventory

#def print_table(inventory):
#    for i in range (0, len(inventory)):
#        print()
