import reflex as rx
import link_bio.styles.styles as styles
from link_bio.pages.index import index
from link_bio.pages.courses import courses
from link_bio.api.api import fastapi_app

from link_bio.api.api import repo, live



    

app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLES,
    api_transformer=fastapi_app,
)

app.add_page(index, route="/")
app.add_page(courses, route="/courses")

app._api.add_route("/repo", repo, methods=["GET"])
app._api.add_route("/live/{user}", live, methods=["GET"])