# contact_book.py
import os
import json
from datetime import datetime

DATA_FILE = "contacts.json"


def load_contacts():
    if not os.path.exists(DATA_FILE):
        return {}
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return {}


def save_contacts(contacts):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(contacts, f, indent=2, ensure_ascii=False)


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def display_menu():
    print("\n" + "═" * 50)
    print("          CONTACT BOOK".center(50))
    print("═" * 50)
    print("  [1]  Add New Contact")
    print("  [2]  View All Contacts")
    print("  [3]  Search Contact")
    print("  [4]  Update Contact")
    print("  [5]  Delete Contact")
    print("  [0]  Exit")
    print("═" * 50)


def add_contact(contacts):
    clear_screen()
    print("ADD NEW CONTACT\n" + "─" * 40)

    name = input("Full Name          : ").strip()
    if not name:
        print("Name is required!")
        return

    # Check if contact already exists
    if name.lower() in {k.lower(): k for k in contacts}:
        print("A contact with this name already exists!")
        return

    phone = input("Phone Number       : ").strip()
    email = input("Email (optional)   : ").strip()
    address = input("Address (optional) : ").strip()

    contacts[name] = {
        "phone": phone,
        "email": email,
        "address": address,
        "added": datetime.now().strftime("%Y-%m-%d %H:%M")
    }

    save_contacts(contacts)
    print(f"\n✓ Contact '{name}' added successfully!")


def view_contacts(contacts):
    clear_screen()
    print("ALL CONTACTS\n" + "─" * 60)

    if not contacts:
        print("No contacts saved yet.")
        return

    print(f"{'#':<3} {'Name':<25} {'Phone':<15} {'Email':<25}")
    print("─" * 60)

    for i, (name, info) in enumerate(contacts.items(), 1):
        print(f"{i:<3} {name:<25} {info['phone']:<15} {info['email']:<25}")

    print("\nTotal contacts:", len(contacts))


def search_contact(contacts):
    clear_screen()
    print("SEARCH CONTACT\n" + "─" * 40)

    if not contacts:
        print("Contact list is empty.")
        return

    query = input("Enter name or phone number to search: ").strip().lower()

    found = False
    print("\nSearch results:\n" + "─" * 60)

    for name, info in contacts.items():
        if query in name.lower() or query in info["phone"]:
            found = True
            print(f"Name    : {name}")
            print(f"Phone   : {info['phone']}")
            print(f"Email   : {info.get('email', '—')}")
            print(f"Address : {info.get('address', '—')}")
            print(f"Added   : {info.get('added', '—')}")
            print("─" * 40)

    if not found:
        print("No matching contacts found.")


def update_contact(contacts):
    clear_screen()
    print("UPDATE CONTACT\n" + "─" * 40)

    if not contacts:
        print("No contacts to update.")
        return

    name = input("Enter name of contact to update: ").strip()
    key = next((k for k in contacts if k.lower() == name.lower()), None)

    if not key:
        print("Contact not found.")
        return

    print("\nCurrent details:")
    print(f"Name    : {key}")
    print(f"Phone   : {contacts[key]['phone']}")
    print(f"Email   : {contacts[key].get('email', '—')}")
    print(f"Address : {contacts[key].get('address', '—')}")

    print("\nLeave blank to keep current value")
    new_phone = input("New Phone (or Enter to skip): ").strip()
    new_email = input("New Email (or Enter to skip): ").strip()
    new_address = input("New Address (or Enter to skip): ").strip()

    if new_phone:
        contacts[key]["phone"] = new_phone
    if new_email:
        contacts[key]["email"] = new_email
    if new_address:
        contacts[key]["address"] = new_address

    save_contacts(contacts)
    print(f"\n✓ Contact '{key}' updated successfully!")


def delete_contact(contacts):
    clear_screen()
    print("DELETE CONTACT\n" + "─" * 40)

    if not contacts:
        print("No contacts to delete.")
        return

    name = input("Enter name of contact to delete: ").strip()
    key = next((k for k in contacts if k.lower() == name.lower()), None)

    if not key:
        print("Contact not found.")
        return

    confirm = input(f"Are you sure you want to delete '{key}'? (y/n): ").lower()
    if confirm.startswith('y'):
        del contacts[key]
        save_contacts(contacts)
        print(f"\n✓ Contact '{key}' deleted.")
    else:
        print("Deletion cancelled.")


def main():
    contacts = load_contacts()

    while True:
        clear_screen()
        display_menu()

        choice = input("\nEnter your choice (0-5): ").strip()

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '0':
            clear_screen()
            print("Thank you for using Contact Book!")
            print(f"Total contacts saved: {len(contacts)}")
            break
        else:
            print("Invalid choice! Please select 0-5.")

        input("\nPress Enter to continue...")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nGoodbye! 👋")