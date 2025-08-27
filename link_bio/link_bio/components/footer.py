import reflex as rx
import datetime
import link_bio.constants as c
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import TextColor as TextColors


def footer() -> rx.Component:
    return rx.vstack(
        rx.image(
            src="/logo.png",
            heigth="auto",
            width="200px",
            align_self="center",
            alt="Logotipo de MaJu Automatizaciones "
            ),

        rx.link(
            f"2021-{datetime.date.today().year} DESARROLLADOR PYTHON",
            href=c.GIT_URL,
            is_external=True,
            fontSize=Size.MEDIUM.value,
            align_self="center",
            ),
        rx.hstack(
            rx.link(
                rx.image(
                    src="/icons/github2.svg",
                    heigth="auto",
                    width="30px",
                    align_self="center",
                ),
                href= c.GIT_URL_CABECERA,
                is_external=True,
                
            ),
            rx.text("Repositorio del proyecto",
            fontSize=Size.MEDIUM.value,
            align_self="center",
            marginTop=Size.ZERO.value,
            ),
            align_self="center",
        ),
        

        marginBottom=Size.BIG.value,
        padding_bottom=Size.MEDIUM.value,
        padding_x=Size.BIG.value,
        color=TextColors.FOOTER.value,
    )