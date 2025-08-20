import reflex as rx
from link_bio.components.navbar import navbar
from link_bio.components.footer import footer
from link_bio.views.header.header import header
from link_bio.views.links.links import links
from link_bio.views.sponsors.sponsors import sponsors
import link_bio.styles.styles as styles
from link_bio.styles.styles import Size as Size

class State(rx.State):
    pass

def index()-> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                links(),
                sponsors(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=Size.BIG.value,
                padding=Size.BIG.value,
            )
        ),
        footer(),
    )
    
    

app = rx.App(
    style=styles.BASE_STYLES
)
app.add_page(
    index,
    title="Juan Ignacio Alonso - Desarrollador Full stack",
    description= "Hola mi nombre es Juan Ignacio Alonso hace 5 años que soy desarrollador web freelancer."
)
