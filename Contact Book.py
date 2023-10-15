class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print("Contact added successfully.")

    def view_contacts(self):
        if self.contacts:
            for i, contact in enumerate(self.contacts, start=1):
                print(f"Contact {i}:")
                print(f"Name: {contact.name}")
                print(f"Phone: {contact.phone}")
                print(f"Email: {contact.email}")
                print(f"Address: {contact.address}")
                print("\n")
        else:
            print("No contacts in the contact book.")

    def search_contact(self, query):
        found = False
        for i, contact in enumerate(self.contacts, start=1):
            if query.lower() in contact.name.lower() or query in contact.phone:
                found = True
                print(f"Contact {i}:")
                print(f"Name: {contact.name}")
                print(f"Phone: {contact.phone}")
                print(f"Email: {contact.email}")
                print(f"Address: {contact.address}")
                print("\n")
        if not found:
            print("Contact not found.")

    def update_contact(self, query, new_contact):
        for i, contact in enumerate(self.contacts):
            if query.lower() in contact.name.lower() or query in contact.phone:
                self.contacts[i] = new_contact
                print("Contact updated successfully.")
                return
        print("Contact not found.")

    def delete_contact(self, query):
        for i, contact in enumerate(self.contacts):
            if query.lower() in contact.name.lower() or query in contact.phone:
                del self.contacts[i]
                print("Contact deleted successfully.")
                return
        print("Contact not found.")

def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Management System Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Name: ")
            phone = input("Phone: ")
            email = input("Email: ")
            address = input("Address: ")
            new_contact = Contact(name, phone, email, address)
            contact_book.add_contact(new_contact)
        elif choice == "2":
            contact_book.view_contacts()
        elif choice == "3":
            query = input("Enter a name or phone number to search: ")
            contact_book.search_contact(query)
        elif choice == "4":
            query = input("Enter the name or phone number to update: ")
            name = input("New Name: ")
            phone = input("New Phone: ")
            email = input("New Email: ")
            address = input("New Address: ")
            new_contact = Contact(name, phone, email, address)
            contact_book.update_contact(query, new_contact)
        elif choice == "5":
            query = input("Enter the name or phone number to delete: ")
            contact_book.delete_contact(query)
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
