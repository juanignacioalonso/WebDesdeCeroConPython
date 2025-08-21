import reflex as rx
import link_bio.styles.styles as styles
from link_bio.styles.styles import Size

def link_sponsor(imagen: str, url:str, alt:str) -> rx.Component:
    return rx.link(
        rx.image(
            src=imagen,
            height=Size.BIG.value,
            width="auto",
            alt = alt
        ),
        href=url,
        is_external=True,
    )