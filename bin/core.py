# Import Libraries:
import os
import json
import pyperclip
import bin.crypt as cry


# Dir and File Path:
JSONS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "JSONs")
# Ensure directory exists
os.makedirs(JSONS_DIR, exist_ok=True)
PassList = os.path.join(JSONS_DIR , "pass_man.json")

def load_passwords():
    # Load existing password data from JSON file and decrypt the contents. Return empty dict if file doesn't exist.
    if os.path.exists(PassList):
        try:
            with open(PassList, 'r') as file:
                encrypted_data = json.load(file)
                decrypted_data = {}
                for website, entry in encrypted_data.items():
                    decrypted_data[website] = {
                        "username": cry.decrypt(entry["uid"]) if "uid" in entry else "",
                        "password": cry.decrypt(entry["passwd"]) if "passwd" in entry else "Not set (generate later)"
                    }
                return decrypted_data
        except Exception as e:
            print(f"Error loading password data: {str(e)}")
            return {}
    return {}

def save_passwords(passwords):
    # Save password data to JSON file after encrypting the contents.
    try:
        encrypted_data = {}
        for website, entry in passwords.items():
            encrypted_data[website] = {
                "uid": cry.encrypt(entry["username"]) if entry["username"] else "",
                "passwd": cry.encrypt(entry["password"]) if entry["password"] and entry["password"] != "Not set (generate later)" else entry["password"]
            }
        with open(PassList, 'w') as file:
            json.dump(encrypted_data, file, indent=4, sort_keys=True)
        return True
    except Exception as e:
        print(f"Error saving password data: {str(e)}")
        return False

def list_passwords():
    # List all existing password entries (masking passwords). Returns dictionary of entries.
    passwords = load_passwords()
    return passwords if passwords else {}

def search_password(website):
    # Search for a specific password entry by website name. Returns result message or details.                      
    passwords = load_passwords()
    
    if website in passwords:
        data = passwords[website]
        pyperclip.copy(data['password'])
        return [
            f"Details for {website}:",
            f"Username: {data['username']}",
            f"Password: {data['password']}",
            "Password copied to clipboard."
        ]
    return [f"No entry found for {website}."]

def delete_password(website):
    # Delete an existing password entry from the vault. Returns result message.              
    passwords = load_passwords()
    
    if website in passwords:
        del passwords[website]
        if save_passwords(passwords):
            return f"Password entry for {website} deleted successfully."
        return "Error saving changes after deletion."
    return f"No entry found for {website}."


def Add(website, username, password):
    # Add a new password entry to the vault. Returns success message or error.
    if not website or not username:
        return "Website and username cannot be empty."
    
    # Load existing passwords
    passwords = load_passwords()
    
    # Check if website already exists
    if website in passwords:
        return f"Error: An entry for {website} already exists. Use 'Edit' to modify."
    
    # Store entry with encrypted username and password (encryption happens in save_passwords)
    passwords[website] = {
        "username": username,
        "password": password if password else "Not set (generate later)"
    }
    
    # Save updated data
    if save_passwords(passwords):
        return f"Password entry for {website} added successfully."
    return "Error saving password entry."


def edit_password(website, username=None, password=None):
    # Edit an existing password entry's username or password. Returns result message.
    passwords = load_passwords()
    
    if website in passwords:
        if username is not None:
            passwords[website]["username"] = username
        if password is not None:
            passwords[website]["password"] = password
        if save_passwords(passwords):
            return f"Entry for {website} updated successfully."
        return "Error saving changes after update."
    return f"No entry found for {website}."

