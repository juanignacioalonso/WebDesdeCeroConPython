import reflex as rx
import link_bio.styles.styles as styles
from link_bio.pages.index import index
from link_bio.pages.courses import courses


class State(rx.State):
    """Define your app state here."""  
    

app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLES
)

app.add_page(index, route="/")
app.add_page(courses, route="/courses")