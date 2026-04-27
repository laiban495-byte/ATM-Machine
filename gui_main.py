"""
Author: Harsh Yadav
Branch: CSE-DS
Project: ATM Simulation (HDFC Bank Theme GUI)
"""

import customtkinter as ctk
from tkinter import messagebox
from atm_package import atm_logic

# Theme setup for HDFC Bank Colors
HDFC_BLUE = "#004c8f"
HDFC_RED = "#ed1b24"
BG_COLOR = "#f4f6f9"
TEXT_DARK = "#1a1a1a"

class HDFC_ATM_UI(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("HDFC Bank ATM Simulator")
        self.geometry("850x750")
        self.configure(fg_color=BG_COLOR)
        
        # Setup starting data
        self.balance = 0.0
        self.history = []
        self.input_buffer = ""
        self.current_mode = "MENU" 
        
        self.build_ui()
        self.show_main_menu()

    def build_ui(self):
        # Header Frame
        self.header_frame = ctk.CTkFrame(self, fg_color=HDFC_BLUE, height=100, corner_radius=0)
        self.header_frame.pack(fill="x", side="top")
        
        # HDFC Bank Logo Mockup
        self.logo_box = ctk.CTkFrame(self.header_frame, fg_color=HDFC_RED, width=45, height=45, corner_radius=6)
        self.logo_box.place(x=30, rely=0.5, anchor="w")
        
        self.header_label = ctk.CTkLabel(
            self.header_frame, 
            text="HDFC BANK", 
            font=("Arial", 32, "bold"), 
            text_color="white"
        )
        self.header_label.place(x=90, rely=0.45, anchor="w")
        
        self.tagline_label = ctk.CTkLabel(
            self.header_frame, 
            text="We understand your world", 
            font=("Arial", 16, "italic"), 
            text_color="#cce0ff"
        )
        self.tagline_label.place(x=90, rely=0.75, anchor="w")

        # Main Content Frame (Screen)
        self.content_frame = ctk.CTkFrame(self, fg_color="white", corner_radius=15, border_width=2, border_color="#d0d0d0")
        self.content_frame.pack(fill="both", expand=True, padx=40, pady=(30, 10))
        
        # Screen Text
        self.screen_label = ctk.CTkLabel(
            self.content_frame, 
            text="", 
            font=("Helvetica", 22, "bold"), 
            text_color=HDFC_BLUE,
            justify="center"
        )
        self.screen_label.pack(expand=True, pady=15)

        # Options Frame (For buttons)
        self.options_frame = ctk.CTkFrame(self.content_frame, fg_color="transparent")
        self.options_frame.pack(fill="x", padx=20, pady=20)
        
        # Dynamic Buttons
        self.btn_1 = self.create_option_button("", lambda: self.handle_option(1))
        self.btn_2 = self.create_option_button("", lambda: self.handle_option(2))
        self.btn_3 = self.create_option_button("", lambda: self.handle_option(3))
        self.btn_4 = self.create_option_button("", lambda: self.handle_option(4))
        
        # Grid layout for options
        self.options_frame.columnconfigure(0, weight=1)
        self.options_frame.columnconfigure(1, weight=1)
        self.btn_1.grid(row=0, column=0, padx=15, pady=10, sticky="ew")
        self.btn_2.grid(row=0, column=1, padx=15, pady=10, sticky="ew")
        self.btn_3.grid(row=1, column=0, padx=15, pady=10, sticky="ew")
        self.btn_4.grid(row=1, column=1, padx=15, pady=10, sticky="ew")

        # Keypad Section (Bottom)
        self.keypad_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.keypad_frame.pack(pady=15)
        
        self.build_keypad()

    def create_option_button(self, text, command):
        return ctk.CTkButton(
            self.options_frame, 
            text=text, 
            font=("Arial", 18, "bold"),
            fg_color=HDFC_BLUE, 
            hover_color="#003366",
            text_color="white",
            corner_radius=8,
            height=60,
            command=command
        )

    def build_keypad(self):
        keys = [
            ('1', 0, 0), ('2', 0, 1), ('3', 0, 2), ('CANCEL', 0, 3, HDFC_RED, '#cc0000'),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('CLEAR', 1, 3, '#f39c12', '#d68910'),
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('ENTER', 2, 3, '#27ae60', '#219150'),
            ('00', 3, 0), ('0', 3, 1), ('.', 3, 2)
        ]
        
        for key_data in keys:
            if len(key_data) == 3:
                text, row, col = key_data
                bg_color = "#e8e8e8"
                hover_color = "#d0d0d0"
                text_color = TEXT_DARK
            else:
                text, row, col, bg_color, hover_color = key_data
                text_color = "white"
                
            btn = ctk.CTkButton(
                self.keypad_frame, 
                text=text, 
                width=85, 
                height=60, 
                font=("Arial", 20, "bold"),
                fg_color=bg_color, 
                hover_color=hover_color,
                text_color=text_color,
                corner_radius=8,
                command=lambda t=text: self.keypad_pressed(t)
            )
            btn.grid(row=row, column=col, padx=8, pady=8)

    def set_buttons_visibility(self, visible, btn1_text="", btn2_text="", btn3_text="", btn4_text=""):
        if visible:
            self.options_frame.pack(fill="x", padx=20, pady=20)
            self.btn_1.configure(text=btn1_text, state="normal" if btn1_text else "disabled")
            self.btn_2.configure(text=btn2_text, state="normal" if btn2_text else "disabled")
            self.btn_3.configure(text=btn3_text, state="normal" if btn3_text else "disabled")
            self.btn_4.configure(text=btn4_text, state="normal" if btn4_text else "disabled")
        else:
            self.options_frame.pack_forget()

    def update_screen(self, text):
        self.screen_label.configure(text=text)

    def show_main_menu(self):
        self.current_mode = "MENU"
        self.input_buffer = ""
        self.update_screen("Welcome to HDFC Bank\n\nPlease select your transaction")
        self.set_buttons_visibility(True, "Check Balance", "Deposit Money", "Withdraw Money", "Mini Statement")

    def handle_option(self, opt_num):
        if self.current_mode == "MENU":
            if opt_num == 1:
                bal_str = atm_logic.display_balance(self.balance)
                self.update_screen(f"Available Balance\n\n{bal_str}\n\nPress CANCEL to exit")
                self.set_buttons_visibility(False)
                self.current_mode = "VIEW"
                
            elif opt_num == 2:
                self.current_mode = "DEPOSIT"
                self.input_buffer = ""
                self.refresh_input_screen()
                self.set_buttons_visibility(False)
                
            elif opt_num == 3:
                self.current_mode = "WITHDRAW"
                self.input_buffer = ""
                self.refresh_input_screen()
                self.set_buttons_visibility(False)
                
            elif opt_num == 4:
                history_list = self.history[-5:] if self.history else ["No recent transactions."]
                history_text = "\n".join(history_list)
                self.update_screen(f"Recent Transactions\n\n{history_text}\n\nPress CANCEL to exit")
                self.set_buttons_visibility(False)
                self.current_mode = "VIEW"

    def refresh_input_screen(self):
        if self.current_mode == "DEPOSIT":
            self.update_screen(f"Enter Amount to Deposit:\n\n₹ {self.input_buffer}_\n\nPress ENTER to confirm")
        elif self.current_mode == "WITHDRAW":
            self.update_screen(f"Enter Amount to Withdraw:\n\n₹ {self.input_buffer}_\n\nPress ENTER to confirm")

    def keypad_pressed(self, key):
        if key == "CANCEL":
            self.show_main_menu()
        elif key == "CLEAR":
            self.input_buffer = ""
            self.refresh_input_screen()
        elif key == "ENTER":
            self.process_enter()
        else:
            if self.current_mode in ["DEPOSIT", "WITHDRAW"]:
                self.input_buffer += key
                self.refresh_input_screen()

    def process_enter(self):
        if self.current_mode == "DEPOSIT":
            try:
                amt = float(self.input_buffer)
                if amt <= 0:
                    raise ValueError
                self.balance = atm_logic.deposit(self.balance, amt, self.history)
                self.update_screen(f"Transaction Successful\n\nDeposited: ₹{amt:.2f}\nNew Balance: ₹{self.balance:.2f}\n\nPress CANCEL to return")
            except ValueError:
                self.update_screen("Invalid Amount Entered\n\nPress CANCEL to return")
            self.current_mode = "VIEW"
            
        elif self.current_mode == "WITHDRAW":
            try:
                amt = float(self.input_buffer)
                if amt <= 0:
                    raise ValueError
                    
                old_balance = self.balance
                self.balance = atm_logic.withdraw(self.balance, amt, self.history)
                
                if self.balance == old_balance: 
                    self.update_screen("Transaction Failed\n\nInsufficient Funds\n\nPress CANCEL to return")
                else:
                    self.update_screen(f"Please collect your cash\n\nTransaction Successful\nNew Balance: ₹{self.balance:.2f}\n\nPress CANCEL to return")
            except ValueError:
                self.update_screen("Invalid Amount Entered\n\nPress CANCEL to return")
            self.current_mode = "VIEW"

if __name__ == "__main__":
    ctk.set_appearance_mode("light")
    app = HDFC_ATM_UI()
    app.mainloop()
