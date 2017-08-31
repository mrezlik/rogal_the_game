import random
import os
#def add_to_inventory(inventory, added_items):
#    inventory.update(added_items)
#    return inventory


def print_table(inventory):
    os.system('clear')
    longest_item_name = max(len(x) for x in inventory)  # length of max keys in inventory
    frame = longest_item_name + 30
    print('{0:>7}\t{1:>13}\t{2}\t{3}'.format('weight', 'item name', "count", "type"))
    print('-' * frame)
    for key, value in sorted(inventory.items(), key=lambda x: x[1], reverse=True):   # lambda return x[1]
        print('{0:>7}\t{1:>13}\t  {2}\t{3}'.format(value[1], key, value[2], value[0]))
    print('-' * frame)
    print("Press any key to exit")

def add_to_inventory(inventory, added_item):
    if added_item[0] in inventory:
        inventory[added_item[0]][2]  += added_item[3]
        inventory[added_item[0]][1] = inventory[added_item[0]][2] * added_item[2]
    else:
        inventory[added_item[0]] = [added_item[1], added_item[2], added_item[3]]
    return inventory

def remove_item(item, inventory)
    inventory[item][2] -= 1
    inventory[item][1] = inventory[added_item[0]][2] * added_item[2]
    return inventory
#def print_table(inventory):
#    for i in range (0, len(inventory)):
#        print()
