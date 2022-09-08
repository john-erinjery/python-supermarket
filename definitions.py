# The recurssively used functions for the program are placed here
from pickle import load, dump

# Login


def login():
    usrname = input('Enter Username : ')
    pswd = input('Enter Password : ')
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
    fr = open('authentification-details.dat', 'rb')
    crt_username, crt_password = load(fr)
    if crt_password == pswrd and crt_username == usrname:
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
    n = 0
    while n < product_remove_no:
        name = input('Enter the Name of the Product to be Removed : ')
        if name.lower() in products.keys():
            del products[name]
        else:
            print('No such product. Please check and Try again!')
            continue
        n += 1
    with open('products-for-sale.txt', 'w') as f:
        f.write(str(products))
        print('Products Removed!')


def update_products():
    with open('products-for-sale.txt') as f:
        products = dict(eval(f.read()))
    products_modify_no = int(
        input('Enter the number of Products to be updated : '))
    n = 0
    while n < products_modify_no:
        name = input('Enter the Name of the Product to be updated : ')
        if name.lower() in products.keys():
            modification_category = int(input(
                'Enter the Category Number to be updated\n1. Name 2. Category 3. Price 4. Stock : '))
            if modification_category == 1:
                print('Current Name :', products[name.lower()]['name'].title())
                new_name = input('Enter the New Name : ').lower()
                pro_dict = products[name]
                pro_dict['name'] = new_name
                products[new_name] = pro_dict
                del products[name]
                name = new_name
                print('Name updated!')
            elif modification_category == 2:
                print('Current Category :',
                      products[name.lower()]['category'].title())
                new_cate = input('Enter the New Category : ').lower()
                products[name]['category'] = new_cate
                print('Category updated!')
            elif modification_category == 3:
                print('Current Price :', str(products[name.lower()]['price']))
                new_price = float(input('Enter the new Price: '))
                products[name]['price'] = new_price
                print('Price updated!')
            elif modification_category == 4:
                print('Current Stock :', str(products[name.lower()]['stock']))
                new_price = float(input('Enter the new Stock: '))
                products[name]['stock'] = new_price
                print('Stock updated!')
            else:
                print('Invalid Command!')
                continue
        else:
            print('No Such Product. Please check and try again!')
            continue
        n += 1
    with open('products-for-sale.txt', 'w') as f:
        f.write(str(products))


def update_stock(purchase_dict):
    with open('products-for-sale.txt') as f:
        products = eval(f.read())
    for i in purchase_dict:
        products[i]['stock'] -= purchase_dict[i]
    with open('products-for-sale.txt', 'w') as f:
        f.write(str(products))

# Billing Software


def get_purchase_list():
    with open('products-for-sale.txt') as f:
        products = dict(eval(f.read()))
    items_purchased = {}
    print('--Enter \'q\' to Quit--')
    print()
    while True:
        item = input('Enter Product Purchased : ').lower()
        if item == 'quit':
            break
        elif item not in products.keys():
            print('Product not Availiable. Please Try Again.')
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

# Employee Management


def view_employee_details():
    with open('employee-details.txt') as f:
        employee_details = eval(f.read())
    name_max = 0
    for i in employee_details:
        if len(i) > name_max:
            name_max = len(i)
    print('S.NO' + '   ' + 'NAME' + ' '*name_max + 'AGE' +
          ' '*4 + 'DATE-OF-BIRTH' + ' '*4 + 'PHONE-NO')
    print('----' + '   ' + '----' + ' '*name_max + '---' +
          ' '*4 + '-------------' + ' '*4 + '--------')
    sn = 1

    for i in employee_details:
        name_space = (name_max + 4) - len(i)
        print(str(sn) + '      ' +
              employee_details[i]['name'].title() + ' '*name_space + str(employee_details[i]['age']) + ' '*5 + employee_details[i]['birth'] + ' '*7 + employee_details[i]['phone'])
        sn += 1


def add_employee():
    with open('employee-details.txt') as f:
        details = eval(f.read())

        employee_add_no = int(
            input('Enter the Number of Employees to be Added : '))
    for i in range(employee_add_no):
        name = input('Enter the Full Name of the Employee : ').lower()
        age = int(input('Enter the Age of the Employee : '))
        dob = input('Enter the Date of Birth of the Employee (DD-MM-YYYY) : ')
        phone = input('Enter the Phone Number of the Employee : ')
    details[name] = {'name': name, 'age': age, 'birth': dob, 'phone': phone}
    with open('employee-details.txt', 'w') as f:
        f.write(str(details))
    print('Employee Added!')


def remove_employee():
    with open('employee-details.txt') as f:
        details = eval(f.read())
    employee_remove_no = int(
        input('Enter the number of Employees to be Removed : '))
    n = 0
    while n < employee_remove_no:
        name = input(
            'Enter the Full Name of the Employee to be Removed : ').lower()
        if name not in details.keys():
            print('No Employee with that Name. Please check and try again.')
            continue
        else:
            del details[name]
        n += 1
    with open('employee-details.txt', 'w') as f:
        f.write(str(details))
    print('Employee Removed!')


def update_employee():
    with open('employee-details.txt') as f:
        employee_details = eval(f.read())
    employee_modification_no = int(
        input('Enter The Number of Updation to be done : '))
    n = 0
    while n < employee_modification_no:
        name = input(
            'Enter the Name of the Employee to be updated : ').lower()
        if name not in employee_details.keys():
            print(
                'The name entered does not exist in the records. Please check and try again.')
            continue
        field = int(input(
            'Enter the field option of the Employee to be updated\n1.Name 2.Age 3.Date-of-Birth 4.Phone-no :  '))
        if field == 1:
            print('Current Name :', name.title())
            new_name = input('New Name : ').lower()
            employee_details[name]['name'] = new_name
            employee_details[new_name] = employee_details[name]
            del employee_details[name]
            print('Name Updated!')
        elif field == 2:
            print('Current Age :', str(employee_details[name]['age']))
            new_age = int(input('New Age : '))
            employee_details[name]['age'] = new_age
            print('Age Updated!')
        elif field == 3:
            print('Current Date-of-Birth :', employee_details[name]['birth'])
            new_dob = input('New Date-of-Birth (DD-MM-YYYY) : ')
            employee_details[name]['birth'] = new_dob
            print('Date-of-Birth Updated!')
        elif field == 4:
            print('Current Phone-no :', employee_details[name]['phone'])
            new_phone = input('New Phone-no : ')
            employee_details[name]['phone'] = new_phone
            print('Phone-no Updated!')
        else:
            print('Invalid Option. Please try again.')
            continue
        n += 1
    with open('employee-details.txt', 'w') as f:
        f.write(str(employee_details))

# Supermarket Details Management


def view_supermarket_details():
    with open('supermarket-details.txt') as f:
        supermarket_details = eval(f.read())
    print('S.NO' + '   ' + 'NAME' + ' '*(1 + len(supermarket_details['name'])) + 'ADDRESS' + ' '*len(
        supermarket_details['address']) + 'PHONE-NO')
    print('----' + '   ' + '----' + ' ' *
          (1 + len(supermarket_details['name'])) + '-------' + ' '*len(supermarket_details['address']) + '--------')
    print('1. ' + '    ' + supermarket_details['name'].title() + ' '*((len(supermarket_details['name']) + 5) - len(
        supermarket_details['name'])) + supermarket_details['address'].title()
        + ' '*(len(supermarket_details['address']) + 7 - len(supermarket_details['address'])) + supermarket_details['phone'])


def update_supermarket_details():
    with open('supermarket-details.txt') as f:
        details = eval(f.read())
    update_no = int(input('Enter the number of Updates to be done : '))
    n = 0
    while n < update_no:
        field = int(
            input('Enter the field to be Updated\n1. Name 2. Address 3. Phone : '))
        if field == 1:
            print('Current Namme :', details['name'])
            new_name = input('New Name : ').lower()
            details['name'] = new_name
            print('Name Updated!')
        elif field == 2:
            print('Current Address :', details['address'])
            new_address = input('New Address : ').lower()
            details['address'] = new_address
            print('Address Updated!')
        elif field == 3:
            print('Current Phone-no :', details['phone'])
            new_phone = input('New Phone-no : ')
            details['phone'] = new_phone
            print('Phone-no Updated!')
        else:
            print('Invalid Option. Please try again.')
            continue
        n += 1
    with open('supermarket-details.txt', 'w') as f:
        f.write(str(details))

# Program Functions


def supermart_name():
    with open('supermarket-details.txt') as f:
        details = eval(f.read())
    print('\t     {}'.format(details['name'].upper()))
    print('\t     {}'.format('-'*len(details['name'])))
    print()


def get_user_option():
    cmd = input('Enter Option : ')
    if cmd.isdigit():
        return int(cmd)
    else:
        return cmd.strip()


def get_user_q_or_b():
    cmd = input('Enter \'q\' to quit, \'b\' to go back : ').lower()
    if cmd.strip() in ['q', 'b']:
        return cmd.strip()
    else:
        return False


def options_1():
    print('1. Billing Software\n2. Employee Management\n3. Product Managent\n4. Supermarket Management\n5. Quit')


def options_2():
    print('1. View Employee Details\n2. Update Employee Details\n3. Add Employee\n4. Remove Employee\n5. Back')


def options_3():
    print('1. View Product Details\n2. Update Product Details\n3. Add Product\n4. Remove Product\n5. Back')


def options_4():
    print('1. View Supermarket Details\n2. Update Supermarket Details\n3. Change Login Credentials\n4. Back')
