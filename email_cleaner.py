import os
import tkinter as tk
from tkinter import messagebox, filedialog

def compare_and_delete_bad_emails(bad_emails_file, all_emails_file):
    with open(bad_emails_file, 'r', encoding='utf-8') as f:
        bad_emails = set(f.read().splitlines())

    with open(all_emails_file, 'r', encoding='utf-8') as f:
        all_emails = f.read().splitlines()

    deleted_emails = []
    updated_emails = []

    for email in all_emails:
        if email in bad_emails:
            deleted_emails.append(email)
        else:
            updated_emails.append(email)

    with open(all_emails_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(updated_emails))

    with open('deleted.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(deleted_emails))

    num_deleted_emails = len(deleted_emails)
    messagebox.showinfo("Cleanup Complete", f"Emails cleaned up!\nDeleted {num_deleted_emails} email(s) and saved them to deleted.txt.")

def browse_all_emails():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    all_emails_entry.delete(0, tk.END)
    all_emails_entry.insert(tk.END, file_path)

def browse_bad_emails():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    bad_emails_entry.delete(0, tk.END)
    bad_emails_entry.insert(tk.END, file_path)

def execute_comparison():
    all_emails_path = all_emails_entry.get()
    bad_emails_path = bad_emails_entry.get()

    if not os.path.exists(all_emails_path):
        messagebox.showerror("File Not Found", f"File not found: {all_emails_path}")
        return

    if not os.path.exists(bad_emails_path):
        messagebox.showerror("File Not Found", f"File not found: {bad_emails_path}")
        return

    if os.path.exists('deleted.txt'):
        os.remove('deleted.txt')
        print("Found old deleted.txt file and cleaned it.")

    compare_and_delete_bad_emails(bad_emails_path, all_emails_path)


window = tk.Tk()
window.title("Compare and Delete Bad Emails")
window.geometry("400x250")


all_emails_label = tk.Label(window, text="All Emails File:")
all_emails_label.pack(pady=10)

all_emails_entry = tk.Entry(window, width=40)
all_emails_entry.pack(pady=5)

bad_emails_label = tk.Label(window, text="Bad Emails File:")
bad_emails_label.pack(pady=10)

bad_emails_entry = tk.Entry(window, width=40)
bad_emails_entry.pack(pady=5)

buttons_frame = tk.Frame(window)
buttons_frame.pack()

browse_all_emails_button = tk.Button(buttons_frame, text="Browse All Emails", command=browse_all_emails)
browse_all_emails_button.pack(side=tk.LEFT, padx=5)

browse_bad_emails_button = tk.Button(buttons_frame, text="Browse Bad Emails", command=browse_bad_emails)
browse_bad_emails_button.pack(side=tk.LEFT, padx=5)

execute_button = tk.Button(window, text="Execute", command=execute_comparison)
execute_button.configure(bg="blue", fg="white")
execute_button.pack(pady=10)

window.mainloop()
