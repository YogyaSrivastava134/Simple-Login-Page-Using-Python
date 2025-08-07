import customtkinter as ctk
import time

# Appearance
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

MAX_ATTEMPTS = 3
LOCK_TIME_SECONDS = 30

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("YCSK")
        self.root.geometry("400x500")
        self.root.resizable(False, False)

        self.attempts = 0
        self.locked = False
        self.remaining_lock_time = 0

        # Title
        self.title_label = ctk.CTkLabel(self.root, text="Login", font=("Segoe UI", 24, "bold"))
        self.title_label.pack(pady=20)

        # Username
        self.username_entry = ctk.CTkEntry(self.root, width=280, height=40, corner_radius=10, placeholder_text="Username")
        self.username_entry.pack(pady=(10, 20))

        # Password
        self.password_entry = ctk.CTkEntry(self.root, width=280, height=40, corner_radius=10, placeholder_text="Password", show="•")
        self.password_entry.pack(pady=(0, 20))

        # Feedback
        self.feedback_label = ctk.CTkLabel(self.root, text="", font=("Segoe UI", 14))
        self.feedback_label.pack(pady=10)

        # Login button
        self.login_button = ctk.CTkButton(self.root, text="Login", command=self.login, width=180, height=40, corner_radius=20, font=("Segoe UI", 16, "bold"))
        self.login_button.pack(pady=20)

        # Footer
        self.footer_label = ctk.CTkLabel(self.root, text="© 2025 YCSK", font=("Segoe UI", 10))
        self.footer_label.pack(side="bottom", pady=10)

    def login(self):
        if self.locked:
            return

        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "Admin" and password == "ABCD@1234":
            self.feedback_label.configure(text="Login successful ✅", text_color="green")
            self.reset_attempts()
        else:
            self.attempts += 1
            if self.attempts >= MAX_ATTEMPTS:
                self.lock_login()
            else:
                self.feedback_label.configure(
                    text=f"Incorrect credentials ❌ \n {MAX_ATTEMPTS - self.attempts} tries left",
                    text_color="red"
                )

    def reset_attempts(self):
        self.attempts = 0
        self.locked = False

    def lock_login(self):
        self.locked = True
        self.login_button.configure(state="disabled")
        self.remaining_lock_time = LOCK_TIME_SECONDS
        self.update_countdown()

    def update_countdown(self):
        if self.remaining_lock_time > 0:
            self.feedback_label.configure(
                text=f"Too many attempts! Try again in {self.remaining_lock_time} sec ⏳",
                text_color="orange"
            )
            self.remaining_lock_time -= 1
            self.root.after(1000, self.update_countdown)
        else:
            self.locked = False
            self.login_button.configure(state="normal")
            self.feedback_label.configure(text="You can try again now 👌", text_color="blue")
            self.reset_attempts()

# Main
if __name__ == "__main__":
    app = ctk.CTk()
    LoginApp(app)
    app.mainloop()

