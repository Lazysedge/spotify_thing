import customtkinter as ctk


def create_section_label(
    parent,
    text
):
    label = ctk.CTkLabel(
        parent,
        text=text,
        font=(
            "Arial",
            18,
            "bold"
        )
    )

    return label