print("Stellar Events' vendor contact manager 3000")
 
vendor_ID = 1
 
contact_list = []
 
class Vendor:
   
    def __init__(self, name, number, email, id):
        self.name = name
        self.number = number
        self.email = email
        self.id = id
 
    def details(self):
      print ("Vendor name:\t {}".format(self.name))
      print ("Phone number:\t {}".format(self.number))
      print ("Email address:\t {}".format(self.email))
      print ("Vendor ID:\t {}".format(self.id))
 
    def update_details(self):
       print("\nWhich details need updating?")
       print("[1]: Vendor name")
       print("[2]: Phone number")
       print("[3]: Email adress")
       print("[9]: GO BACK")
       update_menu = input (">: ")
 
       if update_menu == "1":
          self.name = input("Input new name: ").lower()
          print("\nVendor name has been updated")
          print("New name is: {}".format(self.name))
       elif update_menu == "2":
          self.number = input("Input new phone number: ").lower()
          print("\nPhone number has been updated")
          print("New phone number is: {}".format(self.number))
       elif update_menu == "3":
          self.email = input("Input new email adress: ").lower()
          print("\nEmail has been updated")
          print("New email is: {}".format(self.email))
       elif update_menu == "9":
          menu()
       else:
          print("Sorry, input invalid.")
          print("Please try again!")
          menu()
     
def menu():
  print("\n'Menu: ")
  print("\t[1]: View contact list")
  print("\t[2]: Add a vendor")
  print("\t[3]: Search [vendor name]")
  print("\t[4]: Search [vendor ID]")
  print("\t[5]: Update a vendor's information")
  print("\t[6]: Remove a vendor")
  #print("\t[7]: Save data to file")
  #print("\t[8]: Print data from file")
  print("\t[9]: Exit")
  option_menu()
 
def option_menu():
  choose_option = input("\n[Choose option]: ")
  print("")
  if choose_option == "1":
    view_contacts()
    menu()
  elif choose_option == "2":
    add_vendor()
  elif choose_option == "3":
    search_vendor()
  elif choose_option == "4":
    search_vendor_id()
  elif choose_option == "5":
    update_vendor_fun()
  elif choose_option == "6":
    remove_vendor_fun()
  elif choose_option == "9":
    print("Ka kite anō!")
    exit()
  else:
    print("Invalid input, please try again!")
    option_menu()  
 
    menu()
   
def view_contacts():
  if len(contact_list) == 0:
    print("Sorry, there are no contacts in your contact list!")
  else:
    for contact in contact_list:
      print("[Company]:", contact.name.title(), "[Number]:", contact.number, "[Email]:", contact.email, "[ID]:", contact.id)
 
def add_vendor():
   global vendor_ID
   new_v_name = input("Input vendor name: ").lower()
   new_v_phone = input("Input vendor phone number: ").lower()
   new_v_email = input("Input vendor email: ").lower()
   new_v_ID = vendor_ID
   new_vendor = Vendor(new_v_name, new_v_phone, new_v_email, new_v_ID)
   contact_list.append(new_vendor)
 
   print("New vendor has been added to contact list:")
   new_vendor.details()
   vendor_ID += 1
   menu()
 
def update_vendor_fun():
  print("[x]: MENU")
  searched_vendor_n = input("Enter the name of vendor: ")
 
  if searched_vendor_n == "x":
    menu()
 
  for contact in contact_list:
    if contact.name == searched_vendor_n:
      contact.update_details()
      menu()
    else:
      print("Cannot find contact, please try again!")
      update_vendor_fun()
 
def search_vendor():
   print("\n[x]: MENU")
   searched_vendor_n = input("Enter the name of vendor: ")
 
   if searched_vendor_n == "x":
     menu()
 
   for contact in contact_list:
    if contact.name == searched_vendor_n:
      print ("[Company]:", contact.name.title(), "[Number]:", contact.number, "[Email]:", contact.email, "[ID]:", contact.id)
      menu()
    
 
def search_vendor_id():
   print("\n[x]: MENU")
   searched_vendor_id = input("Enter the ID of vendor: ").lower()
 
   if searched_vendor_id == "x":
     menu()
 
   for contact in contact_list:
     if contact.id == int(searched_vendor_id):
      print ("[Company]:", contact.name.title(), "[Number]:", contact.number, "[Email]:", contact.email, "[ID]:", contact.id)
      menu()
     
 
def remove_vendor_fun():
  print("[x]: MENU")
  searched_vendor_n = input("Enter the name of vendor: ")
 
  if searched_vendor_n == "x":
    menu()
 
  for contact in contact_list:
    if contact.name == searched_vendor_n:
      print ("Are you sure you want to delete this Vendor? ({})".format(contact.name))
      remove_option = input ("[y/n] >: ")
 
      if remove_option.lower().startswith("y"):
        contact_list.remove(contact)
        print("Vendor has been deleted.")
        menu()
      else:
         print("{} was not deleted".format(contact.name))
         menu()
    else:
      print("Cannot find contact, please try again!")
      update_vendor_fun()
 
menu()