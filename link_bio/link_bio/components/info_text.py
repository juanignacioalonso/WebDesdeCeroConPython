import reflex as rx
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import Color as Colors
from link_bio.styles.colors import TextColor as TextColors

def info_text(title:str,body:str) -> rx.Component:
    return rx.box(
        rx.text(
            title, 
            color=Colors.PRIMARY.value,
            fontWeight="bold",
        ),
        rx.text(body),
        fontSize=Size.MEDIUM.value,
        color=TextColors.BODY.value,
    )

