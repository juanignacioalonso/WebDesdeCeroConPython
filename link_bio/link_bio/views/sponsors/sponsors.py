import reflex as rx
import link_bio.constants as c
from link_bio.components.title import title
from link_bio.components.link_sponsor import link_sponsor


def sponsors() -> rx.Component:
    return rx.vstack(
        title("Colaboran"),
        rx.hstack(
            link_sponsor(
                "elgato.png",
                c.ELGATO_URL,
                "Logotipo de el Gato"
            ),
            link_sponsor(
                "compragamer.png",
                c.COMPRAGAMER_URL,
                "Logotipo de Compra Gamer"
            ),
            spacing='9'
        ),
        width = "100%",
        alingItems = "start"
    )