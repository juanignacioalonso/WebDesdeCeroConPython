import reflex as rx
import datetime
from link_bio.styles.styles import Size as Size


def footer() -> rx.Component:
    return rx.vstack(
        rx.image(
            src="/favicon.ico",
            align_self="center",
            ),
        rx.link(
            f"2021-{datetime.date.today().year} DESARROLLADOR PYTHON",
            href="https://mouredev.com",
            is_external=True,
            fontSize=Size.MEDIUM.value,
            align_self="center",
            ),
        rx.text("Powered by Reflex",
                fontSize=Size.MEDIUM.value,
                align_self="center",
                marginTop="0px !important",
                ),
        marginBottom=Size.BIG.value,
    )