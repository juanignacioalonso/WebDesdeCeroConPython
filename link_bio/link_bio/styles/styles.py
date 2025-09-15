import reflex as rx
from enum import Enum
from .colors import Color as Colors
from .colors import TextColor as TextColors
from .fonts import Font , FontWeight

#Seteamos los estilos de la aplicacion, para que los cambios se apliquen en todos los componentes que lo necesiten.

# Constants
MAX_WIDTH = "560PX"

# Sizes 

STYLESHEETS = [
    'https://fonts.googleapis.com/css2?family=Poppins:wght@300;500&display=swap',
    'https://fonts.googleapis.com/css2?family=Comfortaa:wght@500&display=swap'
]

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
    "font_family": Font.DEFAULT.value,
    "font_weigth": FontWeight.LIGHT.value,
    "background_color": Colors.BACKGROUND.value,
    rx.heading:{
        "color":TextColors.HEADER.value,
        "font_family": Font.TITLE.value,
        "font_weigth": FontWeight.MEDIUM.value,
    },
    rx.button:{
        "width":"100%",
        "height":"100%",
        "padding": Size.SMALL.value,
        "borderRadius":10,
        "color": TextColors.HEADER.value,
        "background_color": Colors.CONTENT.value,
        "white_space": "normal",
        "display": "flex",
        "justify-content": "flex-start",
        "align-items": "center",
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
    fontFamily=Font.LOGO.value,
    font_weigth= FontWeight.MEDIUM.value,
    font_size=Size.LARGE.value,
)

title_style = dict(
    width="100%",
    size="6",
    padding=Size.DEFAULT.value,
)

button_title_style = dict (
    fontFamily=Font.TITLE.value,
    font_weigth= FontWeight.MEDIUM.value,
    fontSize=Size.DEFAULT.value,
    color=TextColors.HEADER.value,
)

button_body_style = dict (
    fontSize=Size.MEDIUM.value,
    font_weigth= FontWeight.LIGHT.value,
    color=TextColors.BODY.value,
)
