# The recurssively used functions for the program are placed here
from pickle import load, dump

# Login


def login(usrname: str, pswd: str):
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
        dump((new_usrname, new_passwd), open(
            'authentification-details.dat', 'wb'))
        print('Credentials Successfully Changed!')
    else:
        return False

# Product Management


def view_product_details():
    with open('products-for-sale.txt') as f:
        products = eval(f.read())
    sn = 1
    name_max = 0
    price_space = 0
    cate_space = 0
    price_max = 0
    cate_max = 0
    for i in products.keys():
        if len(products[i]['category']) > cate_max:
            cate_max = len(products[i]['category'])
    for i in products.keys():
        if len(str(products[i]['price'])) > price_max:
            price_max = len(str(products[i]['price']))
    for i in products.keys():
        if len(i) > name_max:
            name_max = len(i)
    print('S.NO' + '  ' + 'NAME' + ' '*(name_max) +
          'PRICE' + ' '*price_max + 'CATEGORY' + ' '*cate_max + 'STOCK')
    print('----' + '  ' + '----' + ' '*(name_max) +
          '-----' + ' '*price_max + '--------' + ' '*cate_max + '------')
    for i in products:
        price_space = (4 + name_max) - len(i)
        cate_space = (price_max + 6) - (len(str(products[i]['price'])) + 1)
        stock_space = (8 + cate_max) - (len(str(products[i]['category'])))
        print(str(sn) + '     ' + products[i]['name'].title() + ' '*price_space + str(products[i]['price']) + ' '*cate_space + products[i]['category'].title()
              + ' '*stock_space + str(round(products[i]['stock'], 1)))
        sn += 1


def add_products():
    with open('products-for-sale.txt') as f:
        products = eval(f.read())
    product_add_no = int(input('Number of Products to be Added : '))
    for i in range(product_add_no):
        name = input('Enter Product Name : ')
        category = input('Enter Product Category : ')
        price = float(input('Enter Product Price : '))
        stock = float(input('Enter Product Stock : '))
        if name not in products.keys():
            products[name.lower()] = {'name': name.lower(
            ), 'category': category.lower(), 'price': price, 'stock': stock}
        else:
            return False
    with open('products-for-sale.txt', 'w') as f:
        f.write(str(products))
        print('Products Added!')


def remove_products():
    with open('products-for-sale.txt') as f:
        products = dict(eval(f.read()))
    product_remove_no = int(input('Number of Products to be Removed : '))
    for i in range(product_remove_no):
        name = input('Enter the Name of the Product to be Removed : ')
        if name.lower() in products.keys():
            del products[name]
        else:
            return False
    with open('products-for-sale.txt', 'w') as f:
        f.write(str(products))
        print('Products Removed!')


def modify_products():
    with open('products-for-sale.txt') as f:
        products = dict(eval(f.read()))
    products_modify_no = int(
        input('Enter the number of Products to be Modified : '))
    for i in range(products_modify_no):
        name = input('Enter the Name of the Product to be Modified : ')
        if name.lower() in products.keys():
            modification_category = int(input(
                'Enter the Category Number to be Modified\n1. Name 2. Category 3. Price 4. Stock : '))
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
                print('Current Category :',
                      products[name.lower()]['category'].title())
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
    with open('products-for-sale.txt', 'w') as f:
        f.write(str(products))

# Billing Software


def update_stock(purchase_dict):
    with open('products-for-sale.txt') as f:
        products = eval(f.read())
    for i in purchase_dict:
        products[i]['stock'] -= purchase_dict[i]
    with open('products-for-sale.txt', 'w') as f:
        f.write(str(products))


def get_purchase_list():
    with open('products-for-sale.txt') as f:
        products = dict(eval(f.read()))
    items_purchased = {}
    print('--Enter \'quit\' to Quit--')
    print()
    while True:
        item = input('Enter Product Purchased : ').lower()
        if item == 'quit':
            break
        elif item not in products.keys():
            print('Invalid Input')
            continue
        quantity = float(input('Enter Quantity : '))
        if quantity > products[item]['stock']:
            print(
                'Purchased quantity greater than total stock. Please check the Quantity.')
            continue
        items_purchased[item] = quantity
    return items_purchased


def bill(purchase_dict):
    with open('supermarket-details.txt') as f:
        details = eval(f.read())
    with open('products-for-sale.txt') as f:
        products = eval(f.read())
    sn = 1
    print()
    print('\t     {}'.format(details['name'].upper()))
    print('        {}'.format(details['address']))
    print('\t      Ph: {}'.format(str(details['phone'])))
    print()
    rate_space = 0
    name_max = 0
    quantity_space = 0
    total_cost = 0
    for i in purchase_dict.keys():
        if len(str(products[i]['price'])) > rate_space:
            rate_space = len(str(products[i]['price']))
    for i in purchase_dict.keys():
        if len(i) > name_max:
            name_max = len(i)
    for i in purchase_dict:
        if len(str(purchase_dict[i])) > quantity_space:
            quantity_space = len(str(purchase_dict[i]))
    print('S.NO' + '  ' + 'PRODUCT' + ' '*name_max +
          'RATE' + ' '*rate_space + 'QUANTITY' + ' '*quantity_space + 'AMOUNT')
    print('----' + '  ' + '-------' + ' '*name_max +
          '----' + ' '*rate_space + '--------' + ' '*quantity_space + '-------')
    for i in purchase_dict:
        rate_space = (rate_space + 4) - len(str(products[i]['price']))
        product_space = (name_max + 7) - len(i)
        amount_space = (8 + quantity_space) - len(str(purchase_dict[i]))
        print(str(sn) + '     ' + i.title() + ' ' *
              product_space + str(products[i]['price']) + ' '*rate_space + str(purchase_dict[i]) + ' '*amount_space + str(purchase_dict[i]*products[i]['price']))
        total_cost += purchase_dict[i]*products[i]['price']
        sn += 1
    spaces = 4 + 2 + 7 + name_max + 4 + rate_space + 8 + quantity_space + 8
    print('-'*(spaces))
    print('Total Amount : {}'.format(str(total_cost)))
    print()
    print('\t       Visit Again!')
    update_stock(purchase_dict)
