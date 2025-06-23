# Import Libraries: 
import os
import hashlib
import hmac
import json

# Dir and File Path:
JSONS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "JSONs")
os.makedirs(JSONS_DIR, exist_ok=True) # If not Found , Create the Directory
MasterPasswd = os.path.join(JSONS_DIR , "app_login.json")


# To check if the Password follows the Criterias:
def Password_Validator(Pass):
    if (12 < len(Pass)) or (4 > len(Pass)):    
        return False
    elif not Pass.isalnum():
        return False
    else:
        return True

# For Setting up Password:
def FirstLogin(UserPass):
    if Password_Validator(UserPass):
        salt = os.urandom(16)
        PasswdHash = hashlib.pbkdf2_hmac('sha256' , UserPass.encode() , salt , 100000)  
        PasswdData={ "salt": salt.hex() , "hash": PasswdHash.hex() }
        with open(MasterPasswd , 'w') as file:
            json.dump(PasswdData , file)
        return True
    else:
        return False

# For Authenticating User into App:
def AppLogin(UserPass):
    with open ( MasterPasswd , 'r' ) as file:
        data = json.load(file)
    salt,stored_hash = [ bytes.fromhex(data["salt"]) , bytes.fromhex(data["hash"]) ]
    PasswdHash = hashlib.pbkdf2_hmac('sha256' , UserPass.encode()  , salt , 100000)
    if hmac.compare_digest(PasswdHash , stored_hash):
        return True
    else:
        return False