import tkinter as tk
from tkinter import messagebox

# membuat data username dan paswword yang benar
username_yang_benar = "namalia"
password_yang_benar = "98765"

# membuat fungsi untuk login
def login():
    try:
        username = masukkan_username.get()
        password = masukkan_password.get()
# memvalidasi username harus huruf bukan angka
        if not username.isalpha():
            raise ValueError("Username harus berupa teks bukan angka")

# memvalidasi password harus angka bukan huruf atau teks
        if not password.isdigit():
            raise ValueError("Password harus berupa angka bukan huruf")

# memeriksa kecocokan username dan password
        if username == username_yang_benar and password == password_yang_benar:
            messagebox.showinfo("Selamat", "Login anda berhasil")
        else:
            messagebox.showerror("Erorr", "Username atau password yang anda masukkan salah")

        masukkan_username.delete(0, tk.END)
        masukkan_password.delete(0, tk.END)

    except ValueError as e:
        messagebox.showwarning("Peringatan error", str(e))

# membuat jendela utama
root = tk.Tk()
root.title("Login")
root.geometry("400x200")

# membuat tampilan  login username
tk.Label(root, text="Username").pack()
masukkan_username = tk.Entry(root)
masukkan_username.pack()

#membuat tampilan login password
tk.Label(root, text="Password").pack()
masukkan_password = tk.Entry(root, show="*")
masukkan_password.pack()

# membuat tombol login masuk
tk.Button(root, text="Login", command=login).pack(pady=10)

root.mainloop()