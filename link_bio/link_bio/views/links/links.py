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
            "icons/twitch.svg",
            c.TWITCH_URL
            ),
        link_button(
            "YouTube",
            "Tutoriales semanales",
            "icons/youtube1.svg",
            c.YOUTUBE_URL
            ),
        link_button(
            "YouTube (canal secundario)",
            "Tutoriales semanales",
            "icons/square-youtube-brands-solid-full.svg",
            c.YOUTUBE_SECONDARY_URL
            ),
        link_button(
            "Discord",
            "El chat de la comunidad",
            "icons/discord2.svg",
            c.DISCORD_URL
            ),
        title(
            "Recursos y más"
            ),
        link_button(
            "Git y GitHub desde cero",
            "Aqui puedes comprar mis libros fisicos",
            "icons/github2.svg",
            c.GIT_URL
            ),
        link_button(
            "Paginas de compras para tu setup",
            "Compra Gamer",
            "icons/minimize-solid-full.svg",
            c.COMPRAGAMER_URL
            ),
        link_button(
            "Mi linkeding",
            "Mi desarrollo profesional",
            "icons/linkedin2.svg",
            c.LINKEDIN_URL
            ),
        link_button(
            "Mis cursos en Udemy",
            "Mis cursos de desarrollo",
            "icons/book.svg",
            c.UDEMY_URL
            ),
        title(
            "Contacto"
            ),
        link_button(
            "Email",
            c.EMAIL_URL,
            "icons/envelope-solid-full.svg",
            f"Juan Alonso - {c.EMAIL_URL}"
            ),
        width="100%",
        spacing="4",
    )