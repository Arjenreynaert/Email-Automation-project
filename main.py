import imaplib
import tkinter as tk
from tkinter import messagebox

def connect_imap():
    email = email_entry.get()
    password = password_entry.get()
    server = server_entry.get()
    port = port_entry.get()
    try:
        mail = imaplib.IMAP4_SSL(server, int(port))
        mail.login(email, password)
        messagebox.showinfo("Success", "Connected to IMAP server!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to connect:\n{e}")

def show_info():
    def on_select():
        selected = email_var.get()
        if selected == "Gmail":
            info_text = (
                "IMAP Server: imap.gmail.com\n"
                "IMAP Port: 993\n"
                "Email: Your full Gmail address.\n"
                "Password: Your Gmail password or app password.\n\n"
                "To enable IMAP in Gmail:\n"
                "1. Go to Gmail settings (gear icon > 'See all settings').\n"
                "2. Select 'Forwarding and POP/IMAP'.\n"
                "3. Enable IMAP under 'IMAP access'.\n"
                "4. Click 'Save changes'."
            )
        elif selected == "Yahoo":
            info_text = (
                "IMAP Server: imap.mail.yahoo.com\n"
                "IMAP Port: 993\n"
                "Email: Your full Yahoo email address.\n"
                "Password: Your Yahoo password or app password.\n\n"
                "To enable IMAP in Yahoo:\n"
                "1. Go to Yahoo Account Security settings.\n"
                "2. Enable 'Allow apps that use less secure sign-in' or create an app password.\n"
                "3. Use the app password in this application."
            )
        elif selected == "Outlook":
            info_text = (
                "IMAP Server: outlook.office365.com\n"
                "IMAP Port: 993\n"
                "Email: Your full Outlook/Hotmail address.\n"
                "Password: Your Outlook password or app password.\n\n"
                "To enable IMAP in Outlook:\n"
                "1. IMAP is enabled by default for Outlook.com accounts.\n"
                "2. If using two-factor authentication, create an app password:\n"
                "   a. Go to https://account.live.com/proofs/Manage.\n"
                "   b. Under 'Security', select 'Create a new app password'.\n"
                "   c. Use the generated app password in this application."
            )
        else:
            info_text = (
                "IMAP Server: The address of your email provider's IMAP server.\n"
                "IMAP Port: Usually 993 for secure connections.\n"
                "Email: Your full email address.\n"
                "Password: Your email account password."
            )
        messagebox.showinfo(f"{selected} IMAP Info", info_text)
        info_win.destroy()

    info_win = tk.Toplevel()
    info_win.title("Select Email Provider")
    tk.Label(info_win, text="Which email provider do you use?").pack(pady=10)
    email_var = tk.StringVar(value="Gmail")
    for provider in ["Gmail", "Yahoo", "Outlook", "Other"]:
        tk.Radiobutton(info_win, text=provider, variable=email_var, value=provider).pack(anchor="w")
    tk.Button(info_win, text="Show Info", command=on_select).pack(pady=10)

root = tk.Tk()
root.title("IMAP Client")
root.geometry("400x250")

top_frame = tk.Frame(root)
top_frame.pack(fill="x")

tk.Label(top_frame, text="Email:").pack()
email_entry = tk.Entry(top_frame, width=40)
email_entry.pack()

tk.Label(top_frame, text="Password:").pack()
password_entry = tk.Entry(top_frame, show="*", width=40)
password_entry.pack()

tk.Label(top_frame, text="IMAP Server:").pack()
server_entry = tk.Entry(top_frame, width=40)
server_entry.insert(0, "imap.example.com")
server_entry.pack()

tk.Label(top_frame, text="IMAP Port:").pack()
port_entry = tk.Entry(top_frame, width=40)
port_entry.insert(0, "993")
port_entry.pack()

btn_frame = tk.Frame(root)
btn_frame.pack(pady=15)

connect_btn = tk.Button(btn_frame, text="Connect", command=connect_imap)
connect_btn.pack(side="left", padx=10)

info_btn = tk.Button(btn_frame, text="ℹ️", command=show_info)
info_btn.pack(side="left")

root.mainloop()
