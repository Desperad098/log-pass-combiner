import tkinter as tk
from tkinter import filedialog, messagebox, ttk

def read_file(file_name):
    with open(file_name, "r") as file:
        return [line.strip() for line in file]

def combine_and_save(logins, passwords, output_file):
    combined_data = [f"{login}:{password}" for login, password in zip(logins, passwords)]
    with open(output_file, "w") as file:
        file.write("\n".join(combined_data))
    return len(combined_data)

def browse_file(label):
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    label.config(text=file_path)

def combine_button_clicked(login_label, password_label):
    logins = read_file(login_label.cget("text"))
    passwords = read_file(password_label.cget("text"))

    min_length = min(len(logins), len(passwords))
    combined_count = combine_and_save(logins[:min_length], passwords[:min_length], "combined_data.txt")

    messagebox.showinfo("Result", f"{combined_count} accounts combined successfully!")

    unchecked_logins = logins[min_length:]
    if unchecked_logins:
        with open("unchecked.txt", "w") as file:
            file.write("\n".join(unchecked_logins))
        messagebox.showinfo("Unchecked Logins", "Unchecked logins saved to unchecked.txt")

def main():
    # Create the main GUI window
    root = tk.Tk()
    root.title("Log:Pass Maker")

    # Set the window size
    window_width = 400
    window_height = 200
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # Set the style for buttons
    style = ttk.Style()
    style.configure("TButton", font=("Helvetica", 12), background="#333", foreground="#000", relief="flat")

    # Set the background color of the window
    root.configure(bg="#444")

    # Create labels to display file paths
    login_label = tk.Label(root, text="Select logins file...", bg="#444", fg="#fff")
    login_label.pack(pady=5)
    password_label = tk.Label(root, text="Select passwords file...", bg="#444", fg="#fff")
    password_label.pack(pady=5)

    # Create buttons to browse and select files
    login_button = ttk.Button(root, text="Browse Logins", command=lambda: browse_file(login_label), style="TButton")
    login_button.pack(pady=5)
    password_button = ttk.Button(root, text="Browse Passwords", command=lambda: browse_file(password_label), style="TButton")
    password_button.pack(pady=5)

    # Create a button to initiate the combination process
    combine_button = ttk.Button(root, text="Combine Logins and Passwords", command=lambda: combine_button_clicked(login_label, password_label), style="TButton")
    combine_button.pack(pady=10)

    # Run the main GUI event loop
    root.mainloop()

if __name__ == "__main__":
    main()
