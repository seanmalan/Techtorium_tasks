contact_list = []




class Contact:
    def __init__(self, name, phone_number, email_address, company_name = ""):
      self.name = name
      self.company_name = company_name
      self.phone_number = phone_number
      self.email_address = email_address
      print(f"\n \nContact created was {self.name} {self.phone_number} {self.email_address} {self.company_name}\n \n")
        
        
    def add_contact(self):
     contact_list.append(self)
      
    def get_contact_details(self):
        for contact in contact_list:
           print(f"\n{contact.name} {contact.phone_number} {contact.email_address} {contact.company_name} \n")
           
           
    def delete_contact(self, name):
        for contact in contact_list:
            if contact.name == name:
                print(f"\n{contact.name} {contact.phone_number} {contact.email_address} {contact.company_name} ")
                delete = input("\nDo you want to delete this contact? (y/n): ")
                if delete == "y":
                    contact_list.remove(contact)
                    print(f"\nContact {contact.name} deleted\n")
                    break
                
        else:
            print("Contact not found")
            
            
    # as this function states, it gets the list of contacts and then does a loop to find all the individual contacts and matches up the name you want with a contact in the list
    def search_contact(self, name):
        for contact in contact_list:
            if contact.name == name:
                print(f"\n{contact.name} {contact.phone_number} {contact.email_address} {contact.company_name} \n")
                break
            else:
                print("Contact not found")
            
    
    # this function is supposed to update the details of a contact in the list after it has gone through to find a sepcific contact
    def update_details(self, name):
        for contact in contact_list:
            if contact.name == name:
                print(f"{contact.name} {contact.phone_number} {contact.email_address} {contact.company_name} ")
                update = input("Do you want to update this contact? (y/n): ")
                if update == "y":
                    
                    break
        else:
            print("Contact not found")
            
    
    
    #instead of having the user needing to enter all the contacts details again, this menu allows them to choose which secific detail they want to update and then replaces the existing value with the new one called new_
    def update_menu(self, name):  
        for contact in contact_list:
            if contact.name == name:
                print(f"\nWhat would you like to update about the contact {contact.name}?")
                print("1. Update name")
                print("2. Update phone number")
                print("3. Update email address")
                print("4. Update company name")
                choice = int(input("\nEnter your choice: "))
                if choice == 1:
                    new_name = input("\nEnter new name: ")
                    self.name = new_name
                    print(f"Name for {contact.name} updated successfully")
                if choice == 2:
                    new_phone_number = input("\nEnter new phone number: ")
                    self.phone_number = new_phone_number
                    print(f"\nPhone number for {contact.name} updated successfully")
                if choice == 3:
                    new_email_address = input("\nEnter new email address: ")
                    self.email_address = new_email_address
                    print(f"\nEmail address for {contact.name} updated successfully")
                if choice == 4:
                    new_company_name = input("\nEnter new company name: ")
                    self.company_name = new_company_name
                    print(f"\nCompany name {contact.name} updated successfully")
            
    
    
def menu():
    
    #this menu helps the user to see what the options are and then choose what they want to do
    print("\n1. Add a new contact")
    print("2. List all contacts")
    print("3. Search for a contact")
    print("4. Delete a Contact")
    print("5. Update a contact")
    print("9. Quit")
    choice = int(input("\nEnter your choice: "))
    return choice

def App(contact_list):
    #I have initialised a greeting variable to be False so that the greeting message only appears once
    greeted = False
    
    #because the greeting hasnt been displayed yet, the if statement will run and display the greeting message and then set the greeting variable to True so that the greeting message only appears once
    if greeted == False:
        print("\nContact Book")
        print("\nWelcome to the Welcome Book\nWhat would you like to do today?\n \n")
        greeted = True


    #the menu below is used to display the options to the user and then take in the users choice and then send the away to the relevant function which helps with the readability of the code as it looks so much cleaner and is easier to read. Once we get into seperating the functions into seperate files it will be even better.

    #this while loop is used to keep the menu running until the user decides to quit
    while True:
        choice = menu()
        #this option allows the user to quit the program
        if choice == 9:
            print("Goodbye")
            break
        
        #this option allows the user to add a new contact to the list
        if choice == 1:
            name = input("\nEnter name: ")
            phone_number = input("Enter phone number: ")
            email_address = input("Enter email address: ")
            company_name = input("Enter company name: ")
            new_contact = Contact(name, phone_number, email_address, company_name)
            new_contact.add_contact()
            
        #this option allows the user to view all the contacts in the list
        if choice == 2:
            if len(contact_list) == 0:
                print("\nNo contacts found \nAdd a contact to view \n")
            for contact in contact_list:
                print(f"{contact.name} {contact.phone_number} {contact.email_address} {contact.company_name}\n")
            
        #this option allows the user to search for a specific contact in the list
        if choice == 3:
            name = input("\nEnter the name of who you want to search: \n")
            for contact in contact_list:
                if contact.name == name:
                    contact.get_contact_details(name)
                else:
                    print("Contact not found")
            
        #this option allows the user to delete a specific contact in the list
        if choice == 4:
            name = input("Enter name: ")
            for contact in contact_list:
                if contact.name == name:
                    contact.delete_contact(name)
                    break
            else:
                print("\nContact not found")
            
        #this option allows the user to update a specific contact in the list
        if choice == 5:
            print("\nUpdate a contact")
            name = input("Enter name: ")
            for contact in contact_list:
                if contact.name == name:
                    contact.update_menu(name)
                    break
                else:
                    print("Contact not found")
            
        
                  
App(contact_list)