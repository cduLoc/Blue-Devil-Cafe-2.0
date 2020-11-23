from collections import OrderedDict, namedtuple
from decimal import Decimal
from string import ascii_uppercase
AllMenu=[]
def tabular(table, widths):
    def sandwich(delim, contents):
        return delim + delim.join(contents) + delim
    def cell(value, width):
        return ' ' + str(value).ljust(width-2)
    def cells(row):
        return sandwich('|', (cell(col, w) for col, w in zip(row, widths))) + '\n'
    horiz_rule = sandwich('+', ('-' * (w - 1) for w in widths)) + '\n'
    return sandwich(horiz_rule, (cells(row) for row in table))

# In Python 3.7, this should be a @dataclass instead:
class Item(namedtuple('Item', 'name')):
    def __new__(cls, name):
        return super().__new__(cls, name)

def printmenu(title, id):
    print(
        tabular([[title]], [45 + 9]) +
        tabular(
            (('{0} {1.name}'.format(*stuff),)
             for stuff in AllMenu[id].items()),
            [45, 9]
        )
    )

def main():
    SectionNames=["Soup & Salad Bar", "Pizza Station"]
    menu_items1 = OrderedDict(zip(ascii_uppercase, [
        Item('Cowboy Texas Stew (with Chicken, Beef and Pork)'),
        Item('Ham and Cheese Wrap'),
        Item('Garden Salad'),
        Item('Coleslaw'),
        Item('Pineapple'),
        Item('Macaroni Salad'),
        Item('Cucumber Salad'),
        Item('Carrots/Hummus'),
        Item('Cereal Bars/Cookies'),
    ]))
    menu_items2 = OrderedDict(zip(ascii_uppercase, [
        Item('Taco Pizza'),
        Item('Pepperoni Pizza'),
        Item('Cheese Pizza'),
        Item('GF Pizza available upon request'),
    ]))

    global AllMenu
    AllMenu = [menu_items1, menu_items2]
    number = 1
    total = ''
    while True:
        for i in range(len(SectionNames)):
            print(str(i) +". " + SectionNames[i])

        temp = input("Choose menu or 'done': ")
        if temp == 'done':
            print('All: ' + total)
            break
        elif int(temp) <= len(SectionNames):
            printmenu(SectionNames[int(temp)],int(temp))
            while True:
                print('Selected: '+ total)
                selection = input("Select a letter or 'done': ")
                if selection == 'done':
                    break
                total += str(number)+". "+ AllMenu[int(temp)][selection].name + " "
                number= number + 1
    print('All: '+ total)

if __name__ == '__main__':
    main()
