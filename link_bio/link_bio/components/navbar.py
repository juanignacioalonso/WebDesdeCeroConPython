import reflex as rx
import link_bio.styles.styles as styles
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import TextColor as TextColors
from link_bio.styles.colors import Color as Colors

def navbar() -> rx.Component:
    return rx.hstack(
        rx.text(
            rx.text(
                rx.text.strong("juan"),
                 "dev",
                as_="span",
                ),
                color=Colors.PRIMARY.value,
                style=styles.navbar_title_style,
            ),

        position="sticky",
        bg=Colors.CONTENT.value,
        padding_x=Size.BIG.value,
        padding_y=Size.DEFAULT.value,
        z_index="999",
        top="0",
    )
