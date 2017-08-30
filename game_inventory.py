# This is the file where you must work. Write code in the functions, create new functions,
# so they work according to the specification
import os


# Adds to the inventory dictionary a list of items from added_items.
def add_to_inventory(inventory, added_items):
    inventory.update(added_items)
    return inventory


def print_table(inventory, order="count,desc"):
    longest_item_name = max(len(x) for x in inventory)  # length of max keys in inventory
    frame = longest_item_name + 40
    print('{0}{1}{longest}{2}{3}{4}{5}'.format('Type', 'Weight','\t', 'Item Name', "\t", "How Many", longest=longest_item_name))
    print('-' * frame)
    if order == 'count,desc':
        for key, value in sorted(inventory.items(), key=lambda x: x[1], reverse=True):   # lambda return x[1]
            print(value[0],"\t",value[1],"\t", key, "\t\t", value[2])
    print('-' * frame)


# Imports new inventory items from a file
# The filename comes as an argument, but by default it's
# "import_inventory.csv". The import automatically merges items by name.
# The file format is plain text with comma separated values (CSV).
def import_inventory(inventory, filename="inventory.csv"):
    with open(filename) as f:
        inventory_from_file = f.read().split(',')
    inventory_from_file = list(filter(None, inventory_from_file))  # remove empty item
    add_to_inventory(inventory, inventory_from_file)  # add imported inventory


# Exports the inventory into a .csv file.
# if the filename argument is None it creates and overwrites a file
# called "export_inventory.csv". The file format is the same plain text
# with comma separated values (CSV).
def export_inventory(inventory, filename="inventory.csv"):
    os.remove(filename)  # remove file if it exist
    with open(filename, "a") as f:
        for key, value in inventory.items():
            f.write('{},'.format(key) * value)  # write to key values time to file
