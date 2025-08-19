import reflex as rx
from link_bio.components.link_icon import link_icon
from link_bio.components.info_text import info_text
from link_bio.components.title import title
from link_bio.styles.colors import TextColor as TextColors
from link_bio.styles.styles import Size as Size
from link_bio import constants as c

cards_data = [
    {"title": "+4", "body": "Años de experiencia"},
    {"title": "+10", "body": "Proyectos completados"},
    {"title": "+3", "body": "Certificaciones"},
]

def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(src="/logo.jpg",fallback="JI", variant="solid", size="7"),
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
                    link_icon(c.GIT_URL),
                    link_icon(c.LINKEDIN_URL),
                    link_icon(c.DISCORD_URL),
                ),
                alignItems="Start",
            ),
            spacing="7",
        ),

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
                ),
        spacing="6",
        alignItems="Start",
    )