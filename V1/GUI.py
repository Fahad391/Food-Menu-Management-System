import customtkinter as gui
from Inventory_Management import add_dish, view_menu

gui.set_appearance_mode("Dark")  # Forces dark mode by default
gui.set_default_color_theme("blue") 

# Created a class for GUI to manage the inventory
class Inventory(gui.CTk):
    def __init__(self):
        super().__init__()

        self.title("Food Menu Management System")
        self.geometry("600x600")
        self.resizable(False, False)

        #  Title Label
        self.title_label = gui.CTkLabel(self, text="Restaurant Menu Manager", font=gui.CTkFont(size=22, weight="bold"))
        self.title_label.pack(padx=20, pady=(20, 10))

        # Created Frame for Input Section
        self.input_frame = gui.CTkFrame(self)
        self.input_frame.pack(padx=20, pady=10, fill="x")
# CODE REVISION: 
# .pack() -> Stacks this frame vertically into the main window interface.
# padx=20 -> Adds 20 pixels of empty space on the left and right (horizontal margins).
# pady=10 -> Adds 10 pixels of empty space on the top and bottom (vertical margins).
# fill="x" -> Makes the frame stretch horizontally to fill the entire width of the window.
        self.name_label = gui.CTkLabel(self.input_frame, text="Dish Name:", font=gui.CTkFont(size=14))
        self.name_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        
        self.name_entry = gui.CTkEntry(self.input_frame, width=250)
        self.name_entry.grid(row=0, column=1, padx=10, pady=10)

        self.price_label = gui.CTkLabel(self.input_frame, text="Price (BDT):", font=gui.CTkFont(size=14))
        self.price_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        
        self.price_entry = gui.CTkEntry(self.input_frame, width=250)
        self.price_entry.grid(row=1, column=1, padx=10, pady=10)

        # Buttons
        self.add_button = gui.CTkButton(self, text="Add Item to Menu", command=self.handle_add_dish)
        self.add_button.pack(padx=20, pady=10, fill="x")

        self.view_button = gui.CTkButton(self, text="Refresh / View Menu", fg_color="transparent", border_width=2, command=self.handle_view_menu)
        self.view_button.pack(padx=20, pady=5, fill="x")

        # Output Log
        self.status_label = gui.CTkLabel(self, text="", text_color="green", font=gui.CTkFont(size=12))
        self.status_label.pack(pady=5)

        self.display_area = gui.CTkTextbox(self, width=460, height=200, state="disabled")
        self.display_area.pack(padx=20, pady=10)

        # Initial view load
        self.handle_view_menu()
# Created 2 functions handle_add_dish & handle_view_menu 
    def handle_add_dish(self):
        """Extracts data from UI and interfaces with backend script."""
        name = self.name_entry.get().strip()
        price = self.price_entry.get().strip()

        try:
            add_dish(name, price)
            
            # Clear fields and display success message
            self.name_entry.delete(0, 'end')
            self.price_entry.delete(0, 'end')
            self.status_label.configure(text=f"Successfully added '{name}'!", text_color="#2ed573")
            
            # Auto refresh view
            self.handle_view_menu()
            
        except ValueError as e:
            self.status_label.configure(text=str(e), text_color="#ff4757")

    def handle_view_menu(self):
        """Retrieves text from backend logic and updates the display text box safely."""
        menu_content = view_menu()
        
        # Textboxes must be set to normal mode before changing text, then set back to disabled
        self.display_area.configure(state="normal")
        self.display_area.delete("1.0", "end")
        self.display_area.insert("1.0", menu_content)
        self.display_area.configure(state="disabled")
