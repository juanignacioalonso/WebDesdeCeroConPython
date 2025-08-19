import reflex as rx
from link_bio.components.link_button import link_button
from link_bio.components.title import title
from link_bio import constants as c
def links() -> rx.Component:
    return rx.vstack(
        title(
            "Comunidad"
            ),
        link_button(
            "Twitch",
            "Directos de lunes a viernes",
            c.TWITCH_URL
            ),
        link_button(
            "YouTube",
            "Tutoriales semanales",
            c.YOUTUBE_URL
            ),
        link_button(
            "YouTube (canal secundario)",
            "Tutoriales semanales",
            c.YOUTUBE_SECONDARY_URL
            ),
        link_button(
            "Discord",
            "El chat de la comunidad",
            c.DISCORD_URL
            ),
        title(
            "Recursos y más"
            ),
        link_button(
            "Git y GitHub desde cero",
            "Aqui puedes comprar mis libros fisicos",
            c.GIT_URL
            ),
        link_button(
            "Paginas de compras para tu setup",
            "Compra Gamer",
            c.COMPRAGAMER_URL
            ),
        link_button(
            "Mi linkeding",
            "Mi desarrollo profesional",
            c.LINKEDIN_URL
            ),
        link_button(
            "Mis cursos en Udemy",
            "Mis cursos de desarrollo",
            c.UDEMY_URL
            ),
        title(
            "Contacto"
            ),
        link_button(
            "Email",
            c.EMAIL_URL,
            f"Juan Alonso - {c.EMAIL_URL}"
            ),
        width="100%",
        spacing="4",
    )