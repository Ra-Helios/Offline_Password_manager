
C_def= [("a","l") , ("b","U") , ("c","L") , ("d","c") , ("e","O") , ("f","C") , ("g","T") , ("h","u") , ("i","t") , ("j","l.") , ("k","U.") , ("l","L.") , ("m","c.") , ("n","O.") , ("o","C.") , ("p","T.") , ("q","u.") , ("r","t.") , ("s","V") , ("t",">") , ("u","v") , ("v","<") , ("w","V.") , ("x",">.") , ("y","v.") , ("z","<.") , (" ","Z") , (".","X") , (">","rt") , ("<","ef") , ("A","Yl") , ("B","YU") , ("C","YL") , ("D","Yc") , ("E","YO") , ("F","YC") , ("G","YT") , ("H","Yu") , ("I","Yt") , ("J","Yl.") , ("K","YU.") , ("L","YL.") , ("M","Yc.") , ("N","YO.") , ("O","YC.") ,("P","YT.") ,  ("Q","Yu.") , ("R","Yt.") , ("S","YV") , ("T","Y>") , ("U","Yv") , ("V","Y<") , ("X","Y>.") , ("Y","Yv.") , ("Z","Y<.") , ("0","3") , ("1","4") , ("2","5") , ("3","6") , ("4","7") , ("5","8") , ("6","9") , ("7","0") , ("8","1") , ("9","2") ] 

def encrypt(text):
    encrypted_text = ""
    for char in text:
        flag=False
        for tup in C_def:
            while tup[0]==char: 
                encrypted_text+=tup[1]
                flag=True
                break
        if not flag:
            encrypted_text+=char 
    return encrypted_text

def decrypt(text):
    decrypted_text = ""
    i = 0
    while i < len(text):
        matched = False
        # Try to match substrings of varying lengths (longest first)
        for length in range(3, 0, -1):  # Check for 3-char, then 2-char, then 1-char matches
            if i + length <= len(text):
                substring = text[i:i + length]
                for tup in C_def:
                    if tup[1] == substring:  # Match found in C_def for encrypted value
                        decrypted_text += tup[0]
                        i += length
                        matched = True
                        break
            if matched:
                break
        if not matched:  # If no match is found, keep the character as is
            decrypted_text += text[i]
            i += 1
    return decrypted_text