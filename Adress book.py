import csv
import datetime

class Contact:
    def __init__(self, name, mobile_phone, company, address='', webpage='', mobile_phone_2='', 
                 mobile_phone_3='', home_phone='', office_phone='', private_email_1='', 
                 private_email_2='', office_email='', melody='', birthday='', notes='', spouse='', children=None):
        self.name = name
        self.mobile_phone = mobile_phone
        self.company = company
        self.address = address
        self.webpage = webpage
        self.mobile_phone_2 = mobile_phone_2
        self.mobile_phone_3 = mobile_phone_3
        self.home_phone = home_phone
        self.office_phone = office_phone
        self.private_email_1 = private_email_1
        self.private_email_2 = private_email_2
        self.office_email = office_email
        self.melody = melody
        self.birthday = birthday
        self.notes = notes
        self.spouse = spouse
        self.children = children or []

    def get_details(self):
        return f"Name: {self.name}\nMobile Phone: {self.mobile_phone}\nCompany: {self.company}\n" \
               f"Address: {self.address}\nWebpage: {self.webpage}\nMobile Phone 2: {self.mobile_phone_2}\n" \
               f"Mobile Phone 3: {self.mobile_phone_3}\nHome Phone: {self.home_phone}\n" \
               f"Office Phone: {self.office_phone}\nPrivate Email 1: {self.private_email_1}\n" \
               f"Private Email 2: {self.private_email_2}\nOffice Email: {self.office_email}\n" \
               f"Melody: {self.melody}\nBirthday: {self.birthday}\nNotes: {self.notes}\n" \
               f"Spouse: {self.spouse}\nChildren: {', '.join([c.name for c in self.children])}"

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                return True
        return False

    def update_contact(self, name, **kwargs):
        for contact in self.contacts:
            if contact.name == name:
                for key, value in kwargs.items():
                    setattr(contact, key, value)
                return True
        return False

    def search_contacts(self, search_term):
        matching_contacts = []
        for contact in self.contacts:
            if search_term in contact.name or search_term in contact.company:
                matching_contacts.append(contact)
        return matching_contacts

    def create_group(self, group_name):
        group = []
        setattr(self, group_name, group)
        return group

    def add_to_group(self, contact, group_name):
        getattr(self, group_name).append(contact)

    def remove_from_group(self, contact, group_name):
        getattr(self, group_name).remove(contact)

    def get_birthday_reminders(self):
        today = datetime.date.today()
        reminders = []
        for contact in self.contacts:
            if contact.birthday != '':
                bday = datetime.datetime.strptime(contact.birthday, '%Y-%m-%d').date()
                if (bday - today).days == 10:
                    reminders.append(f"{contact.name}'s birthday is coming up on {contact.birthday}!")
        return reminders

    def import_contacts(self, filename):
        with open(filename, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                contact = Contact(**row)
                self.add_contact(contact)

    def export_contacts(self, filename):
        with open(filename, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=Contact().__dict__.keys())
            writer.writeheader()
            for contact in self.contacts:
                writer.writerow(contact.__dict__)

    def print_contact_list(self):
        for contact in self.contacts:
            print(f"{contact.name}, {contact.mobile_phone}, {contact.company}")

    def print_contact_details(self, name):
        for contact in self.contacts:
            if contact.name == name:
                print(contact.get_details())
                return True
        return False




def main_menu():
    print("Contact Book Main Menu")
    print("1. Add a Contact")
    print("2. Delete a Contact")
    print("3. Update a Contact")
    print("4. Search Contacts")
    print("5. Create a Group")
    print("6. Add Contact to Group")
    print("7. Remove Contact from Group")
    print("8. Birthday Reminders")
    print("9. Import Contacts from CSV")
    print("10. Export Contacts to CSV")
    print("11. Print Contact List")
    print("12. Print Contact Details")
    print("0. Exit")

    choice = input("Enter choice (0-12): ")
    return choice







contact_book = ContactBook()

while True:
    choice = main_menu()

    if choice == "1":
        # Add a contact
        name = input("Enter name: ")
        mobile_phone = input("Enter mobile phone: ")
        company = input("Enter company: ")
        address = input("Enter address (optional): ")
        webpage = input("Enter webpage (optional): ")
        mobile_phone_2 = input("Enter mobile phone 2 (optional): ")
        mobile_phone_3 = input("Enter mobile phone 3 (optional): ")
        home_phone = input("Enter home phone (optional): ")
        office_phone = input("Enter office phone (optional): ")
        private_email_1 = input("Enter private email 1 (optional): ")
        private_email_2 = input("Enter private email 2 (optional): ")
        office_email = input("Enter office email (optional): ")
        melody = input("Enter melody (optional): ")
        birthday = input("Enter birthday (optional, format YYYY-MM-DD): ")
        notes = input("Enter notes (optional): ")
        spouse = input("Enter spouse (optional): ")
        children = input("Enter children (optional, comma-separated list): ")
        children = children.split(",") if children else []
        contact = Contact(name, mobile_phone, company, address, webpage, mobile_phone_2, mobile_phone_3,
                          home_phone, office_phone, private_email_1, private_email_2, office_email,
                          melody, birthday, notes, spouse, children)
        contact_book.add_contact(contact)
        print("Contact added successfully.")

    elif choice == "2":
        # Delete a contact
        name = input("Enter name of contact to delete: ")
        if contact_book.delete_contact(name):
            print("Contact deleted successfully.")
        else:
            print("Contact not found.")

    elif choice == "3":
        # Update a contact
        name = input("Enter name of contact to update: ")
        field = input("Enter field to update (e.g. mobile_phone): ")
        value = input(f"Enter new value for {field}: ")
        if contact_book.update_contact(name, **{field: value}):
            print("Contact updated successfully.")
        else:
            print("Contact not found.")

    elif choice == "4":
        # Search for contacts
        search_term = input("Enter search term: ")
        results = contact_book.search_contacts(search_term)
        if results:
            print("Search results:")
            for contact in results:
                print(contact.get_details())
        else:
            print("No matching contacts found.")

    elif choice == "5":
        # Create a group
        group_name = input("Enter group name: ")
        group = Group(group_name)
        contact_book.add_group(group)
        print("Group created successfully.")

    elif choice == "6":
        # Add contact to group
        name = input("Enter name of contact to add to group: ")
        group_name = input("Enter group name: ")
        if contact_book.add_contact_to_group(name, group_name):
            print("Contact added to group successfully.")
        else:
            print("Contact or group not found.")

    elif choice == "7":
        # Remove contact from group
        name = input("Enter name of contact to remove from group: ")
        group_name = input("Enter group name: ")
        if contact_book.remove_contact_from_group(name, group_name):
            print("Contact removed from group successfully.")
        else:
            print("Contact or group not found.")

    elif choice == "8":
        # View all contacts
        contacts = contact_book.get_all_contacts()
        if contacts:
            print("All contacts:")
            for contact in contacts:
                 print(contact.get_details())
        else:
            print("No contacts found.")


    elif choice == "9":
        # View all groups
        groups = contact_book.get_all_groups()
        if groups:
            print("All groups:")
            for group in groups:
               print(group.get_details())
        else:
            print("No groups found.")

    elif choice == "10":
       # View contacts in a group
       group_name = input("Enter name of group to view contacts: ")
       contacts = contact_book.get_contacts_in_group(group_name)
       if contacts:
           print(f"All contacts in {group_name} group:")
           for contact in contacts:
            print(contact.get_details())
       else:
            print("No contacts found in group.")

    elif choice == "11":
       # Quit the program
       print("Exiting program. Goodbye!")
       break

    else:
         print("Invalid choice. Please try again.")



