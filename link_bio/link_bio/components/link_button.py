import reflex as rx
import link_bio.styles.styles as styles
from link_bio.styles.styles import Size

def link_button(title:str, body:str, image: str, url:str ) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
               rx.image(
                   src=image,
                   width=styles.Size.BIG.value,
                   heigth=styles.Size.BIG.value,
                   margin=Size.MEDIUM.value,
               ),
               rx.vstack(
                   rx.text(title, style=styles.button_title_style),
                   rx.text(body, style=styles.button_body_style), 
                   spacing="2",
                   align_items="start",
                   margin=Size.ZERO.value,
               ),
                spacing="4",
            )
        ),
        href=url,
        is_external=True,
        width="100%",
        
    )

