import reflex as rx
from link_bio.components.link_button import link_button
from link_bio.components.title import title

def links() -> rx.Component:
    return rx.vstack(
        title(
            "Comunidad"
            ),
        link_button(
            "Twich",
            "Directos de lunes a viernes",
            "https://twich.tx/mouredev"
            ),
        link_button(
            "YouTube",
            "Tutoriales semanales",
            "https://youtube.com/@mouredev"
            ),
        link_button(
            "YouTube (canal secundario)",
            "Tutoriales semanales",
            "https://youtube.com/@mouredevtv"
            ),
        link_button(
            "Discord",
            "El chat de la comunidad",
            "https://discord.gg/mouredev"
            ),
        title(
            "Comunidad"
            ),
        link_button(
            "Twich",
            "Directos de lunes a viernes",
            "https://twich.tx/mouredev"
            ),
        link_button(
            "YouTube",
            "Tutoriales semanales",
            "https://youtube.com/@mouredev"
            ),
        link_button(
            "YouTube (canal secundario)",
            "Tutoriales semanales",
            "https://youtube.com/@mouredevtv"
            ),
        link_button(
            "Discord",
            "El chat de la comunidad",
            "https://discord.gg/mouredev"
            ),
        width="100%",
    )