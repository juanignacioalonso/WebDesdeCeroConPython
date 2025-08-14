import reflex as rx
import datetime

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(src="/favicon.ico"),
        rx.link(
            f"2021-{datetime.date.today().year} DESARROLLADOR PYTHON",
            href="https://mouredev.com",
            is_external=True,
            ),
        rx.text("Powered by Reflex"),
    )