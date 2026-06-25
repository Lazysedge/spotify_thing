import customtkinter as ctk


class ProgressPanel(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)

        # -------------------------
        # Title
        # -------------------------
        self.title_label = ctk.CTkLabel(
            self,
            text="Progress",
            font=("Arial", 20, "bold")
        )

        self.title_label.pack(
            pady=(10, 5)
        )

        # -------------------------
        # Status text
        # -------------------------
        self.status_label = ctk.CTkLabel(
            self,
            text="Ready",
            anchor="w"
        )

        self.status_label.pack(
            fill="x",
            padx=10
        )

        # -------------------------
        # Progress bar
        # -------------------------
        self.progress_bar = ctk.CTkProgressBar(
            self
        )

        self.progress_bar.pack(
            fill="x",
            padx=10,
            pady=10
        )

        self.progress_bar.set(0)

        # -------------------------
        # Percentage text
        # -------------------------
        self.percent_label = ctk.CTkLabel(
            self,
            text="0%"
        )

        self.percent_label.pack()

        # -------------------------
        # Log box
        # -------------------------
        self.log_box = ctk.CTkTextbox(
            self,
            height=200
        )

        self.log_box.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        self.log_box.configure(
            state="disabled"
        )

    # --------------------------------
    # Update percentage
    # --------------------------------
    def update_progress(
        self,
        current,
        total,
        message=""
    ):

        if total == 0:
            progress = 0
        else:
            progress = current / total

        self.progress_bar.set(
            progress
        )

        percent = progress * 100

        self.percent_label.configure(
            text=f"{percent:.1f}%"
        )

        if message:
            self.status_label.configure(
                text=message
            )

    # --------------------------------
    # Add log message
    # --------------------------------
    def log(
        self,
        message
    ):
        self.log_box.configure(
            state="normal"
        )

        self.log_box.insert(
            "end",
            message + "\n"
        )

        self.log_box.see("end")

        self.log_box.configure(
            state="disabled"
        )

    # --------------------------------
    # Reset
    # --------------------------------
    def reset(self):

        self.progress_bar.set(0)

        self.percent_label.configure(
            text="0%"
        )

        self.status_label.configure(
            text="Ready"
        )

        self.log_box.configure(
            state="normal"
        )

        self.log_box.delete(
            "1.0",
            "end"
        )

        self.log_box.configure(
            state="disabled"
        )