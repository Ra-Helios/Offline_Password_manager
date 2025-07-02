# Offline Password Manager

- **Offline Password Manager** is a _secure_, _cross-platform_ desktop application built with `Python`. 
- It allows you to _store_, _search_, _add_, _edit_, and _delete_ your **_passwords_** and **_usernames_** for various websites or services or domains
- All encrypted and saved _locally_ on your device.
- **No** internet connection is required, and your sensitive data never leaves your computer.
- Features include a _user-friendly_ **_GUI_** ( Using CustomTkinter Py-Lib ), _master password authentication_, _clipboard copy_, and _robust encryption_ for all stored credentials.

  
---


# Index

>- Setup for [**_WindowsOS_**](#-setup-for-windowsos)
>- Setup for [**_LinuxOS_**](#-setup-for-linuxos)
>- Setup for [**_MacOS_**](#-setup-for-macos)

Follow the steps below after downloading and extracting the **_.zip_**


---


## 🔵 Setup for WindowsOS

#### 1. Install the Dependencies:

  There are Two methods to install the dependencies (_Python Libraries_)

  1. ##### With Virtual Environment :- (_Recommanded_)
      Open the extracted Folder, **_Right-click_** on the screen, **_click-on_** [`"Open in Terminal"`] to  Open  **Windows Powershell** ( _Recommanded_ )  and type the following command/s,
      
      ```
      
      python -m venv .venv
      .\.venv\Scripts\activate.ps1
      pip install -r requirements.txt
      
      ```
      
  > [!NOTE]
  > Only Works on Windows PowerShell
      
OR,

  2. ##### Without Virtual Environment :-
      Open the extracted Folder, **_Right-click_** on the screen, **_click-on_** [`"Open in Terminal"`] to  Open  **Windows Powershell** ( _Recommanded_ )  and type the following command/s,

     ```

     pip install -r requirements.txt

     ```
     
#### 2. Run the Program for the First Time:

  After installation of Dependencies, Run `RUN.py` in **_Windows Powershell_** or any Terminal, 

  ```

  python RUN.py

  ```

  > [!NOTE]
  > If you use **Virtual Environment** , activate it before running the program,
  > ```
  >
  >.\.venv\Scripts\activate.ps1
  >
  >```
  > _Only Works on Windows PowerShell_

  Now , you can set-up your `App-Login` password and continue using the program .
  You can run the program as required by using the same commands as above after `App-Login` password setup.
     
---

## 🟢 Setup for LinuxOS

#### 1. Install the Dependencies:

  There are Two methods to install the dependencies (_Python Libraries_)

   1. ##### With Virtual Environment :- (_Recommended_)

         Open the extracted Folder, **_Right-click_** on the screen, **_click-on_** [`"Open in Terminal"`] to open your terminal and type the following commands,

   ```

    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
   
   ```

   
> [!NOTE]
> If you get errors related to Tkinter, install it via your package manager:
> ```
> sudo apt update
> sudo apt install python3-tk
> ```
> _Required for GUI support on many Linux distributions._

  OR,

  2. ##### Without Virtual Environment :-
     
      Open the extracted Folder, **_Right-click_** on the screen, **_click-on_** [`"Open in Terminal"`] and type,

 ```

pip install -r requirements.txt

```

  
  #### 2. Run the Program for the First Time:

  After installing dependencies, run `RUN.py` in your terminal,

  ```
python3 RUN.py

```


> [!NOTE]
> If you use a virtual environment, activate it before running the program:
>
> ```
> source .venv/bin/activate
> ```

Now, you can set up your `App-Login` password and continue using the program.
You can run the program as required by using the same commands as above after `App-Login` password setup.

---

## 🍎 Setup for MacOS

#### 1. Install the Dependencies:

There are Two methods to install the dependencies (_Python Libraries_)

  1. ##### With Virtual Environment :- (_Recommended_)
      Open the extracted Folder, open your **Terminal**, and type,

```

  python3 -m venv .venv
  source .venv/bin/activate
  pip install -r requirements.txt

```


> [!NOTE]
> If you get errors related to Tkinter, you may need to install it with Homebrew:
> ```
> brew install python
> pip install tk
> ```
> _Tkinter is required for GUI support._

  OR,

  2. ##### Without Virtual Environment :-
      Open the extracted Folder, open your **Terminal**, and type,
     ```
     
     pip install -r requirements.txt
     
     ```

     
#### 2. Run the Program for the First Time:

After installing dependencies, run `RUN.py` in your terminal:

   ```

    python3 RUN.py

  ```

> [!NOTE]
> If you use a virtual environment, activate it before running the program:
>
> ```
> source .venv/bin/activate
> ```

Now, you can set up your `App-Login` password and continue using the program.
You can run the program as required by using the same commands as above after `App-Login` password setup.


---
---
<ins> _End of File_  </ins>
