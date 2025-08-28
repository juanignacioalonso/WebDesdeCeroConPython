import reflex as rx
from link_bio.styles.colors import Color

class FloatButton(rx.Component):
    library = "antd"
    tag = "FloatButton"
    icon: rx.Var[rx.Component]
    href: rx.Var[str]
    target: rx.Var[str] = "_blank"
    badge: rx.Var[dict] = {"dot": True, "color": Color.PRIMARY.value}
    
    # Propiedades opcionales con valores por defecto
    tooltip: rx.Var[str] = "Botón flotante"
    type: rx.Var[str] = "primary"
    shape: rx.Var[str] = "circle"
    style: rx.Var[dict] = {"right": "24px", "bottom": "24px"}

# Crear la instancia del componente
float_button = FloatButton.create