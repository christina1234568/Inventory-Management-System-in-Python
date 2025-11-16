# CHRISTINA_ROUSSETY, THIERRY PASCAL AZIE
# TP074367, YP075166

import datetime
def get_data(file_name):
    data = []
    try:
        with open(file_name, "r") as source_file:
            for line in source_file.readlines():
                line_list = line.strip().split(",")
                data.append(line_list)
            return data
    except:
        return data
def modify_info(file_name, target_info, new_info):
    # Read the contents of the file
    with open(file_name, 'r') as file:
        lines = file.readlines()
    # Modify the desired information in memory
    modified_lines = []
    for line in lines:
        if target_info in line:
            update = line.replace(target_info, new_info) # The in built function replace is used to repalce a tageted string
            modified_lines.append(update)  # Modify the line
        else:
            modified_lines.append(line)
    # Write the modified information back to the file
    with open(file_name, 'w') as file:
        file.writelines(modified_lines)
        print("Info modified successfully!")

def getting_available_stock():
    with open("ppe.txt", "r") as f:
        item_code = input("input item code:\n")
        for row in f.readlines():
            row_list = row.strip().split(",")
            if row_list[1] == item_code:
                print()
                print(row_list[3])
                return row_list[3]

# The name of the above function ois to read from file to get available stock of a specific item
def save_modified_file(file_name, record):
    with open(file_name, 'w') as file:
        file.writelines(record)

# Above function is use overwrite the content of named file with new updated infos
def append_data(file_name, record):
    #
    with open(file_name, "a") as dest_file:
        dest_file.write(",".join(record) + "\n")

# function to append data to a file
def add_records(file_name, record):
    with open(file_name, "a") as dest_file:
        dest_file.write(",".join(record) + "\n")

# Function to add an item to the inventory file
def enter_new_info():
    new_info = input("Enter new info:")
    return new_info
# function to get new info from user(function is used to pass variable in the modify_info function)
def get_hospital_name():
    while True:
        hospital_name = input("Enter hospital name:")
        hospital_name.upper()
        condition = hospital_name.upper().isalpha()
        length = len(hospital_name)
        while length <= 25 and condition == True:
            check_if_value_exists("hospital.txt", hospital_name, 0)
            if check_if_value_exists("hospital.txt", hospital_name, 0) == False:
                print("Hospital name has been successfully received! ")
                return hospital_name
            else:
                print("Hospital name already exist in records, verify name and re enter!")
                break

        else:
            print("Name might be too long or might contain a digit, re enter the hospital name!")
# isalpha is used to ensure that name entered by user contains only digit
#function check_if_value_exist is use to check if value inputed is already in use
def modify_hospital_Name():
    while True:
        hospital_name= input("Enter hospital name:")
        hospital_name.upper()
        condition = hospital_name.upper().isalpha()
        length = len(hospital_name)
        while length <= 25 and condition == True:
            check_if_value_exists("hospital.txt", hospital_name, 0)
            if check_if_value_exists("hospital.txt", hospital_name, 0) == True:
                print("Hospital name is in file!")
                return hospital_name
            else:
                print("Hospital name not in file, re enter hospital name!")
                break
        else:
            print("Name might be too long or might contain a digit, re enter the hospital name!")
# the check_if_value_exist is use this time to verify whether the targeted information really exist

def get_hospital_number():
    while True:
        hospital_phone_number = input("Enter phone number:")
        length = len(hospital_phone_number)
        while hospital_phone_number.isdigit() == True and length == 10:
            check_if_value_exists("hospital.txt", hospital_phone_number, 2)
            if check_if_value_exists("hospital.txt", hospital_phone_number, 2) == False:
                print("phone number recorded successfully!")
                return hospital_phone_number
            else:
                print("Phone number already in records, verify phone number and re enter!")
                break

        else:
            print("Phone number is invalid,re enter phone number !" ","
                  "ensure that input phone number has only digits and has 10 digits!")
#the in-built function isdigit() is used to check whether number inputed by user contain only digits
# it will return the boolean value True if the condition is met
def modify_hospital_number():
    while True:
        hospital_phone_number = input("Enter phone number:")
        length = len(hospital_phone_number)
        while hospital_phone_number.isdigit() == True and length == 10:
            check_if_value_exists("hospital.txt", hospital_phone_number, 2)
            if check_if_value_exists("hospital.txt", hospital_phone_number, 2) == True:
                print("phone number is in file\n")
                return hospital_phone_number
            else:
                print("phone number not found re enter phone number!\n")
                break
        else:
            print("Phone number is invalid,re enter phone number !" ","
                  "ensure that input phone number has only digits and has 10 digits!\n")

            # the isdigit() function returns True as output if all the characters in a string are digits
            # else the function returns False if letters are present in the string


def get_hospital_code():
    while True:
        hospital_code = input("Enter hospital code (four characters ):")
        length = len(hospital_code)

        while length == 4:
            check_if_value_exists("hospital.txt", hospital_code, 1)
            if check_if_value_exists("hospital.txt", hospital_code, 1) == False:
                print("Hospital code recorded successfully\n")
                return hospital_code.upper()
            else:
                print("Hospital code already in records enter another hospital code!\n")
                break

        else:
            print("hospital id is invalid,re enter the hospital code!\n")
#the hospital code must have a length of 4


def modify_hospital_code():
    hospital_code = str(input("Enter hospital code (four characters ):"))
    length = len(hospital_code)

    while length == 4:
        check_if_value_exists("hospital.txt", hospital_code, 1)
        if check_if_value_exists("hospital.txt", hospital_code, 1) == True:
            print("Hospital code recorded successfully\n")
            return hospital_code.upper()
        else:
            print("Code not found verify info and re enter!\n")
            break

    while length != 4:
        print("hospital id is invalid,re enter the hospital code!")
        hospital_code = input("Re enter hospital code:")
        length = len(hospital_code)
        if length == 4:
            check_if_value_exists("hospital.txt", hospital_code, 1)
            if check_if_value_exists("hospital.txt", hospital_code, 1) == True:
                print("Hospital code recorded successfully\n")
                return hospital_code.upper()
            else:
                print("Hospital code not in file verify your information and re enter!\n")
        else:
            continue


def add_new_hospital():
    hospital = []
    hospital_name = get_hospital_name()
    hospital_phone_number = get_hospital_number()
    hospital_code = get_hospital_code()
    add_records("hospital.txt", [hospital_name, hospital_code, hospital_phone_number])
    hospital = hospital.append([hospital_name, hospital_code, hospital_phone_number])
    print("Details have been recorded successfully!\n")
    return hospital


# all the informations are appended to the empty list hospital which is itself appended to the file "hospital.txt"
def get_supplier_name():
    while True:
        supplier_name = input("Enter supplier name:")
        supplier_name = supplier_name.upper()
        length = len(supplier_name)
        while length <= 40 and supplier_name.isalpha() == True:
            check_if_value_exists("supplier.txt", supplier_name, 0)
            if check_if_value_exists("supplier.txt", supplier_name, 0) == False:
                print("name recorded successfully!\n")
                return supplier_name
            else:
                print(" supplier name already in file please check and re enter!\n")
                break
        else:
            print("Name is too long re enter the supplier name!\n")


def modify_supplier_name():
    while True:
        supplier_name = input("Enter supplier name:")
        supplier_name = supplier_name.upper()
        length = len(supplier_name)
        while length <= 40 and supplier_name.isalpha() == True:
            check_if_value_exists("supplier.txt", supplier_name, 0)
            if check_if_value_exists("supplier.txt", supplier_name, 0) == True:
                print("name is in file!\n")
                return supplier_name
            else:
                print("Name not found, verify and re enter supplier name!\n")
                break
        else:
            print("Name is too long re enter the supplier name!\n")


def get_supplier_phone_number():
    while True:
        supplier_phone_number = input("Enter phone number:")
        length = len(supplier_phone_number)
        while supplier_phone_number.isdigit() == True and length == 10:
            check_if_value_exists("supplier.txt", supplier_phone_number, 2)
            if check_if_value_exists("supplier.txt", supplier_phone_number, 2) == False:
                print("phone number recorded successfully!\n")
                return supplier_phone_number
            else:
                print("phone number already in file, verify and re enter phone number!\n")
                break
        else:
            print("Phone number is invalid,re enter phone number !" ","
                  "ensure that input phone number has only digits and has 10 digits!\n")

            # the isdigit() function returns True as output if all the characters in a string are digits
            # else the function returns False if letters are present in the string
def modify_supplier_phone_number():
    while True:
        supplier_phone_number = input("Enter phone number:")
        length = len(supplier_phone_number)
        while supplier_phone_number.isdigit() == True and length == 10:
            check_if_value_exists("supplier.txt", supplier_phone_number, 2)
            if check_if_value_exists("supplier.txt", supplier_phone_number, 2) == True:
                print("phone number found!\n")
                return supplier_phone_number
            else:
                print("phone number not in list, verify and re enter info!\n")
                break
        else:
            print("Phone number is invalid,re enter phone number !" ","
                  "ensure that input phone number has only digits and has 10 digits!\n")

def quantity_less_than_25():
    with open("ppe.txt","r") as source_file:
        data = []
        for line in source_file:
            data = line.strip().split(",")
            if int(data[3]) < 25:
                print("Items that have values less than 25:\n")
                print(data[0],"amount", data[3],'\n')
            else:
                print("items that have values more than 25: \n")
                print(data[0], "amount",data[3],'\n')

def get_supplier_code():
    while True:
        supplier_code = str(input("Enter supplier code (four characters ):\n"))
        length = len(supplier_code)
        while length == 4:
            check_if_value_exists("supplier.txt", supplier_code, 1)
            if check_if_value_exists("supplier.txt", supplier_code, 1) == False:
                print("supplier code recorded successfully!\n")
                return supplier_code.upper()
            else:
                print("Supplier code already exist, choose another supplier code!\n")
                break

        else:
            print("invalid supplier code! Make sure supplier code has 4 characters!\n")


def modify_supplier_code():
    while True:
        supplier_code = str(input("Enter supplier code (four characters ):\n"))
        length = len(supplier_code)

        while length == 4:
            check_if_value_exists("supplier.txt", supplier_code, 1)
            if check_if_value_exists("supplier.txt", supplier_code, 1) == True:
                print("supplier code is in list")
                return supplier_code.upper()
            else:
                print("Supplier code not in list, verify and re enter supplier code!\n")
                break

        else:
            print("invalid supplier code! make sure supplier code has 4 characters!\n")


def get_supplier_email():
    while True:
        supplier_email_address = input("Enter email address of supplier:\n ")
        condition = len(supplier_email_address)
        while condition < 25:
            check_if_value_exists("supplier.txt", supplier_email_address, 3)
            if check_if_value_exists("supplier.txt", supplier_email_address, 3) == False:
                print("email recorded successfully!\n")
                return supplier_email_address
            else:
                print("email already in file! verify and re enter email!\n")
                break
        else:
            print("Email address is invalid, re enter the email address!\n")
            continue
def modify_supplier_email():
    while True:
        supplier_email_address = input("Enter email address of supplier:\n")
        condition = len(supplier_email_address)
        while condition < 25:
            check_if_value_exists("supplier.txt", supplier_email_address, 3)
            if check_if_value_exists("supplier.txt", supplier_email_address, 3) == True:
                print("email is in file !")
                return supplier_email_address
            else:
                print("Email does not exist! , verify and re enter!\n")
                break
        else:
            print("Email address is invalid, re enter the email address!\n")



def add_new_supplier():
    supplier_name = get_supplier_name()
    supplier_phone_number = get_supplier_phone_number()
    supplier_code = get_supplier_code()
    supplier_email = get_supplier_email()
    add_records("supplier.txt", [supplier_name, supplier_code, supplier_phone_number, supplier_email])
    print("details have been recorded successfully!\n")

def receiving_ppe():
    while True:
        try:
            amount = int(input("Enter quantity received in digits :"))
            break
        except:
            print("Re enter amount in digit !!!")
            amount = int(input("Enter quantity received in digits :"))
            continue
            #try and except is used to ensure that amount entered is numeric
    while amount > 0:
        while True:
            supplier_code = input("Enter Supplier code:")
            check_if_value_exists("supplier.txt", supplier_code, 1)
            if check_if_value_exists("supplier.txt", supplier_code, 1) == True:
                print("Code found !")
                break
            else:
                print("supplier code not found re enter supplier code!")
                continue
        while True:
            item_name = input("Enter item name: ")
            check_if_value_exists("ppe.txt", item_name,0)
            if check_if_value_exists("ppe.txt", item_name,0) == True:
                print("item found!")
                break
            else: print("Item not found!, re enter item name!")

        while True:
            item_code = input("Enter item code:")
            check_if_value_exists("ppe.txt", item_code, 1)
            if check_if_value_exists("ppe.txt", item_code, 1) == True:
                print("Item found!")
                current_date = datetime.datetime.now()
                transac_date = current_date.date()
                #datetime module are imported to record date of transactions
                append_data("transaction.txt",
                            [item_name, item_code, str(amount), str(supplier_code), str(transac_date)])
                # information are appended to "transaction.txt"
                print("date of transaction is:",transac_date.strftime("%y-%m-%d")) #printing date of transaction
                print("Transaction recorded successfully!\n")
                return([item_name, item_code, str(amount), str(supplier_code), str(transac_date)])

            else:
                print("Item Code not found re enter item code!\n")


def distributed_ppe():
    quantity_to_be_distributed = quantity()
    available_stock = getting_available_stock()
    # The program will check if available stock is greater that amount to be distributed before saving the transaction
    while quantity_to_be_distributed > 0:
        if quantity_to_be_distributed > int(available_stock):
            print("Amount to be distributed exceeds available stock!, Chose another amount for distribution!\n")
            break
        else:
            while True:
                hospital_code = input("Enter hospital code:")
                check_if_value_exists("hospital.txt", hospital_code, 1)
                if check_if_value_exists("hospital.txt", hospital_code, 1) == True:
                    print("Hospital code found!")
                    break
                else:
                    print("code not found re enter code!")
                continue
                # Then the program will check if the hospital to which ppe must be distributed is in the program records
        while True:
            item_name = input("Enter item name: ")
            check_if_value_exists("ppe.txt",item_name,0)
            if check_if_value_exists("ppe.txt",item_name,0) == False:
                print("item name is not in file re enter item name!\n")
                continue
            else:
                print("Item Found!")
                break
        while True:
            item_code = input("Enter item code:")
            check_if_value_exists("ppe.txt", item_code, 1)
            if check_if_value_exists("ppe.txt", item_code, 1) == True:
                print("Item found!")
                current_date = datetime.datetime.now()
                transac_date = current_date.date()
                neg_value = quantity_to_be_distributed * -1
                append_data("distribution.txt", [item_name, item_code, str(neg_value), str(hospital_code), str(transac_date)])
                append_data("transaction.txt",
                            [item_name, item_code, str(neg_value), str(hospital_code), str(transac_date)])
                print("date of transaction is:", transac_date.strftime("%y-%m-%d"))
                print("Transaction recorded successfully!\n")
                break
            else:
                print("Wrong code inputed!\n")
                continue
        break

# function to print actual inventory
def display_inventory():
    with open("ppe.txt", "r") as file:
        print("Current Inventory is\t:")
        for line in file:
            line = line.split(",")
            print("*" * 50)
            print(line[0], (line[1]), ":", line[3], "boxes")
            print("*" * 50)
            # The "ppe.txt" file is opened in read mode and the content
            # of the file at position[0], [1], [3] are printed in each line
def quantity():
    while True:
        quantity = input("Enter amount of boxes:\n")
        quantity.isnumeric()
        if quantity.isnumeric == False:
            continue

        else:
            return int(quantity)
        # use to get quantity from user
def increase_inventory():
    amount_received = quantity()
    if amount_received > 0:
        item_code = input("Enter item code:")
        check_if_value_exists("ppe.txt", item_code, 1)
        if check_if_value_exists("ppe.txt", item_code, 1) == True:
            print("Item found!")
            with open("ppe.txt", "r") as sourceFile:
                amount_in_stock = getting_available_stock()

                lines = sourceFile.readlines()
                modified_lines = []
                for line in lines:
                    if item_code in line:
                        line_number = lines.index(line)
                        new_amount = int(amount_in_stock) + int(amount_received)
                        update = lines[int(line_number)].replace(amount_in_stock, str(new_amount))
                        print(update)
                        modified_lines.append(update)
                    else:
                        modified_lines.append(line)
            save_modified_file("ppe.txt", modified_lines)
            return save_modified_file("ppe.txt", modified_lines)
        else:
            print()
            print("Item is not in inventory!, re enter item details!\n")

    else:
        print("Enter amount in digit!\n")
        # The function is use to increase the amount of ppe in the file
        #the function willa ask user amount received and will perform calculation to update quantity in stock
def decrease_inventory():
    while True:
        amount_distributed = quantity()
        available_stock = getting_available_stock()
        if amount_distributed < int(available_stock):
            item_code = input("Enter item code:")
            check_if_value_exists("ppe.txt", item_code, 1)
            if check_if_value_exists("ppe.txt", item_code, 1) == True:
                print("Item found!")
                with open("ppe.txt", "r") as sourceFile:
                    lines = sourceFile.readlines()
                    modified_lines = []
                    for line in lines:
                        if item_code in line:
                            line_number = lines.index(line)
                            new_amount = int(available_stock) - int(amount_distributed)
                            update = lines[int(line_number)].replace(available_stock, str(new_amount))
                            print(update)
                            modified_lines.append(update)
                        else:
                            modified_lines.append(line)
                save_modified_file("ppe.txt", modified_lines)
                return save_modified_file("ppe.txt", modified_lines)
            else:
                print("Item not in inventory please re enter!")
                break
        else:
            print("Wrong value inputted amount distributed cannot be greater than available stock!")
            continue
                # use to decrease amount of ppe in inventory
                #perform calculation to subtract quantity inputed by user from actual stock

def display_quantity():
    while True:
        item_code = input("Enter item code to be searched:")
        found = check_if_value_exists("ppe.txt", item_code, 1)
        if found == True:
            print()
            print("item found!")
            with open("ppe.txt", "r") as f:
                for line in f:
                    x = line.strip().split(",")
                    if (x[1]) == item_code:
                        print(x)
                        print("item Name:", x[0],"\n")
                        print("item Code:", x[1], "\n")
                        print("Amount:", x[3], "\n")

            break
        else:
            print("item code does not exist!\n")
            continue
    # The function is used to read from file and search for the line where the item code inputed by user is found
    # Then will print items in the line at specific positions
def sort_in_ascending_order():
    data = []
    with open("ppe.txt", "r") as source_file:
        for line in source_file:
            line_list = line.strip().split(",")
            data.append(line_list)
            indexing_length = int(len(data)) - 1

        sorted = False
        while not sorted:
            sorted = True
            for i in range(0, indexing_length):
                if data[i][3] > data[i + 1][3]:
                    sorted = False
                    data[i], data[i + 1] = data[i + 1], data[i]

        for item in data:
            print(item[0], "quantity: ", item[3])

            #function to sort list in ascending order,  the bumble sort algorithm is used here

def search_records_by_date(start_date, end_date, file_name):
    with open(file_name, 'r') as file:
        data = []
        for line in file:
            lineList = line.strip().split(",")
            data.append(lineList)
            for item in data:
                date_str = item[4]
            record_date = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
            if start_date <= record_date <= end_date:
                print(line.strip())
                # function to search transactions in a specific time period,
                # startdate and enddate must be inputed by user

def get_start_date():
    print("Enter startDate below(YY-MM-DD)")
    start_date = input((datetime.date))
    date = datetime.datetime.strptime(start_date, '%Y-%m-%d').date()
    return date
#function to get start date
def get_end_date():
    print("Enter EndDate below(YY-MM-DD)")
    end_date = input((datetime.date))
    date = datetime.datetime.strptime(end_date, '%Y-%m-%d').date()
    return date
#function to get end date
supplier = get_data("supplier.txt")
hospital = get_data("hospital.txt")
ppe = get_data("ppe.txt")

if supplier == []:
    file = open("supplier.txt", "a")
    #use to automatically create "supplier.txt" when the program is run for the first time
if hospital == []:
    file = open("hospital.txt", "a")
    #automatically use to create "hospital.txt" when program is run for the first time



def check_if_value_exists(file_name, value, location):
    found = False
    with open(file_name, "r") as search_file:
        for record in search_file:
            record_list = record.strip().split(",")
            if record_list[location] == value:
                found = True
                break
    return found



# function to add new user
# used at the start of the program if no user exist yet
def add_initial_user():
    print()
    print("-------------------")
    print("CREATE USER")
    print("-------------------")
    while True:
        user_id = input("Enter userID(4 digits):")
        if len(user_id) != 4:
            print("Invalid!")
            continue
        try:
            user_id = int(user_id)
            break
        except ValueError:
            print("Invalid! Please enter numbers only!")
            continue
    username = input("Enter username:")
    while True:
        password = input("Enter password(6 digits):")
        if len(password) != 6:
            print("Invalid!")
            continue
        try:
            password = int(password)
            break
        except ValueError:
            print("Invalid! Please enter numbers only!")
            continue
    usertype = "admin"
    user = [str(user_id), username, str(password), usertype]
    f = open("users.txt", "a")
    f.write(",".join(user))
    f.write("\n")
    print()
    print("New User Created!")
    f.close()
    print()
    print()

def add_new_user():
    print()
    print("-------------------")
    print("CREATE USER")
    print("-------------------")
    while True:
        user_id = input("Enter userID(4 digits):")
        if len(user_id) != 4:
            print("Invalid!")
            continue
        found = check_if_value_exists("users.txt", user_id, 0)
        if found == True:
            print("UserID is already taken!")
            continue
        try:
            user_id = int(user_id)
            break
        except ValueError:
            print("Invalid! Please enter numbers only!")
            continue
    while True:
        username = input("Enter Username:")
        found = check_if_value_exists("users.txt", username, 1)
        if found == True:
            print("Username is already taken!")
            continue
        else:
            break
    while True:
        password = input("Enter password(6 digits):")
        if len(password) != 6:
            print("Invalid!")
            continue
        found = check_if_value_exists("users.txt", password, 2)
        if found == True:
            print("Password is already taken!")
            continue
        try:
            password = int(password)
            break
        except ValueError:
            print("Invalid! Please enter numbers only!")
            continue
    usertype = "staff"

    user = [str(user_id), username, str(password), usertype]
    f = open("users.txt", "a")
    f.write(",".join(user))
    f.write("\n")
    print()
    print("New User Created!")
    f.close()
    print()
    print()


# function to create initial inventory
# used at the initial start of the program
# used before main menu as else, no data to work with available
def create_inventory():
    print("-------------------")
    print("Create Inventory")
    f = open("ppe.txt", "x")
    counter = 1
    while counter < 7:
        print("-------------------")
        print(counter)
        name = input("Enter item name:\n")
        item_code = input("Enter item code:\n")
        if len(item_code) != 2:
            print("Code entered invalid.")
            continue
        supplier_code = input("Enter supplier code:\n")
        if len(supplier_code) != 4:
            print("Supplier code entered invalid.")
            continue
        amount = 100
        with open("ppe.txt", "a") as f:
            item = [name, item_code, supplier_code, str(amount)]
            f.write(",".join(item))
            f.write("\n")
            counter = counter + 1
    f.close()

    print()
    print()


# function to search for item details
# found in main menu
# accessible by staff and admin
def item_details():
    print()
    print("----------------------------")
    print("Searching for Item Details:")
    print("----------------------------")
    while True:
        item_code = input("Enter Item Code to be searched for:")
        found = check_if_value_exists("ppe.txt", item_code, 1)
        if found == True:
            print()
            print("Item found!")
            with open("ppe.txt", "r") as f:
                for line in f:
                    x = line.strip().split(",")
                    if x[1] == item_code:
                        print(x)
                        print("PPE:", x[0])
                        print("PPE Code:", x[1])
                        print("PPE Supplier Code:", x[2])
                        print("Quantity in stock(boxes):", x[3])
            break
        else:
            print("Item does not exist!")
            continue



# function to search for supplier details
def supplier_details():
    print()
    print("--------------------------------")
    print("Searching for Supplier Details:")
    print("--------------------------------")
    while True:
        supplier_code = input("Enter Supplier Code to be searched for:")
        found = check_if_value_exists("supplier.txt", supplier_code, 1)
        if found == True:
            print()
            print("Supplier found!")
            with open("supplier.txt", "r") as f:
                for line in f:
                    x = line.strip().split(",")
                    if x[1] == supplier_code:
                        print(x)
                        print("Supplier Code:", x[1])
                        print("Supplier Name:", x[0])
                        print("Phone Number:", x[2])
                        print("Email:", x[3])
            break
        else:
            print("Supplier does not exist!")
            continue


# function for searching for hospitals details
def hospitals_details():
    print("------------------------------")
    print("Searching for Hospital Details")
    print("------------------------------")
    print()
    while True:
        hospital_code = input("Enter Hospital Code to be searched for:")
        found = check_if_value_exists("hospital.txt", hospital_code, 1)
        if found == True:
            print()
            print("Hospital found!")
            with open("hospital.txt", "r") as f:
                for line in f:
                    x = line.strip().split(",")
                    if x[1] == hospital_code:
                        print(x)
                        print("Hospital Code:", x[1])
                        print("Hospital Name:", x[0])
                        print("Phone Number:", x[2])
            break
        else:
            print("Hospital does not exist!")
            continue

# this function will enable us to check whether the supplier-code or hospital-code is recorded
# on the same line as the item_code so that it is known whether there is reception or distribution of this item

def validation_transaction(file_name, value1, location1, value2, location2):
    found = False
    with open(file_name, "r") as search_file:
        for record in search_file.readlines():
            record_list = record.strip().split(",")
            if record_list[location1] == value1 and record_list[location2] == value2:
                found = True
                break
    return found

def item_distribution():
    print("-----------------------------------")
    print("Searching Item Distributed Details")
    print("-----------------------------------")
    print()
    while True:
        total = 0
        item_code = input("Enter Item code to be searched for:")
        hospital_code = input("Enter Hospital code:")
        found = validation_transaction("distribution.txt", item_code, 1, hospital_code, 3)
        if found == True:
            with open("distribution.txt", "r") as f:
                for line in f:
                    x = line.strip().split(",")
                    if x[1] == item_code and x[3] == hospital_code:
                            print()
                            print("Distribution found!")
                            print("PPE Code:", x[1])
                            print("Hospital Code:", x[3])
                            print("Quantity distributed (boxes):", x[2])
                            print("Date distributed:", x[4])
                            total = total - int(x[2])
            break
        else:
            print("Distribution of this item does not exist!")
            transaction_menu()
    print()
    print("Total distributed for PPE", item_code, "to Hospital", hospital_code, "is:", total)



def item_received():
    print("--------------------------------")
    print("Searching Item Received Details")
    print("--------------------------------")
    print()
    while True:
        total = 0
        item_code = input("Enter Item code to be searched for:")
        supplier_code = input("Enter Supplier code:")
        found = validation_transaction("transaction.txt", item_code, 1, supplier_code, 3)
        if found == True:
            with open("transaction.txt", "r") as f:
                for line in f:
                    x = line.strip().split(",")
                    if x[1] == item_code and x[3] == supplier_code:
                        print()
                        print("Reception found!")
                        print("PPE Code:", x[1])
                        print("Supplier Code:", x[3])
                        print("Quantity Received (boxes):", x[2])
                        print("Date Received:", x[4])
                        total = total + int(x[2])
            break
        else:
            print("Reception of this item does not exist!")
            transaction_menu()
    print()
    print("Total received for PPE", item_code, "from Supplier", supplier_code, "is:", total)





def hospital_menu():
    print()
    print("-------------------------")
    print("HOSPITAL MENU")
    print("-------------------------")
    while True:
        print()
        print("1. Search for Hospitals Details")
        print("2. Modify Hospital Name")
        print("3. Modify Hospital Code")
        print("4. Modify Hospital Phone Number")
        print("5. Add New Hospital")
        print("6. MAIN MENU\n")
        sub_choice = input("Enter your choice:\n")
        if sub_choice == "1":
            hospitals_details()
        elif sub_choice == "2":
            hospital_name = modify_hospital_Name()
            new_info = enter_new_info()
            modify_info("hospital.txt", hospital_name, new_info)
        elif sub_choice == "3":
            hospital_code = modify_hospital_code()
            new_info = enter_new_info()
            modify_info("hospital.txt", hospital_code, new_info)
        elif sub_choice == "4":
            hospital_number = modify_hospital_number()
            new_info = enter_new_info()
            modify_info("hospital.txt", hospital_number, new_info)
        elif sub_choice == "5":
            add_new_hospital()
        elif sub_choice == "6":
            break
        else:
            print("Invalid!\n")
            continue
def suppliers_menu():
    print("-------------------------")
    print("SUPPLIERS MENU")
    print("-------------------------")
    while True:
        print()
        print("1. Search for Supplier Details")
        print("2. Modify Supplier Name")
        print("3. Modify Supplier Code")
        print("4. Modify Supplier Phone Number")
        print("5. Modify Supplier Email")
        print("6. Add New Supplier")
        print("7. MAIN MENU\n")
        sub_choice = input("Enter your choice:\n")
        if sub_choice == "1":
            supplier_details()
        elif sub_choice == "2":
            supplier_name = modify_supplier_name()
            new_info = enter_new_info()
            modify_info("supplier.txt", supplier_name, new_info)
        elif sub_choice == "3":
            supplier_code = modify_supplier_code()
            new_info = enter_new_info()
            modify_info("supplier.txt", supplier_code, new_info)
        elif sub_choice == "4":
            supplier_number = modify_supplier_phone_number()
            new_info = enter_new_info()
            modify_info("supplier.txt", supplier_number, new_info)
        elif sub_choice == "5":
            supplier_email = modify_supplier_email()
            new_info = enter_new_info()
            modify_info("supplier.txt", supplier_email, new_info)
        elif sub_choice == "6":
            add_new_supplier()
        elif sub_choice == "7":
            break
        else:
            print("Invalid!\n")
            continue

def item_tracking():
    print("-------------------------")
    print("INVENTORY MENU")
    print("-------------------------")
    while True:
        print()
        print("1. Display Inventory")
        print("2. Display List in Ascending Order")
        print("3. Display Quantity of a Specific Item")
        print("4. Search for Item Details")
        print("5. Search for Item With Quantity Less Than 25")
        print("6. MAIN MENU\n")
        sub_choice = input("Enter your choice here\n")
        if sub_choice == "1":
            display_inventory()
        elif sub_choice == "2":
            sort_in_ascending_order()
        elif sub_choice == "3":
            display_quantity()
        elif sub_choice == "4":
            item_details()
        elif sub_choice == "5":
            quantity_less_than_25()
        elif sub_choice == "6":
            break
        else:
            print("Invalid!\n")
            continue
def transaction_menu():
    print("-------------------------")
    print("TRANSACTION MENU")
    print("-------------------------")
    while True:
        print()
        print("1. Record Reception of PPE")
        print("2. Record Distribution of PPE")
        print("3. Increase Amount of PPE in Stock")
        print("4. Decrease Amount of PPE in Stock")
        print("5. Search Transactions by Time Period")
        print("6. Search for Item Distributed Details")
        print("7. Search for Item Received Details")
        print("8. MAIN MENU\n")
        sub_choice = input("Enter your choice:\n")
        if sub_choice == "1":
            receiving_ppe()
        elif sub_choice == "2":
            distributed_ppe()
        elif sub_choice == "3":
            increase_inventory()
        elif sub_choice == "4":
            decrease_inventory()
        elif sub_choice == "5":
            search_records_by_date(get_start_date(), get_end_date(), 'transaction.txt')
        elif sub_choice == "6":
            item_distribution()
        elif sub_choice == "7":
            item_received()
        elif sub_choice == "8":
            break
        else:
            print("Invalid!\n")
            continue


# the general main menu can be accessed both by admin and staff
def main_menu():
    print()
    print("---------------")
    print("MAIN MENU")
    print("---------------")
    while True:
        print()
        print("1. Transactions Menu")
        print("2. Hospital Menu")
        print("3. Supplier Menu ")
        print("4. Inventory Menu ")
        print("5. EXIT\n")
        choice = input("Enter your choice:\n")
        if choice == "1":
            transaction_menu()
            continue
        elif choice == "2":
            hospital_menu()
            continue
        elif choice == "3":
            suppliers_menu()
        elif choice == "4":
            item_tracking()
        elif choice == "5":
            print("Closing PPE Inventory Management")
            break
        else:
            print("Invalid option!")
            continue

def save_file(file_name, data):
    with open(file_name, "w") as f:
        for item in data:
            f.write(",".join(item))

def modify_user_id():
    print()
    while True:
        user_id = input("Enter userID to be modified:")
        found = check_if_value_exists("users.txt", user_id, 0)
        if found == True:
            break
        elif found == False:
            print("UserID does not exist!")
            continue
    while True:
        new_user_id = input("Enter new userID:")
        if len(new_user_id) != 4:
            print("Invalid! Please enter 4 digits!")
            continue
        found = check_if_value_exists("users.txt", new_user_id, 0)
        if found == True:
            print("UserID is already taken!")
            continue
        try:
            new_user_id = int(new_user_id)
            break
        except ValueError:
            print("Invalid! Please enter numbers only!")
            continue
    new_file = []
    with open("users.txt", "r") as f:
        for line in f:
            x = line.split(",")
            if x[0] == user_id:
                x[0] = str(new_user_id)
                print("UserID changed!")
                print(x)
                new_file.append(x)
            elif user_id != x[0]:
                new_file.append(x)
    save_file("users.txt", new_file)

def modify_username():
    print()
    while True:
        user_id = input("Enter userID to be modified:")
        found = check_if_value_exists("users.txt", user_id, 0)
        if found == True:
            break
        elif found == False:
            print("UserID does not exist!")
            continue
    while True:
        new_username = input("Enter new Username:")
        found = check_if_value_exists("users.txt", new_username, 1)
        if found == True:
            print("Username is already taken!")
            continue
        else:
            break
    new_file = []
    with open("users.txt", "r") as f:
        for line in f:
            x = line.split(",")
            if x[0] == user_id:
                x[1] = new_username
                print("Username changed!")
                print(x)
                new_file.append(x)
            elif user_id != x[0]:
                new_file.append(x)
    save_file("users.txt", new_file)

def modify_password():
    print()
    while True:
        user_id = input("Enter userID to be modified:")
        found = check_if_value_exists("users.txt", user_id, 0)
        if found == True:
            break
        elif found == False:
            print("UserID does not exist!")
            continue
    while True:
        new_password = input("Enter new Password:")
        if len(new_password) != 6:
            print("Invalid!")
            continue
        found = check_if_value_exists("users.txt", new_password, 2)
        if found == True:
            print("Password is already taken!")
            continue
        try:
            new_password = int(new_password)
            break
        except ValueError:
            print("Invalid! Please enter numbers only!")
            continue
    new_file = []
    with open("users.txt", "r") as f:
        for line in f:
            x = line.split(",")
            if x[0] == user_id:
                x[2] = str(new_password)
                print("Password changed!")
                print(x)
                new_file.append(x)
            elif user_id != x[0]:
                new_file.append(x)
    save_file("users.txt", new_file)

# function to modify existing user
def modify_user():
    print()
    print("----------------------")
    print("Modifying User Details")
    print("----------------------")
    print("1. Modify UserID")
    print("2. Modify Username")
    print("3. Modify Password")
    print()
    choice = int(input("Enter option:"))
    if choice == 1:
        modify_user_id()
    elif choice == 2:
        modify_username()
    elif choice == 3:
        modify_password()
    else:
        print("Invalid option!")

# function for searching user in admin menu
def search_user():
    print()
    print("---------------")
    print("Searching User")
    print("---------------")
    while True:
        user_id = input("Enter userID to be searched:")
        found = check_if_value_exists("users.txt", user_id, 0)
        if found == True:
            print()
            print("User found!")
            with open("users.txt", "r") as f:
                for line in f:
                    x = line.strip().split(",")
                    if int(x[0]) == int(user_id):
                        print(x)
                        print("UserID:", x[0])
                        print("Username:", x[1])
                        print("Password:", x[2])
                        print("User type:", x[3])
            break
        else:
            print("UserID does not exist!")
            continue

# function for deleting user in admin menu
def delete_user():
    print()
    print("--------------")
    print("Deleting User")
    print("--------------")
    while True:
        user_id = input("Enter userID to be deleted:")
        found = check_if_value_exists("users.txt", user_id, 0)
        if found == True:
            new_file= []
            with open("users.txt", "r") as f:
                for line in f:
                    x = line.split(",")
                    if user_id == x[0]:
                        print()
                        print("User deleted!")
                    elif user_id != x[0]:
                        new_file.append(x)
                save_file("users.txt", new_file)
            break
        else:
            print("UserID does note exist!")
            continue
    # saveFile function is called to save new_inventory
    # thus, deleting the user with the userID entered

# this menu will be accessed only by admin
def menu_admin():
    print()
    print("-----------")
    print("ADMIN MENU")
    print("-----------")
    print("User Management")
    print()
    while True:
        print()
        print("1. Add new user")
        print("2. Modify existing user details")
        print("3. Search user")
        print("4. Delete user")
        print("5. Main Menu")
        print("6. EXIT")
        print()
        choice = int(input("Enter function option:"))
        if choice == 1:
            add_new_user()
            continue
        elif choice == 2:
            modify_user()
            continue
        elif choice == 3:
            search_user()
            continue
        elif choice == 4:
            delete_user()
            continue
        elif choice == 5:
            main_menu()
            continue
        elif choice == 6:
            print("Closing PPE Inventory Management")
            break
        else:
            print("Invalid option")
            continue

def validation_login():
      while True:
        print()
        user_id = input("Enter userID:")
        password = input("Enter password:")
        with open("users.txt", "r") as f:
            for row in f.readlines():
                row_list = row.strip().split(",")
                if row_list[0] == user_id and row_list[2] == password:
                    print()
                    print("Validated!")
                    return row_list[3]

        print("Invalid!")
        continue


# function for login
# used after creation of first user and creation of initial inventory
def login():
    print()
    print("------------------------------------")
    print("Welcome to PPE Inventory Management")
    print("------------------------------------")
    print("LOGIN")
    print()
    user_type = validation_login()
    if user_type == "admin":
        menu_admin()
    else:
        main_menu()

# if read function of users.txt file gives an error, file does not exist yet
# add_new_user function will be used
try:
    f = open("users.txt", "r")
    f.close()
except:
    add_initial_user()

print()
# if read file function gives an error, then create_inventory function will be used
# creating initial inventory
try:
    f = open("ppe.txt", "r")
    f.close()
except:
    print("NO INVENTORY!")
    create_inventory()

login()
