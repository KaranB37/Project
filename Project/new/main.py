import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Sign In")

# Create the labels and entry fields for username and password
tk.Label(root, text="Username").grid(row=0)
username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1)
tk.Label(root, text="Password").grid(row=1)
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=1, column=1)

# Create the function that will be called when the "Sign In" button is pressed
def sign_in():
    # Get the username and password entered by the user
    username = username_entry.get()
    password = password_entry.get()

    # Check if the username and password are correct
    if username == "admin" and password == "password":
        # If they are, show a success message
        tk.messagebox.showinfo("Success", "You have successfully signed in!")
    else:
        # If they aren't, show an error message
        tk.messagebox.showerror("Error", "Incorrect username or password.")

# Create the "Sign In" button
tk.Button(root, text="Sign In", command=sign_in).grid(row=2, columnspan=2)

# Start the main event loop
root.mainloop()