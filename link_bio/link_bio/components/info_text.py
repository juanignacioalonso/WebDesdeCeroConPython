import reflex as rx
from link_bio.styles.styles import Size as Size

def info_text(title:str,body:str) -> rx.Component:
    return rx.box(
        rx.text(
            title, 
            color="blue",
            fontWeight="bold",
        ),
        rx.text(body),
        fontSize=Size.MEDIUM.value,
    )

