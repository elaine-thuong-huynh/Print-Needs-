# -*- coding: utf-8 -*-
"""


@author: PC
"""
import csv
from datetime import datetime
import pandas as pd

pd.set_option('display.max_columns', 100)
pd.set_option('display.max_rows', 1000)
pd.set_option('display.max_colwidth', 1000)
pd.set_option('display.width', None)
 
### Menu option 1: Enter new data   
def enterNewData():
    with open('donation_program.csv', 'a', newline = "") as file:
        w = csv.writer(file, quoting=csv.QUOTE_ALL) 
        item = []
        ### Enter name, phone number and address
        name = input("May I know your name? ").title()
        phone_number = input("Please enter your phone number:  ")
        address = input("Please enter your address. \nIf you do not want to enter your address, enter NA: ").title()
        ### Enter item type
        while True:
            while True:
                item_index = input("""Please enter the index of item type from the list: 
1. Clothes
2. Food 
3. Electrical Appliances 
4. Books and Stationary 
5. Household Essentials 
6. Others \n""")
                if item_index == '1':
                        item_type = 'Clothes'
                        break
                elif item_index == '2':
                        item_type = 'Food'
                        break
                elif item_index == '3':
                        item_type = 'Electrical Appliances'
                        break
                elif item_index == '4':
                        item_type = 'Books and Stationary'
                        break
                elif item_index == '5':
                        item_type = 'Household Essentials'
                        break
                elif item_index == '6':
                        item_type = 'Others - ' + input('Please specify the item type you want: ')
                        break
                else:
                    print('\nAlert! Please enter a valid number from 1 to 6: ')
            ### Enter item name
            item_name  = input('Please enter name of the item you want: ').title()
            ### Enter item quantity
            while True:
                try:
                    item_quantity = int(input('Please enter quantity of the item you want: '))
                    break
                except ValueError:
                    print('\nPlease enter an integer!')
            time = datetime.now()
            exact_time = time.strftime('%d/%m/%Y %H:%M')
            item_x = [name, phone_number, address, item_type, item_name, item_quantity, exact_time]
            item.append(item_x)
            ### Ask if looking for any other items
            x = input('Are you looking for any other items? \nIf Yes, press any keys \nIf No, enter N: \n')
            if x == 'N' or x =='n':
            ### Check information before leaving    
                print('\nHere is what you entered: \n ')
                print(f'Name: {name} \nPhone Number:{phone_number} \nAddress: {address}')
                count = 0
                for i in item:
                    count +=1
                    w.writerow(i)
                    print(f'Item {count}: \nItem type: {i[3]}, Item name: {i[4]}, Item quantity: {i[5]} \n')
                break
    print('\nThank you for using our program! We will contact you as soon as possible. \nPlease press 3 to save data!')
            
### Menu option 2: Review and edit data               
def review_edit_requests():
    df = pd.read_csv('donation_program.csv')
    df = df.astype({'Phone_number': str})
    ### Review data
    name = input('May I know your name?: ').title()
    info = df[df.Name == name].loc[:, df.columns != 'Time_stamp']
    print(f'\nThe information below is what you entered: \n\n{info}')
    ### Edit data: Update info or delete info
    a = input('Do you want to edit your information? \nIf Yes, please enter Y \nIf No, please press any keys:\n')
    if a == 'Y' or a =='y':
        while True:
            b = input('Do you want to update or delete your information? \nPress 1 for update information, 2 for delete: \n')
            if b == '1':
                #### Update data
                while True:
                    e = input('Do you want to change your personal information or item quantity? \nEnter 1 for personal info \nEnter 2 for item quantity: \n')
                    if e == '1':
                        ### Update personal info
                        idx = df.index[df.Name == name]
                        name_change = input('Enter the new name: ').title()
                        phone_number_change = input('Enter the new phone number: ')
                        address_change = input('Enter the new address: ').title()
                        df.at[idx, 'Name'] = name_change
                        df.at[idx, 'Phone_number'] = phone_number_change
                        df.at[idx, 'Address'] = address_change
                        time = datetime.now()
                        time_stamp = time.strftime('%d/%m/%Y %H:%M')
                        df.at[idx, 'Time_stamp'] = time_stamp
                        df.to_csv('donation_program.csv', index = False)
                        break
                    elif e == '2':
                        ### Update item quantity
                        idx = df.index[df.Name == name].tolist()
                        while True:
                            while True:
                                try:
                                    h = int(input('Enter the index of the item (the integer in 1st column) you want to change quantity: '))
                                    break
                                except ValueError:
                                    print('\nAlert! Please enter an integer: ')
                            if h in idx:
                                while True:
                                    try:
                                        item_quantity_change = int(input('Enter the new item quantity: '))
                                        break
                                    except ValueError:
                                        print('\nAlert! Please enter an integer: ')
                                df.at[h, 'Item_quantity'] = item_quantity_change
                                time = datetime.now()
                                time_stamp = time.strftime('%d/%m/%Y %H:%M')
                                df.at[idx, 'Time_stamp'] = time_stamp
                                df.to_csv('donation_program.csv', index = False)
                                break
                            else:
                                print('\nAlert! Please enter only YOUR index item ')
                        break
                    else:
                        print('\nAlert! Please enter either 1 or 2:  ')
                break
            elif b == '2':
                ### Delete data
                idx = df.index[df.Name == name].tolist()
                while True:
                    while True:
                        try:
                            c = int(input('Enter the index of item (the integer in 1st column) you want to delete: '))
                            break
                        except ValueError:
                            print('\nAlert! Please enter an integer!')
                    if c in idx:
                        df.drop(df.index[c], inplace = True)
                        df.to_csv('donation_program.csv', index = False)
                        break
                    else:
                        print('\nAlert! Please enter only YOUR index item:  ')
                break
            else:
                print('\nAlert! Please either 1 or 2: ')
    print('\nThank you for using our program! We will contact you as soon as possible. \nPlease press 3 to save data!')
                    
                
                           
def printMenu():
    print('Welcome to the donation program!')


def processCommand():
    while True:
        cmdStr = input('''Enter command character to proceed: 
1. Enter new data 
2. Review and edit 
3. Save and Exit 
''')
        if cmdStr == "1":
            enterNewData()
            pass
        elif cmdStr == "2":
            review_edit_requests()
            pass
        elif cmdStr == "3":
            break
        else:
            print('\nAlert! Please enter a valid number from 1 to 3: ')
    return
    

def main():
    printMenu()
    processCommand()
    
    
if (__name__ == "__main__"):
    main()
    
    
    


   
    
        

        
