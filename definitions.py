# The recurssively used functions for the program are placed here
from pickle import load, dump

# Login
def login(usrname:str, pswd:str):
    fr = open('authentification-details.dat', 'rb')
    crt_username, crt_password = load(fr)
    if crt_password == pswd and crt_username == usrname:
        return True
    else:
        return False

# Changeing Credentials
def change_credentials():
    usrname = input('Enter Current Username : ')
    pswrd = input('Enter Current Password : ')
    if login(usrname, pswrd):
        new_usrname = input('Enter New Username : ')
        new_passwd = input('Enter New Password : ')
        dump((new_usrname, new_passwd), open('authentification-details.dat', 'wb'))
        print('Credentials Successfully Changed!')
    else:
        return False

# Product Management
def view_product_details():
    with open('items-for-sale.txt') as f:
        products = eval(f.read())
    sn = 1
    name_max = 0
    price_space = 0
    cate_space = 0
    for i in products.keys():
        if len(i) > name_max:
            name_max = len(i)
    print('S.NO' + '  ' + 'NAME' + ' '*(name_max) + 'PRICE' + '     ' + 'CATEGORY' + '    ' + 'STOCK')
    print('----' + '  ' + '----' + ' '*(name_max) + '-----' + '     ' + '--------' + '    ' + '------')
    for i in products:
        price_space = (4 + name_max) - len(i)
        cate_space = 11 - (len(str(products[i]['price'])) + 1)
        stock_space = 12 - (len(str(products[i]['category'])))
        print(str(sn) + '     ' + products[i]['name'].title() + ' '*price_space + str(products[i]['price']) + ' '*cate_space + products[i]['category'].title()
             + ' '*stock_space + str(products[i]['stock']))
        sn += 1


def add_products():
    with open('items-for-sale.txt') as f:
        products = eval(f.read())
    product_add_no = int(input('Number of Products to be Added : '))
    for i in range(product_add_no):
        name = input('Enter Product Name : ')
        category = input('Enter Product Category : ')
        price = float(input('Enter Product Price : '))
        stock = float(input('Enter Product Stock : '))
        if name not in products.keys():
            products[name.lower()] = {'name' : name.lower(), 'category' : category.lower(), 'price': price, 'stock' : stock}
        else:
            return False
    with open('items-for-sale.txt', 'w') as f:
        f.write(str(products))
        print('Products Added!')


def remove_products():
    with open('items-for-sale.txt') as f:
        products = dict(eval(f.read()))
    product_remove_no = int(input('Number of Products to be Removed : '))
    for i in range(product_remove_no):
        name = input('Enter the Name of the Product to be Removed : ')
        if name.lower() in products.keys():
            del products[name]
        else:
            return False
    with open('items-for-sale.txt', 'w') as f:
        f.write(str(products))
        print('Products Removed!')


def modify_items():
    with open('items-for-sale.txt') as f:
        products = dict(eval(f.read()))
    products_modify_no = int(input('Enter the number of Products to be Modified : '))
    for i in range(products_modify_no):
        name = input('Enter the Name of the Product to be Modified : ')
        if name.lower() in products.keys():
            modification_category = int(input('Enter the Category Number to be Modified\n1. Name 2. Category 3. Price 4. Stock : '))
            if modification_category == 1:
                print('Current Name :', products[name.lower()]['name'].title())
                new_name = input('Enter the New Name : ').lower()
                pro_dict = products[name]
                pro_dict['name'] = new_name
                products[new_name] = pro_dict
                del products[name]
                name = new_name
                print('Name Modified!')
            elif modification_category == 2:
                print('Current Category :',products[name.lower()]['category'].title())
                new_cate = input('Enter the New Category : ').lower()
                products[name]['category'] = new_cate
                print('Category Modified!')
            elif modification_category == 3:
                print('Current Price :', str(products[name.lower()]['price']))
                new_price = float(input('Enter the new Price: '))
                products[name]['price'] = new_price
                print('Price Modified!')
            elif modification_category == 4:
                print('Current Stock :', str(products[name.lower()]['stock']))
                new_price = float(input('Enter the new Stock: '))
                products[name]['stock'] = new_price
                print('Stock Modified!')
            else:
                print('Invalid Command!')
    with open('items-for-sale.txt', 'w') as f:
        f.write(str(products))
# This is a comment