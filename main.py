import tkinter
import tkinter.messagebox
import password_generator
import pandas
import os

VAULT_FILE_PATH = "vault.csv"
APP_LOGO_PATH = "logo.png"

PWD_GEN_LETTER = 3
PWD_GEN_SYMBOL = 3
PWD_GEN_NUMBER = 3

def login():
    username = input_username.get()
    password = input_password.get()

    if username == "" and password == "":
        login_frame.pack_forget()
        password_manager_frame.pack()
        #show_password_manager()
    else:
        tkinter.messagebox.showerror("Login Failed", "Invalid username or password")

# Fungsi untuk keluar aplikasi
def exit_app():
    window.destroy()

def generate_password():
    pwd = password_generator.generate(PWD_GEN_LETTER, PWD_GEN_SYMBOL, PWD_GEN_NUMBER)
    input_password.delete(0, tkinter.END)
    input_password.insert(0, pwd)

    window.clipboard_clear()
    window.clipboard_append(pwd)
    window.update()

def save():
    website = input_website.get()
    username = input_username.get()
    password = input_password.get()

    if website == "":
        tkinter.messagebox.showerror("Error", "Website is required")
        return

    if username == "":
        tkinter.messagebox.showerror("Error", "Username is required")
        return

    if password == "":
        tkinter.messagebox.showerror("Error", "Password is required")
        return

    confirmation_message = f"""
        Do you want to save this password?
        
        Website: {website}
        Username/email: {username}
        Password: {password}
    """
    confirmation = tkinter.messagebox.askokcancel("Save Confirmation", confirmation_message)

    if not confirmation:
        return

    data_frame = {
        "website": [website],
        "username": [username],
        "password": [password],
    }

    save_data = pandas.DataFrame(data_frame)
    save_data.to_csv(VAULT_FILE_PATH, index=False, mode="a", header=not os.path.exists(VAULT_FILE_PATH))

    tkinter.messagebox.showinfo("Success", "Password saved!")

    input_password.delete(0, tkinter.END)
    input_username.delete(0, tkinter.END)
    input_website.delete(0, tkinter.END)


window = tkinter.Tk()
window.title("Password Manager")
window.configure(padx=20, pady=20)

def show_password_manager():
    password_manager_frame.pack()
    password_list_frame.pack()

    if os.path.exists(VAULT_FILE_PATH):
        data = pandas.read_csv(VAULT_FILE_PATH)
        password_list.delete("1.0", tkinter.END)
        password_list.insert(tkinter.END, data.to_string(index=False))


# Tampilan otentikasi login
login_frame = tkinter.Frame(window)
login_frame.pack(pady=10)

label_username = tkinter.Label(login_frame, text="Username")
label_username.pack()
input_username = tkinter.Entry(login_frame, width=35)
input_username.pack()

label_password = tkinter.Label(login_frame, text="Password")
label_password.pack()
input_password = tkinter.Entry(login_frame, width=35, show="*")
input_password.pack(pady=10)

login_button = tkinter.Button(login_frame, text="Login", command=login)
login_button.pack()

# Tampilan aplikasi Password Manager
password_manager_frame = tkinter.Frame(window)

logo = tkinter.PhotoImage(file=APP_LOGO_PATH)
logo_canvas = tkinter.Canvas(password_manager_frame, width=200, height=200)
logo_canvas.create_image(100, 100, image=logo)
logo_canvas.grid(row=0, column=1)

label_website = tkinter.Label(password_manager_frame, text="Website:")
label_website.grid(row=1, column=0)
input_website = tkinter.Entry(password_manager_frame, width=36)
input_website.grid(row=1, column=1, columnspan=2, pady=10)

label_username = tkinter.Label(password_manager_frame, text="Email/Username:")
label_username.grid(row=2, column=0)
input_username = tkinter.Entry(password_manager_frame, width=36)
input_username.grid(row=2, column=1, columnspan=2, pady=10)

label_password = tkinter.Label(password_manager_frame, text="Password:")
label_password.grid(row=3, column=0)
input_password = tkinter.Entry(password_manager_frame, width=36)
input_password.grid(row=3, column=1, columnspan=2, pady=10)

generate_pwd_button = tkinter.Button(password_manager_frame, text="Generate", command=generate_password)
generate_pwd_button.grid(row=3, column=3)

save_button = tkinter.Button(password_manager_frame, text="Save", width=36, command=save)
save_button.grid(row=4, column=1, columnspan=2, pady=10)

show_password_button = tkinter.Button(password_manager_frame, text="Show Password", command=show_password_manager)
show_password_button.grid(row=5, column=1, columnspan=2, pady=5)

exit_button = tkinter.Button(password_manager_frame, text="Exit", command=exit_app)
exit_button.grid(row=6, column=1, columnspan=2, pady=5)

# Halaman List password
password_list_frame = tkinter.Frame(window)

password_list = tkinter.Text(password_list_frame, height=10, width=80)
password_list.pack()
password_list_frame.pack_forget()

window.mainloop()
