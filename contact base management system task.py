class Contact:
    def __init__(self, name, mobile, email):
        self.name = name
        self.mobile = mobile
        self.email = email


class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self):
        name = input("Enter name: ")
        mobile = input("Enter mobile: ")
        email = input("Enter email: ")

        contact = Contact(name, mobile, email)
        self.contacts.append(contact)
        print("Contact added successfully!\n")

    def list_contacts(self):
        if not self.contacts:
            print("No contacts available.\n")
            return

        print("\nContact List:")
        for c in self.contacts:
            print(f"Name: {c.name}, Mobile: {c.mobile}, Email: {c.email}")
        print()

    def update_contact(self):
        mobile = input("Enter mobile number to update: ")

        for c in self.contacts:
            if c.mobile == mobile:
                print("Contact found! Leave blank if no change.")

                new_name = input("Enter new name: ")
                new_mobile = input("Enter new mobile: ")
                new_email = input("Enter new email: ")

                # Update only if user entered value
                if new_name:
                    c.name = new_name
                if new_mobile:
                    c.mobile = new_mobile
                if new_email:
                    c.email = new_email

                print("Contact updated successfully!\n")
                return

        print("Contact not found!\n")

    def delete_contact(self):
        mobile = input("Enter mobile number to delete: ")

        for c in self.contacts:
            if c.mobile == mobile:
                self.contacts.remove(c)
                print("Contact deleted successfully!\n")
                return

        print("Contact not found!\n")


# Main Program
cb = ContactBook()

while True:
    print("---- Contact Book Menu ----")
    print("1. Add Contact")
    print("2. Update Contact")
    print("3. List Contacts")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        cb.add_contact()
    elif choice == "2":
        cb.update_contact()
    elif choice == "3":
        cb.list_contacts()
    elif choice == "4":
        cb.delete_contact()
    elif choice == "5":
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Try again.\n")
