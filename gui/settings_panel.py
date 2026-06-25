import customtkinter as ctk
from tkinter import filedialog
import multiprocessing


class SettingsPanel(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)

        # --------------------------------
        # Title
        # --------------------------------
        title = ctk.CTkLabel(
            self,
            text="Settings",
            font=("Arial", 20, "bold")
        )

        title.pack(
            pady=(10, 20)
        )

        # --------------------------------
        # Download Folder
        # --------------------------------
        self.download_folder = ""

        folder_frame = ctk.CTkFrame(self)
        folder_frame.pack(
            fill="x",
            padx=10,
            pady=5
        )

        ctk.CTkLabel(
            folder_frame,
            text="Download Folder"
        ).pack(side="left", padx=10)

        self.folder_label = ctk.CTkLabel(
            folder_frame,
            text="Not selected"
        )

        self.folder_label.pack(
            side="left",
            padx=10
        )

        ctk.CTkButton(
            folder_frame,
            text="Browse",
            command=self.select_folder
        ).pack(
            side="right",
            padx=10
        )

        # --------------------------------
        # Audio Format
        # --------------------------------
        format_frame = ctk.CTkFrame(self)
        format_frame.pack(
            fill="x",
            padx=10,
            pady=5
        )

        ctk.CTkLabel(
            format_frame,
            text="Audio Format"
        ).pack(
            side="left",
            padx=10
        )

        self.format_menu = ctk.CTkOptionMenu(
            format_frame,
            values=[
                "mp3",
                "flac",
                "m4a",
                "wav"
            ]
        )

        self.format_menu.set("mp3")
        self.format_menu.pack(
            side="right",
            padx=10
        )

        # --------------------------------
        # Bitrate
        # --------------------------------
        bitrate_frame = ctk.CTkFrame(self)
        bitrate_frame.pack(
            fill="x",
            padx=10,
            pady=5
        )

        ctk.CTkLabel(
            bitrate_frame,
            text="Bitrate"
        ).pack(
            side="left",
            padx=10
        )

        self.bitrate_menu = ctk.CTkOptionMenu(
            bitrate_frame,
            values=[
                "128k",
                "192k",
                "320k"
            ]
        )

        self.bitrate_menu.set("320k")
        self.bitrate_menu.pack(
            side="right",
            padx=10
        )

        # --------------------------------
        # Worker Count
        # --------------------------------
        workers_frame = ctk.CTkFrame(self)
        workers_frame.pack(
            fill="x",
            padx=10,
            pady=5
        )

        ctk.CTkLabel(
            workers_frame,
            text="Download Workers"
        ).pack(
            side="left",
            padx=10
        )

        cpu_count = multiprocessing.cpu_count()

        self.worker_menu = ctk.CTkOptionMenu(
            workers_frame,
            values=[
                str(i)
                for i in range(
                    1,
                    cpu_count + 1
                )
            ]
        )

        self.worker_menu.set(
            str(
                min(
                    4,
                    cpu_count
                )
            )
        )

        self.worker_menu.pack(
            side="right",
            padx=10
        )

        # --------------------------------
        # Automatic CSV Export
        # --------------------------------
        self.export_csv_var = ctk.BooleanVar(
            value=True
        )

        self.export_checkbox = ctk.CTkCheckBox(
            self,
            text="Automatically export playlists to CSV",
            variable=self.export_csv_var
        )

        self.export_checkbox.pack(
            anchor="w",
            padx=20,
            pady=5
        )

        # --------------------------------
        # Duplicate Removal
        # --------------------------------
        self.remove_duplicates_var = ctk.BooleanVar(
            value=False
        )

        self.duplicate_checkbox = ctk.CTkCheckBox(
            self,
            text="Automatically remove duplicates",
            variable=self.remove_duplicates_var
        )

        self.duplicate_checkbox.pack(
            anchor="w",
            padx=20,
            pady=5
        )

        # --------------------------------
        # AI Features
        # --------------------------------
        self.ai_enabled_var = ctk.BooleanVar(
            value=True
        )

        self.ai_checkbox = ctk.CTkCheckBox(
            self,
            text="Enable AI playlist recommendations",
            variable=self.ai_enabled_var
        )

        self.ai_checkbox.pack(
            anchor="w",
            padx=20,
            pady=5
        )

        # --------------------------------
        # Appearance Mode
        # --------------------------------
        theme_frame = ctk.CTkFrame(self)
        theme_frame.pack(
            fill="x",
            padx=10,
            pady=5
        )

        ctk.CTkLabel(
            theme_frame,
            text="Appearance"
        ).pack(
            side="left",
            padx=10
        )

        self.theme_menu = ctk.CTkOptionMenu(
            theme_frame,
            values=[
                "System",
                "Dark",
                "Light"
            ],
            command=self.change_theme
        )

        self.theme_menu.set("System")

        self.theme_menu.pack(
            side="right",
            padx=10
        )

    # --------------------------------
    # Folder selection
    # --------------------------------
    def select_folder(self):

        folder = filedialog.askdirectory()

        if folder:
            self.download_folder = folder

            self.folder_label.configure(
                text=folder
            )

    # --------------------------------
    # Theme switch
    # --------------------------------
    def change_theme(
        self,
        mode
    ):
        ctk.set_appearance_mode(
            mode
        )

    # --------------------------------
    # Return settings
    # --------------------------------
    def get_settings(self):

        return {
            "download_folder":
                self.download_folder,

            "format":
                self.format_menu.get(),

            "bitrate":
                self.bitrate_menu.get(),

            "workers":
                int(
                    self.worker_menu.get()
                ),

            "export_csv":
                self.export_csv_var.get(),

            "remove_duplicates":
                self.remove_duplicates_var.get(),

            "ai_enabled":
                self.ai_enabled_var.get(),

            "theme":
                self.theme_menu.get()
        }