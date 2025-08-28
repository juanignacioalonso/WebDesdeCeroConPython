import reflex as rx
from link_bio.routes import Route
from link_bio.components.link_button import link_button
from link_bio.components.title import title
from link_bio import constants as c
def courses_links() -> rx.Component:
    return rx.vstack(
        title(
            "Cursos Gratis"
            ),
        link_button(
            "Retos de programación",
            "Ruta de estudio semanal para practica de lógica de programación",
            "/icons/cursos.svg",
            c.CODE_CHALLENGES_URL,
            is_external=False
            ),
            link_button(
            "Python desde cero",
            "Curso de +37h: Fundamentos, frontend, backend, testing...",
            "/icons/python.svg",
            c.PYTHON_COURSE_URL,
            is_external=False
            ),
            link_button(
            "Git y GitHub",
            "Curso de 5h para aprender Git y GitHub desde cero",
            "/icons/github2.svg",
            c.GIT_COURSE_URL,
            is_external=False
            ),
            link_button(
            "SQL y Bases de dato",
            "Curso de 7h desde cero para aprender los fundamentos de SQL",
            "/icons/database.svg",
            c.SQL_COURSE_URL,
            is_external=True
            ),
            title(
            "Mucho más en"
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
            "/icons/youtube1.svg",
            c.YOUTUBE_URL
            ),

        width="100%",
        spacing="4",
    )