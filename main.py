def main():
    master_password = "admin@123"  # You can change this
    entered_password = input("Enter master password: ")

    if entered_password != master_password:
        print("Access Denied ❌")
        return

    while True:
        choice = input("Would you like to add a new password or view existing ones (add/view/exit)? ").lower()
        
        if choice == "add":
            service = input("Enter the service name: ")
            username = input("Enter the username: ")
            password = input("Enter the password: ")
            save_password(service, username, password)
            print("Password saved securely! 🔐")
        
        elif choice == "view":
            view_passwords()

        elif choice == "exit":
            break
        
        else:
            print("Invalid choice. Please enter 'add', 'view', or 'exit'.")
