import reflex as rx
import datetime
import link_bio.constants as c
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import TextColor as TextColors


def footer() -> rx.Component:
    return rx.vstack(
        rx.image(
            src="logo.png",
            heigth="auto",
            width="300px",
            align_self="center",
            ),
        rx.link(
            f"2021-{datetime.date.today().year} DESARROLLADOR PYTHON",
            href=c.GIT_URL,
            is_external=True,
            fontSize=Size.MEDIUM.value,
            align_self="center",
            ),
        rx.text("Powered by Reflex",
                fontSize=Size.MEDIUM.value,
                align_self="center",
                marginTop=Size.ZERO.value,
                ),
        marginBottom=Size.BIG.value,
        padding_bottom=Size.MEDIUM.value,
        color=TextColors.FOOTER.value,
    )