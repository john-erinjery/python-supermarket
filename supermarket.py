# Python program of a Supermarket software

import definitions
definitions.supermart_name()
n = 0
logged_in = True
while n < 3:
    if definitions.login():
        logged_in = True
        print('Log in Successful!')
        break
    else:
        print('--Wrong Username or Password.')
        if n != 2 and n != 1:
            print('--The program will terminate after',
                  str(2-n), 'more attempts.')
        elif n == 1:
            print('--The Program will terminate after 1 more attempt.')
        n += 1
if logged_in:
    print()
    definitions.supermart_name()
    while True:
        definitions.options_1()
        n = False
        while n == False:
            optn = definitions.get_user_option()
            if optn in [1, 2, 3, 4, 5]:
                n = True
            else:
                print('Invalid Input.')
        if optn == 1:
            definitions.bill(definitions.get_purchase_list())
            cmd = False
            n = 0
            while cmd == False:
                if n != 0:
                    print('Invalid Input')
                cmd = definitions.get_user_q_or_b()
                n += 1
            if cmd == 'q':
                break
            else:
                continue
        elif optn == 2:
            definitions.options_2()
            n = False
            while n == False:
                optn_2 = definitions.get_user_option()
                if optn_2 in [1, 2, 3, 4, 5]:
                    n = True
                else:
                    print('Invalid Input.')
            if optn_2 == 1:
                definitions.view_employee_details()
                cmd = False
                n = 0
                while cmd == False:
                    if n != 0:
                        print('Invalid Input')
                    cmd = definitions.get_user_q_or_b()
                    n += 1
                if cmd == 'q':
                    break
                else:
                    continue
            elif optn_2 == 2:
                definitions.update_employee()
                cmd = False
                n = 0
                while cmd == False:
                    if n != 0:
                        print('Invalid Input')
                    cmd = definitions.get_user_q_or_b()
                    n += 1
                if cmd == 'q':
                    break
                else:
                    continue
            elif optn_2 == 3:
                definitions.add_employee()
                cmd = False
                n = 0
                while cmd == False:
                    if n != 0:
                        print('Invalid Input')
                    cmd = definitions.get_user_q_or_b()
                    n += 1
                if cmd == 'q':
                    break
                else:
                    continue
            elif optn_2 == 4:
                definitions.remove_employee()
                cmd = False
                n = 0
                while cmd == False:
                    if n != 0:
                        print('Invalid Input')
                    cmd = definitions.get_user_q_or_b()
                    n += 1
                if cmd == 'q':
                    break
                else:
                    continue
            elif optn_2 == 5:
                continue
            else:
                print('Invalid Command')
                continue
        elif optn == 3:
            definitions.options_3()
            n = False
            while n == False:
                optn_2 = definitions.get_user_option()
                if optn_2 in [1, 2, 3, 4, 5]:
                    n = True
                else:
                    print('Invalid Input.')
            if optn_2 == 1:
                definitions.view_product_details()
                cmd = False
                n = 0
                while cmd == False:
                    if n != 0:
                        print('Invalid Input')
                    cmd = definitions.get_user_q_or_b()
                    n += 1
                if cmd == 'q':
                    break
                else:
                    continue
            elif optn_2 == 2:
                definitions.update_products()
                cmd = False
                n = 0
                while cmd == False:
                    if n != 0:
                        print('Invalid Input')
                    cmd = definitions.get_user_q_or_b()
                    n += 1
                if cmd == 'q':
                    break
                else:
                    continue
            elif optn_2 == 3:
                definitions.add_products()
                cmd = False
                n = 0
                while cmd == False:
                    if n != 0:
                        print('Invalid Input')
                    cmd = definitions.get_user_q_or_b()
                    n += 1
                if cmd == 'q':
                    break
                else:
                    continue
            elif optn_2 == 4:
                definitions.remove_products()
                cmd = False
                n = 0
                while cmd == False:
                    if n != 0:
                        print('Invalid Input')
                    cmd = definitions.get_user_q_or_b()
                    n += 1
                if cmd == 'q':
                    break
                else:
                    continue
            elif optn_2 == 5:
                continue
        elif optn == 4:
            definitions.options_4()
            n = False
            while n == False:
                optn_2 = definitions.get_user_option()
                if optn_2 in [1, 2, 3, 4]:
                    n = True
                else:
                    print('Invalid Input.')
            if optn_2 == 1:
                definitions.view_supermarket_details()
                cmd = False
                n = 0
                while cmd == False:
                    if n != 0:
                        print('Invalid Input')
                    cmd = definitions.get_user_q_or_b()
                    n += 1
                if cmd == 'q':
                    break
                else:
                    continue
            elif optn_2 == 2:
                definitions.update_supermarket_details()
                cmd = False
                n = 0
                while cmd == False:
                    if n != 0:
                        print('Invalid Input')
                    cmd = definitions.get_user_q_or_b()
                    n += 1
                if cmd == 'q':
                    break
                else:
                    continue
            elif optn_2 == 3:
                s = False
                definitions.change_credentials()
                cmd = False
                n = 0
                while cmd == False:
                    if n != 0:
                        print('Invalid Input')
                    cmd = definitions.get_user_q_or_b()
                    n += 1
                if cmd == 'q':
                    break
                else:
                    continue
            else:
                continue
        elif optn == 5:
            break
