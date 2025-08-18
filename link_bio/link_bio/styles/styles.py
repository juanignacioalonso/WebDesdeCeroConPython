import reflex as rx
from enum import Enum

#Seteamos los estilos de la aplicacion, para que los cambios se apliquen en todos los componentes que lo necesiten.

# Constants
MAX_WIDTH = "600PX"

# Sizes 

# 0.5em = 8px, 1em = 16px,  2em = 32px  em  mantiene el espacio relativo al tamaño de la fuente del elemento padre

class Size(Enum):
    SMALL = "0.5em"
    MEDIUM = "0.8em"
    DEFAULT = "1em"
    BIG = "2em"

# Styles

BASE_STYLES = {
    rx.button:{
        "width":"100%",
        "height":"100%",
        "display":"block",
        "padding": Size.SMALL.value,
        "border_radius":Size.DEFAULT.value,
    },
    rx.link : { 
        "text_decoration":"none",
        "_hover": {}
    },

}

title_style = dict(
    width="100%",
    padding_top=Size.DEFAULT.value,
)

button_title_style = dict (
    fontSize=Size.DEFAULT.value,
)

button_body_style = dict (
    fontSize=Size.MEDIUM.value,
)
