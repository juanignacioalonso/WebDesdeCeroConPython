import reflex as rx
import link_bio.styles.styles as styles
import link_bio.constants as c
from link_bio.pages.index import index
from link_bio.pages.courses import courses
from link_bio.api.api import fastapi_app

from link_bio.api.api import repo, live



    
app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLES,
    api_transformer=fastapi_app,
    head_components=[
        rx.script(
            src=f"https://www.googletagmanager.com/gtag/js?id={c.G_TAG}"),
        rx.script(
            f"""
window.dataLayer = window.dataLayer || [];
function gtag(){{dataLayer.push(arguments);}}
gtag('js', new Date());
gtag('config', '{c.G_TAG}');
"""
        ),
    ],
)

