import reflex as rx
from link_bio.components.link_button import link_button

def links() -> rx.Component:
    return rx.vstack(
        link_button("Twich","https://twich.tx/mouredev"),
        link_button("YouTube","https://youtube.com/@mouredev"),
        link_button("YouTube (canal secundario)","https://youtube.com/@mouredevtv"),
        link_button("Discord","https://discord.gg/mouredev"),
    )