import reflex as rx
from enum import Enum
from .colors import Color as Colors
from .colors import TextColor as TextColors
from .fonts import Font as Fonts

#Seteamos los estilos de la aplicacion, para que los cambios se apliquen en todos los componentes que lo necesiten.

# Constants
MAX_WIDTH = "600PX"

# Sizes 

# 0.5em = 8px, 1em = 16px,  2em = 32px  em  mantiene el espacio relativo al tamaño de la fuente del elemento padre

class Size(Enum):
    ZERO ="0px !important"
    SMALL = "0.5em"
    MEDIUM = "0.8em"
    DEFAULT = "1em"
    LARGE =  "1.5em"
    BIG = "2em"

# Styles

BASE_STYLES = {
    "font_family": Fonts.DEFAULT.value,
    "background_color": Colors.BACKGROUND.value,
    rx.heading:{
        "color":TextColors.HEADER.value,
        "font_family": Fonts.TITLE.value,
    },
    rx.button:{
        "width":"100%",
        "height":"100%",
        "display":"block",
        "padding": Size.SMALL.value,
        "border_radius":Size.DEFAULT.value,
        "color": TextColors.HEADER.value,
        "background_color": Colors.CONTENT.value,
        "_hover": {
            "background_color": Colors.SECUNDARY.value,
        }
    },
    rx.link : { 
        "text_decoration":"none",
        "_hover": {}
    },

}

navbar_title_style = dict(
    fontFamily=Fonts.LOGO.value,
    font_size=Size.LARGE.value,
)

title_style = dict(
    width="100%",
    size="6",
    padding=Size.DEFAULT.value,
)

button_title_style = dict (
    fontFamily=Fonts.TITLE.value,
    fontSize=Size.DEFAULT.value,
    color=TextColors.HEADER.value,
)

button_body_style = dict (
    fontSize=Size.MEDIUM.value,
    color=TextColors.BODY.value,
)
