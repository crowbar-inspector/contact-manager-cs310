import datetime
import csv
from dataclasses import dataclass

@dataclass
class Contact:
    first_name: str
    last_name: str
    phone: str
    date_added: datetime.date

def mergesort(arr, key=lambda x: x):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = mergesort(arr[:mid], key)
    right = mergesort(arr[mid:], key)

    return merge(left, right, key)

def merge(left, right, key):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if key(left[i]) <= key(right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

class TreeNode:
    def __init__(self, contact, key_func):
        self.contact = contact
        self.key = key_func(contact)
        self.left = None
        self.right = None

class ContactBST:
    def __init__(self, key_func):
        self.root = None
        self.key_func = key_func

    def insert(self, contact):
        if self.root is None:
            self.root = TreeNode(contact, self.key_func)
        else:
            self._insert(self.root, contact)

    def _insert(self, node, contact):
        k = self.key_func(contact)
        if k < node.key:
            if node.left is None:
                node.left = TreeNode(contact, self.key_func)
            else:
                self._insert(node.left, contact)
        else:
            if node.right is None:
                node.right = TreeNode(contact, self.key_func)
            else:
                self._insert(node.right, contact)

    def search(self, key_value):
        return self._search(self.root, key_value)

    def _search(self, node, key_value):
        if node is None:
            return None

        if key_value == node.key:
            return node.contact
        elif key_value < node.key:
            return self._search(node.left, key_value)
        else:
            return self._search(node.right, key_value)

def load_contacts(path="data.csv"):
    contacts = []
    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            fname = row["first_name"]
            lname = row["last_name"]
            phone = row["phone"]
            date_added = datetime.datetime.strptime(row["date"], "%Y/%m/%d")
            contacts.append(Contact(fname, lname, phone, date_added))

    return contacts

def build_indexes(contacts):
    fname_tree = ContactBST(key_func=lambda c: c.first_name)
    lname_tree = ContactBST(key_func=lambda c: c.last_name)
    phone_tree = ContactBST(key_func=lambda c: c.phone)
    for c in contacts:
        fname_tree.insert(c)
        lname_tree.insert(c)
        phone_tree.insert(c)
    return fname_tree, lname_tree, phone_tree

def print_menu():
    print("\nContact Manager")
    print("1. List contacts")
    print("2. Add contact")
    print("3. Delete contact")
    print("4. Sort contacts")
    print("5. Search contact")
    print("6. Exit")

def list_contacts(contacts, limit):
    print(f"\nShowing up to {limit} contacts:")
    if limit is not None:
        for c in contacts[:limit]:
            print(f"{c.first_name:20} {c.last_name:20} {c.phone:12} {c.date_added.isoformat()}")
    else:
        for c in contacts:
            print(f"{c.first_name:20} {c.last_name:20} {c.phone:12}")

def is_valid_phone(phone):
    return phone.isdigit() and len(phone) == 10

def add_contact(contacts, fname_tree, lname_tree, phone_tree):
    fname = input("First Name: ").strip()
    lname = input("Last Name: ").strip()
    phone = input("Phone (10 digits): ").strip()

    if not is_valid_phone(phone):
        print("Error: Invalid phone number")
        return

    c = Contact(fname, lname, phone, datetime.datetime.now())
    contacts.append(c)
    fname_tree.insert(c)
    lname_tree.insert(c)
    phone_tree.insert(c)
    print("Contact added: " + fname + " " + lname + ", " + phone + ", " + datetime.datetime.now().isoformat())

def delete_contact(contacts, fname_tree, lname_tree, phone_tree):
    phone = input("Enter # of contact to delete: ").strip()
    for i, c in enumerate(contacts):
        if c.phone == phone:
            contacts.pop(i)
            print("Contact deleted from list.")
            fname_tree, lname_tree, phone_tree = build_indexes(contacts)
            return
    print("Contact not found.")

def sort_contacts(contacts):
    print("Sort by: 1) first name 2) last name 3) phone  4) date added")
    option = input("Choice: ").strip()

    if option == "1":
        contacts[:] = mergesort(contacts, key=lambda c: c.first_name)
    elif option == "2":
        contacts[:] = mergesort(contacts, key=lambda c: c.last_name)
    elif option == "3":
        contacts[:] = mergesort(contacts, key=lambda c: c.phone)
    elif option == "4":
        contacts[:] = mergesort(contacts, key=lambda c: c.date_added)
    else:
        print("Invalid option.")
        return

    print("Contacts sorted.")

def search_contacts(fname_tree, lname_tree, phone_tree, contacts):
    print("Search by: 1) first name 2) last name 3) phone")
    option = input("Choice: ").strip()

    if option == "1":
        query = input("Enter first name: ").strip().lower()

        matches = [
            c for c in contacts
            if query in c.first_name.lower()
        ]

    elif option == "3":
        query = input("Enter last name: ").strip().lower()
        matches = [
            c for c in contacts
            if query in c.last_name.lower()
        ]

    elif option == "3":
        query = input("Enter #: ").strip()

        matches = [
            c for c in contacts
            if c.phone.startswith(query)
        ]

    else:
        print("Invalid option.")
        return

    if not matches:
        print("No matching contacts found.")
        return

    print(f"\nMatches found ({len(matches)}):\n")
    for c in matches:
        print(f"{c.first_name:20} | {c.last_name:20} | {c.phone} | {c.date_added}")

def save_contacts(contacts, path="data.csv"):
    import csv
    with open(path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["first_name", "last_name", "phone", "date"])
        for c in contacts:
            writer.writerow([c.first_name, c.last_name, c.phone, c.date_added.isoformat()])





