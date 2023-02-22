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

logo = tkinter.PhotoImage(file=APP_LOGO_PATH)
logo_canvas = tkinter.Canvas(window, width=200, height=200)
logo_canvas.create_image(100, 100, image=logo)
logo_canvas.grid(row=0, column=1)

label_website = tkinter.Label(text="Website:")
label_website.grid(row=1, column=0)
input_website = tkinter.Entry(width=35)
input_website.grid(row=1, column=1, columnspan=2)

label_username = tkinter.Label(text="Email/Username:")
label_username.grid(row=2, column=0)
input_username = tkinter.Entry(width=35)
input_username.grid(row=2, column=1, columnspan=2)

label_password = tkinter.Label(text="Password:")
label_password.grid(row=3, column=0)
input_password = tkinter.Entry(width=21)
input_password.grid(row=3, column=1)
generate_pwd_button = tkinter.Button(text="Generate Password", command=generate_password)
generate_pwd_button.grid(row=3, column=2)

save_button = tkinter.Button(text="Save", width=36, command=save)
save_button.grid(row=4, column=1, columnspan=2)

window.mainloop()