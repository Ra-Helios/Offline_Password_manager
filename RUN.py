import os
from tkinter import messagebox
import customtkinter as ctk
import pyperclip
import bin.core as main
import bin.auth as auth

# Set appearance mode and theme for a modern look
ctk.set_appearance_mode("Dark")  # Options: "System", "Light", "Dark"
ctk.set_default_color_theme("green")  # Options: "blue", "dark-blue", "green"

# Class for First Login:
class FirstLoginWindow:
    
    def __init__(self):
        # Set First Login Window Specs:
        self.window = ctk.CTk()
        self.window.title("App Login Set-Up")
        self.window.geometry("400x300")
        
        # Add label
        lable = ctk.CTkLabel(master=self.window, text="Set-Up Login Password", font=("Arial", 14))
        lable.pack(pady=10)
        
        # Add entry field for created password (masked)
        self.entry = ctk.CTkEntry(master=self.window, placeholder_text="Password", show="*")
        self.entry.pack(pady=10)
        
        # Add label for password criteria below entry field
        criteria_label = ctk.CTkLabel(master=self.window, text="Criteria: \n>>> 4-12 Characters,\n>>> Only Alphanumeric Entry.", font=("Arial", 10), text_color="gray")
        criteria_label.pack(pady=5)  # Small padding to keep it close to the entry field
        
        # Add save button
        button = ctk.CTkButton(master=self.window, text="Save", command=self.set_authentication)
        button.pack(pady=10)
        
    def set_authentication(self):
        password = self.entry.get()
        flag = auth.FirstLogin(password)
        if flag:
            messagebox.showinfo("Set-Up Successful","Password Saved Successfully!")
            self.window.quit() 
            self.window.destroy()# Close the authentication window
            AppLoginWindow().run()
        else:
            messagebox.showerror("Error","Password Doesn't meet Criteria")
    
    def run(self):
        self.window.mainloop()

# Class for App Login:
class AppLoginWindow:
    
    def __init__(self):
        # Set App Login Window Specs:
        self.window = ctk.CTk()
        self.window.title("App Login")
        self.window.geometry("400x300")
        
        # Add label
        label = ctk.CTkLabel(master=self.window, text="Enter App Login Password", font=("Arial", 14))
        label.pack(pady=20)
        
        # Add entry field for password (masked)
        self.entry = ctk.CTkEntry(master=self.window, placeholder_text="Password", show="*")
        self.entry.pack(pady=10)
        
        # Add login button
        button = ctk.CTkButton(master=self.window, text="Login", command=self.check_authentication)
        button.pack(pady=10)
    
    def check_authentication(self):
        max_attempts = 3
        if not hasattr(self, 'attempts'):  # Initialize attempts if not already set
            self.attempts = 0
    
        password = self.entry.get()
        flag = auth.AppLogin(password)  
    
        if flag:
            messagebox.showinfo("Login Successful!","Login Successful, Proceeding to Home...")
            self.window.quit() 
            self.window.destroy() # Close the authentication window
            MainAppWindow().run()  # Open the main app window
        else:
            self.attempts += 1  # Increment failed attempts
            remaining = max_attempts - self.attempts
            if remaining > 0:
                # Show error message with remaining attempts
                messagebox.showwarning("Warning",f"Incorrect Password. {remaining} attempts remaining.")
            else:
                # Show final error message and close or disable further attempts
                messagebox.showerror("Error","Too many failed attempts. Access denied! Try Again Later.")
                self.window.quit()
                self.window.destroy()  # Close the window after max attempts
    
    def run(self):
        self.window.mainloop()

class MainAppWindow:
    def __init__(self):
        # Create the main app window
        self.window = ctk.CTk()
        self.window.title("Password Manager")
        self.window.geometry("800x600")
        
        # Configure grid layout for sidebar and content area
        self.window.grid_columnconfigure(0, weight=0)  # Sidebar column
        self.window.grid_columnconfigure(1, weight=1)  # Content column (expands)
        self.window.grid_rowconfigure(0, weight=1)     # Single row
        
        # Sidebar frame (left side)
        self.sidebar_frame = ctk.CTkFrame(self.window, width=150, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, sticky="nsew")
        
        # Sidebar title
        sidebar_label = ctk.CTkLabel(self.sidebar_frame, text="Menu", font=("Arial", 16, "bold"))
        sidebar_label.pack(pady=10)
        
        # Feature buttons to sidebar
        features = [
            ("List", self.show_list_passwords),
            ("Search", self.show_search_password),
            ("Add", self.show_add_password),
            ("Edit", self.show_edit_password),
            ("Delete", self.show_delete_password)
        ]
        for feature_name, command in features:
            btn = ctk.CTkButton(self.sidebar_frame, text=feature_name, command=command, corner_radius=5)
            btn.pack(pady=5, padx=10, fill="x")
        
        # Create content frame (right side)
        self.content_frame = ctk.CTkFrame(self.window, corner_radius=5)
        self.content_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        
        # Initialize current content 
        self.current_content = None
        self.show_list_passwords()  # Default view
    
    def clear_content(self):
        # Clear the current content in the content frame.
        if self.current_content is not None:
            for widget in self.content_frame.winfo_children():
                widget.destroy()
        self.current_content = None
    
    def show_add_password(self):
        # Display the Add Password feature in the content frame.
        self.clear_content()
        self.current_content = "add_password"
        
        # Title
        title = ctk.CTkLabel(self.content_frame, text="Add New Password", font=("Arial", 16, "bold"))
        title.pack(pady=10)
        
        # Input fields
        Description_label = ctk.CTkLabel(self.content_frame, text="Website/Service/Domain:")
        Description_label.pack()
        self.Description_entry = ctk.CTkEntry(self.content_frame, placeholder_text="e.g., Gmail / Steam / GitHub")
        self.Description_entry.pack(pady=5, padx=20, fill="x")
        
        uid_label = ctk.CTkLabel(self.content_frame, text="UID/Email:")
        uid_label.pack()
        self.uid_entry = ctk.CTkEntry(self.content_frame, placeholder_text="e.g., user@example.com")
        self.uid_entry.pack(pady=5, padx=20, fill="x")
        
        password_label = ctk.CTkLabel(self.content_frame, text="Password:")
        password_label.pack()
        self.password_entry = ctk.CTkEntry(self.content_frame, placeholder_text="Enter password", show="•")
        self.password_entry.pack(pady=5, padx=20, fill="x")
        
        # List button
        Add_btn = ctk.CTkButton(self.content_frame, text="Add to List", command=self.save_password)
        Add_btn.pack(pady=10)
    
    def save_password(self):
        # Save the new password entry using main.py function.
        description = self.Description_entry.get().strip()
        username = self.uid_entry.get().strip()
        password = self.password_entry.get().strip()
        result = main.Add(description, username, password)
        messagebox.showinfo("Result", result)
        # Clear fields after saving
        self.Description_entry.delete(0, "end")
        self.uid_entry.delete(0, "end")
        self.password_entry.delete(0, "end")
    
    def show_list_passwords(self):
        # Display the List Passwords feature in the content frame.
        self.clear_content()
        self.current_content = "list_passwords"
        
        # Title
        title = ctk.CTkLabel(self.content_frame, text="List All Passwords", font=("Arial", 16, "bold"))
        title.pack(pady=10)
        
        # Get list of passwords from main.py
        password_list = main.list_passwords()
        
        # For Null Password List
        if not password_list:
            null_label = ctk.CTkLabel(self.content_frame, text="The List is Empty.")
            null_label.pack(pady=10)
            return
        scroll_bar  = ctk.CTkScrollableFrame(self.content_frame, height=200, width=300)
        scroll_bar.pack(pady=10,padx=10,fill="both", expand=True)
        
        for dspt, data in password_list.items():
            # Frame for each Entry
            entry_frame = ctk.CTkFrame(scroll_bar)
            entry_frame.pack(pady=5, padx=5, fill="x")
            
            # Display Descrpition and UID
            website_label = ctk.CTkLabel(entry_frame, text=f"Domain: {dspt}", font=("Arial", 12, "bold"))
            website_label.pack(anchor="w", padx=5)
            
            username_label = ctk.CTkLabel(entry_frame, text=f"UID: {data['username']}")
            username_label.pack(anchor="w", padx=5)
            
            password_label = ctk.CTkLabel(entry_frame, text=f"Password: {'*' * len(data['password']) if data['password'] != 'Not set (generate later)' else 'Not set'}")
            password_label.pack(anchor="w", padx=5)
            
            # Buttons to copy username and password
            copy_username_btn = ctk.CTkButton(entry_frame, text="Copy UID", width=120, command=lambda u=data['username']: self.copy_to_clipboard(u, "Username"))
            copy_username_btn.pack(side="left", padx=5, pady=2)
            
            copy_password_btn = ctk.CTkButton(entry_frame, text="Copy Password", width=120, command=lambda p=data['password']: self.copy_to_clipboard(p, "Password"))
            copy_password_btn.pack(side="left", padx=5, pady=2)
    
    def show_search_password(self):
        # Display the Search Password feature in the content frame.
        self.clear_content()
        self.current_content = "search_password"
        
        # Title
        title = ctk.CTkLabel(self.content_frame, text="Search Password", font=("Arial", 16, "bold"))
        title.pack(pady=10)
        
        # Search bar
        search_label = ctk.CTkLabel(self.content_frame, text="Website/Service/Domain to Search:")
        search_label.pack()
        self.search_entry = ctk.CTkEntry(self.content_frame, placeholder_text="e.g., Gmail / Steam / GitHub")
        self.search_entry.pack(pady=5, padx=20, fill="x")
        
        # Search button
        search_btn = ctk.CTkButton(self.content_frame, text="Search", command=self.perform_search)
        search_btn.pack(pady=10)
        
        # Result display area
        self.result_frame = ctk.CTkTextbox(self.content_frame, height=150, width=300)
        self.result_frame.pack(pady=10, padx=10, fill="both", expand=True)
        self.result_frame.configure(state="disabled")
    
    def perform_search(self):
        # Perform search using main.py function and display results.
        website = self.search_entry.get().strip()
        results = main.search_password(website)
        
        # Clear the Previous search
        for widget in self.result_frame.winfo_children():
            widget.destroy()
        
        if len(results) == 1 and "No entry found" in results[0]:
            no_result_label = ctk.CTkLabel(self.result_frame, text=results[0])
            no_result_label.pack(pady=10)
        else:
            # Display search results
            for line in results[:-1]: # Excluding the last line
                label = ctk.CTkLabel(self.result_frame, text=line)
                label.pack(anchor="w", padx=5)
                
            # Copy Buttons
            password_list = main.list_passwords()
            if website in password_list:
                data = password_list[website]
                copy_uid_btn = ctk.CTkButton(self.content_frame, text="Copy UID", command=lambda u=data["username"]:self.copy_to_clipboard(u, "UID"))
                copy_uid_btn.pack(pady=5)
                copy_password_btn = ctk.CTkButton(self.content_frame, text="Copy Password", command=lambda p=data['password']: self.copy_to_clipboard(p, "Password"))
                copy_password_btn.pack(pady=5)
                clipboard_label = ctk.CTkLabel(self.content_frame, text="Password copied to clipboard.")
                clipboard_label.pack(pady=5)

    
    def copy_to_clipboard(self, text, item_type):
        # Copy the provided text to clipboard and show confirmation.
        pyperclip.copy(text)
        messagebox.showinfo("Success", f"{item_type} copied to clipboard!")
    
    def show_delete_password(self):
        # Display the Delete Password feature in the content frame.
        self.clear_content()
        self.current_content = "delete_password"
        
        # Add title
        title = ctk.CTkLabel(self.content_frame, text="Delete Password", font=("Arial", 16, "bold"))
        title.pack(pady=10)
        
        # Add delete input field
        delete_label = ctk.CTkLabel(self.content_frame, text="Website/Service/Domain to Delete:")
        delete_label.pack()
        self.delete_entry = ctk.CTkEntry(self.content_frame, placeholder_text="e.g., Gmail / Steam / Github")
        self.delete_entry.pack(pady=5, padx=20, fill="x")
        
        # Add delete button
        delete_btn = ctk.CTkButton(self.content_frame, text="Delete", command=self.perform_delete)
        delete_btn.pack(pady=10)
    
    def perform_delete(self):
        # Perform deletion using main.py function and show result.
        website = self.delete_entry.get().strip()   
        result = main.delete_password(website)
        messagebox.showinfo("Result", result)
        self.delete_entry.delete(0, "end")
    
    def show_edit_password(self):
        # Display the Edit Password feature in the content frame.
        self.clear_content()
        self.current_content = "edit_password"
        
        # Title
        title = ctk.CTkLabel(self.content_frame, text="Edit Password Entry", font=("Arial", 16, "bold"))
        title.pack(pady=10)
        
        # Input field for website to edit
        website_label = ctk.CTkLabel(self.content_frame, text="Website/Service/Domain to Edit:")
        website_label.pack()
        self.edit_website_entry = ctk.CTkEntry(self.content_frame, placeholder_text="e.g., Gmail / Steam / Github")     
        self.edit_website_entry.pack(pady=5, padx=20, fill="x")
        
        # Input fields for new username and password 
        username_label = ctk.CTkLabel(self.content_frame, text="UID/Email (leave blank to keep unchanged):")
        username_label.pack()
        self.edit_username_entry = ctk.CTkEntry(self.content_frame, placeholder_text="e.g., user@example.com")
        self.edit_username_entry.pack(pady=5, padx=20, fill="x")
        
        password_label = ctk.CTkLabel(self.content_frame, text="New Password (leave blank to keep unchanged):")
        password_label.pack()
        self.edit_password_entry = ctk.CTkEntry(self.content_frame, placeholder_text="Enter new password", show="•")
        self.edit_password_entry.pack(pady=5, padx=20, fill="x")
        
        # Update button
        update_btn = ctk.CTkButton(self.content_frame, text="Update", command=self.perform_edit)
        update_btn.pack(pady=10)
    
    def perform_edit(self):
        # Perform edit using main.py function and show result.
        website = self.edit_website_entry.get().strip()
        username = self.edit_username_entry.get().strip() or None
        password = self.edit_password_entry.get().strip() or None
        
        if not website:
            messagebox.showerror("Error", "Website name cannot be empty.")
            return
        
        result = main.edit_password(website, username, password)
        messagebox.showinfo("Result", result)
        # Clear fields after update
        self.edit_website_entry.delete(0, "end")
        self.edit_username_entry.delete(0, "end")
        self.edit_password_entry.delete(0, "end")
    
    def run(self):
        self.window.mainloop()


# Start the application with the authentication window
if __name__ == "__main__":
    if os.path.exists(auth.MasterPasswd):
        AppLoginWindow().run()
    else:
        FirstLoginWindow().run()
