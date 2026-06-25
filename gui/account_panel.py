import customtkinter as ctk


class AccountPanel(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)

        self.username_label = ctk.CTkLabel(
            self,
            text="Not logged in",
            font=("Arial", 20, "bold")
        )

        self.username_label.pack(
            pady=10
        )

        self.spotify_id_label = ctk.CTkLabel(
            self,
            text=""
        )

        self.spotify_id_label.pack()

        self.product_label = ctk.CTkLabel(
            self,
            text=""
        )

        self.product_label.pack()

    def update_user(self, user):

        self.username_label.configure(
            text=user.get(
                "display_name",
                "Unknown User"
            )
        )

        self.spotify_id_label.configure(
            text=f"Spotify ID: {user.get('id')}"
        )

        self.product_label.configure(
            text=f"Plan: {user.get('product', 'Unknown')}"
        )