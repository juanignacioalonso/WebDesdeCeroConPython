import reflex as rx
import link_bio.utils as utils
from link_bio.routes import Route
from link_bio.components.navbar import navbar
from link_bio.components.footer import footer
from link_bio.views.header import header
from link_bio.views.courses_links import courses_links
from link_bio.views.sponsors import sponsors
import link_bio.styles.styles as styles
from link_bio.styles.styles import Size as Size


@rx.page(
        route=Route.COURSES.value,
        title=utils.curses_title,
        description= utils.curses_description,
        image=utils.preview,
        meta=utils.curses_meta
      
)
def courses()-> rx.Component:
    return rx.box(
        navbar(),
        utils.lang(),
        rx.center(
            rx.vstack(
                header(details=False),
                courses_links(),
                sponsors(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=Size.BIG.value,
                padding=Size.BIG.value,
            )
        ),
        footer(),
    )


