def display_menu():
    print("Shopping List Manager")
    print("1. Add item")
    print("2. Remove item")
    print("3. View list")
    print("4. Exit")

def main():
    shopping_list = []
    
    while True:
        display_menu()
        
        choice = input("Please choose an option (1-4): ").strip()
        
        if choice == '1':
            item = input("Enter the item to add: ").strip()
            if item:
                shopping_list.append(item)
                print(f"'{item}' has been added to the shopping list.")
            else:
                print("Item name cannot be empty.")
        
        elif choice == '2':
            if not shopping_list:
                print("The shopping list is empty. Nothing to remove.")
            else:
                print("Current shopping list:", shopping_list)
                item = input("Enter the item to remove: ").strip()
                if item in shopping_list:
                    shopping_list.remove(item)
                    print(f"'{item}' has been removed from the shopping list.")
                else:
                    print(f"'{item}' was not found in the shopping list.")
        
        elif choice == '3':
            if not shopping_list:
                print("The shopping list is empty.")
            else:
                print("\n--- Current Shopping List ---")
                for i, item in enumerate(shopping_list, 1):
                    print(f"{i}. {item}")
        
        elif choice == '4':
            print("Thank you for using the Shopping List. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
