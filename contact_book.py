
import json
import os

FILE_NAME = "contacts.json"

# Load saved contacts
if os.path.exists(FILE_NAME):
    with open(FILE_NAME, "r") as file:
        contacts = json.load(file)
else:
    contacts = []


def save_contacts():
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)


def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }

    contacts.append(contact)
    save_contacts()
    print("Contact added successfully!")


def view_contacts():
    if not contacts:
        print("No contacts found.")
        return

    print("\n--- Contact List ---")
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. Name: {contact['name']}, Phone: {contact['phone']}")


def search_contact():
    query = input("Enter name or phone number to search: ").lower()

    found = False
    for contact in contacts:
        if (query in contact["name"].lower()
                or query in contact["phone"].lower()):
            print("\nName:", contact["name"])
            print("Phone:", contact["phone"])
            print("Email:", contact["email"])
            print("Address:", contact["address"])
            found = True

    if not found:
        print("Contact not found.")


def update_contact():
    phone = input("Enter the phone number of the contact to update: ")

    for contact in contacts:
        if contact["phone"] == phone:
            print("Leave a field blank to keep its current value.")

            name = input(f"New name [{contact['name']}]: ")
            new_phone = input(f"New phone [{contact['phone']}]: ")
            email = input(f"New email [{contact['email']}]: ")
            address = input(f"New address [{contact['address']}]: ")

            if name:
                contact["name"] = name
            if new_phone:
                contact["phone"] = new_phone
            if email:
                contact["email"] = email
            if address:
                contact["address"] = address

            save_contacts()
            print("Contact updated successfully!")
            return

    print("Contact not found.")


def delete_contact():
    phone = input("Enter the phone number of the contact to delete: ")

    for contact in contacts:
        if contact["phone"] == phone:
            contacts.remove(contact)
            save_contacts()
            print("Contact deleted successfully!")
            return

    print("Contact not found.")


while True:
    print("\n====== CONTACT BOOK ======")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        update_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        print("Thank you for using Contact Book!")
        break
    else:
        print("Invalid choice! Please try again.")
