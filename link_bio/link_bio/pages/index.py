import reflex as rx
import link_bio.utils as utils
from link_bio.components.navbar import navbar
from link_bio.components.footer import footer
from link_bio.views.header import header
from link_bio.views.index_links import index_links
from link_bio.views.sponsors import sponsors
import link_bio.styles.styles as styles
from link_bio.styles.styles import Size as Size
from link_bio.api.api import repo
from link_bio.state.PageState import PageState

class IndexState(rx.State):
    pass



@rx.page(
        title=utils.index_title,
        description= utils.index_description,
        image=utils.preview,
        meta=utils.index_meta,
        on_load=[PageState.feactured_links]
      
)
def index()-> rx.Component:
    return rx.box(
        navbar(),
        utils.lang(),
        rx.center(
            rx.vstack(
                header(),
                index_links(PageState.feactured_info),
                sponsors(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=Size.BIG.value,
                padding=Size.BIG.value,
            )
        ),
        footer(),
    )


