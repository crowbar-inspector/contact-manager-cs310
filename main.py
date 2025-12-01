import datetime

import contact


def main():
    contacts = contact.load_contacts()
    fname_tree, lname_tree, phone_tree = contact.build_indexes(contacts)

    while True:
        contact.print_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            contact.list_contacts(contacts, 20)
        elif choice == "2":
            contact.add_contact(contacts, fname_tree, lname_tree, phone_tree)
        elif choice == "3":
            contact.delete_contact(contacts, fname_tree, lname_tree, phone_tree)
        elif choice == "4":
            contact.sort_contacts(contacts)
        elif choice == "5":
            contact.search_contacts(fname_tree, lname_tree, phone_tree, contacts)
        elif choice == "6":
            contact.save_contacts(contacts)
            print("Goodbye.")
            break
        else:
            print("Invalid choice.")




if __name__ == "__main__":
    main()
