import reflex as rx
from link_bio.components.link_icon import link_icon
from link_bio.components.info_text import info_text
from link_bio.components.title import title
from link_bio.styles.colors import TextColor as TextColors
from link_bio.styles.colors import Color as Colors
from link_bio.styles.styles import Size as Size
from link_bio import constants as c

cards_data = [
    {"title": "+4", "body": "Años de experiencia"},
    {"title": "+10", "body": "Proyectos completados"},
    {"title": "+3", "body": "Certificaciones"},
]

def header(details = True) -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
                src="Juan.jpeg",
                fallback="JI", 
                size="7",
                color=TextColors.BODY.value,
                bg=Colors.CONTENT.value,
                padding="2px",
                border="4px",
                borderColor=Colors.PRIMARY.value,
                ),
            rx.vstack(
                rx.heading(
                    "Juan Ignacio Alonso",
                    size="6",
                    ),
                rx.text(
                    "@juandev",
                    marginTop=Size.ZERO.value,
                    color = TextColors.BODY.value,
                ),
                rx.hstack(
                    link_icon(
                        "/icons/whatsapp.svg",
                        c.WHATSAPP,
                        "GitHub"
                        ),
                    link_icon(
                        "/icons/linkedin2.svg",
                        c.LINKEDIN_URL,
                        "Linkeding"
                        ),
                    link_icon(
                        "/icons/discord2.svg",
                        c.DISCORD_URL,
                        "Discord"
                        ),
                ),
                alignItems="Start",
            ),
            spacing="7",
        ),
        rx.cond(
            details,
            rx.vstack(
                rx.flex(
                    rx.foreach(
                        cards_data,  # 👈 ahora recorre la lista de diccionarios
                        lambda item: rx.card(
                            info_text(item["title"], item["body"]), 
                            width="30%",
                        ),
                    ),
                    spacing="3",
                    flex_wrap="wrap",
                    width="100%",
                ),

                rx.text(
                        """
                        Desarrollador Full Stack con experiencia en Python 
                        (Django) y Angular, orientado a la creación de soluciones 
                        escalables y eficientes. Cuento con sólidos conocimientos en 
                        bases de datos relacionales y no relacionales, despliegue en la nube (AWS) 
                        y metodologías ágiles. Con capacidad para desempeñarme también en roles de soporte técnico.
                        Busco integrarme a equipos dinámicos con enfoque en calidad, buenas prácticas y resultados.
                        """,
                        color=TextColors.BODY.value,
                        font_size=Size.MEDIUM.value,
                        )
            ),

        ),
        spacing="6",
        alignItems="Start",
    )