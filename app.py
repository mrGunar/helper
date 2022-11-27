import customtkinter as ctk
from services import *


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Application for generating training program")
        self.minsize(200, 200)

        self.generate_button = ctk.CTkButton(master=self,
                                            text="Generate", 
                                            command=...)
        self.generate_button.grid(row=2, column=4, padx=50, pady=20)

        self.add_exercise_button = ctk.CTkButton(master=self, 
                                                           text="Add exercise", 
                                                           command=...)
        self.add_exercise_button.grid(row=0, column=0, padx=20, pady=20)
        
        self.checkbox = ctk.CTkCheckBox(master=self, text="check box")
        self.checkbox.grid(row=1, column=0, pady=40, padx=22)


if __name__ == "__main__":
    app = App()
    app.mainloop()
