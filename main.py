import tkinter as tk
import profile as userAccount

def login_press(user, entry_username, entry_password):
    """
    This function handles the events when the login button is pressed
    :param user: class variable for user
    :param entry_username: username ID
    :param entry_password: Password for the username ID
    :return: None
    """

    database = user.accounts
    if entry_username in database:
        if database[entry_username] == entry_password:
            print("User Found! Welcome", entry_username)
        else:
            print("Wrong Password!")
    else:
        print("Username", entry_username, "not found!")

def register_press(user, screen):
    regWindow = tk.Toplevel(screen)
    regWindow.title("Register User")
    regWindow.geometry("300x300")
    regWindow.configure(bg='#33C7FF')

    inst = tk.Label(regWindow, text="\nRegister Username and Password\n\n", bg='#33C7FF')
    inst.config(font=("Courier bold", 14))
    inst.pack()

    username = tk.Label(regWindow, text="Username: ", font=("Courier bold", 14), bg='#33C7FF').pack()
    entry_username = tk.Entry(regWindow, width=30)
    entry_username.pack()

    password = tk.Label(regWindow, text="Password: ", font=("Courier bold", 14), bg='#33C7FF').pack()
    entry_password = tk.Entry(regWindow, width=30)
    entry_password.pack()

    tk.Label(regWindow, text=" ", bg='#33C7FF').pack()
    register = tk.Button(regWindow, font=("Courier bold", 12), text='Register', bg='light gray', width=8, command= lambda: registerUser(user, entry_username.get(), entry_password.get()))
    register.pack()

def registerUser(user, username, password):
    if len(username) > 5 and len(password) > 5:
        user.register_account(username, password)

def main_application(screen, user):
    """
    This function runs the user login application using Tkinter.
    :return: screen - Tk() window
    """

    screen.geometry("500x400")
    screen.title("Login System")
    screen.configure(bg='#33C7FF')

    welcome = tk.Label(screen, text="Welcome!\n\nEnter Username and Password", bg='#33C7FF', pady=30)
    welcome.config(font=("Courier bold", 20))
    welcome.pack()

    username = tk.Label(screen, text="Username: ", bg='#33C7FF', font=("Courier bold", 14)).pack()
    entry_username = tk.Entry(screen, width=30)
    entry_username.pack()

    password = tk.Label(screen, text="Password: ", bg='#33C7FF', font=("Courier bold", 14)).pack()
    entry_password = tk.Entry(screen, width=30, show='*')
    entry_password.pack()
    tk.Label(text=" ", bg='#33C7FF').pack()
    button = tk.Button(screen, font=("Courier bold", 13), text="Login", bg="light gray", width=10, command= lambda: login_press(user, entry_username.get(), entry_password.get()))
    button.pack()

    tk.Label(text=" ", bg='#33C7FF').pack()
    register = tk.Button(screen, font=("Courier bold", 13), text='Register', bg='light gray', width=10, command= lambda: register_press(user, screen))
    register.pack()

    return screen

if __name__ == '__main__':
    user = userAccount.UserProfile()
    screen = tk.Tk()
    win = main_application(screen, user)
    win.mainloop()