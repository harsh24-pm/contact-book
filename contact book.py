contacts = []

def add_contact():
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()
    
    contact = {"name": name, "phone": phone, "email": email}
    contacts.append(contact)
    print(f"\n✅ Contact '{name}' added successfully!\n")

def view_contacts():
    if not contacts:
        print("\n📭 No contacts found.\n")
        return
    
    print("\n" + "=" * 40)
    print("ALL CONTACTS")
    print("=" * 40)
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. Name: {contact['name']}")
        print(f"   Phone: {contact['phone']}")
        print(f"   Email: {contact['email']}")
        print("-" * 40)
    print()

def search_contact():
    if not contacts:
        print("\n📭 No contacts found.\n")
        return
    
    query = input("Enter name to search: ").strip().lower()
    results = [c for c in contacts if query in c["name"].lower()]
    
    if results:
        print(f"\n🔍 Found {len(results)} result(s):")
        for contact in results:
            print(f"   Name: {contact['name']}")
            print(f"   Phone: {contact['phone']}")
            print(f"   Email: {contact['email']}")
            print("-" * 40)
    else:
        print("\n❌ No contact found with that name.\n")

def delete_contact():
    if not contacts:
        print("\n📭 No contacts found.\n")
        return
    
    name = input("Enter name to delete: ").strip().lower()
    for contact in contacts:
        if contact["name"].lower() == name:
            contacts.remove(contact)
            print(f"\n🗑️ Contact '{contact['name']}' deleted successfully!\n")
            return
    
    print("\n❌ Contact not found.\n")

def show_menu():
    print("=" * 40)
    print("        CONTACT BOOK MENU")
    print("=" * 40)
    print("1. Add new contact")
    print("2. View all contacts")
    print("3. Search contact by name")
    print("4. Delete contact")
    print("5. Exit")
    print("=" * 40)

def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ").strip()
        print()
        
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please enter a number between 1-5.\n")

if __name__ == "__main__":
    main()