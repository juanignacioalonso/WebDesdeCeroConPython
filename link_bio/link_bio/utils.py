import reflex as rx

# Comun

def lang() -> rx.Component:
    return rx.script("document.documentElement.lang='es'")

preview = ""

_meta=[
        {"name": "og:type","content":"website"},
        {"name": "og:image","content":preview},
        {"name": "twitter:card","content":"summary_large_image"},
        {"name": "twitter:card","content":"@igna32365"},
    ]

# Index


index_title = "Juan Ignacio Alonso - Desarrollador Full stack"
index_description= "Hola mi nombre es Juan Ignacio Alonso hace 5 años que soy desarrollador web freelancer."

index_meta = [
    {"name": "og:title","content":index_title},
    {"name": "og:description","content":index_description},
]

index_meta.extend(_meta)

# Cursos

curses_title = "JuanDev - Cursos Gratis"
curses_description= "Este es el listados de mis cursos."

curses_meta = [
    {"name": "og:title","content":curses_title},
    {"name": "og:description","content":curses_description},
]

curses_meta.extend(_meta)

