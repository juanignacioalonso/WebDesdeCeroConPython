import reflex as rx

def header() -> rx.Component:
    return rx.vstack(
        rx.avatar(src="/logo.jpg",fallback="JI", variant="solid", size="7"),
        rx.text("@juandev"),
        rx.text("Hola mi nombre es Juan Ignacio y soy tu papito"),
        rx.text("""Desarrollador Full Stack con experiencia en Python 
                (Django) y Angular, orientado a la creación de soluciones 
                escalables y eficientes. Cuento con sólidos conocimientos en 
                bases de datos relacionales y no relacionales, despliegue en la nube (AWS) 
                y metodologías ágiles. Con capacidad para desempeñarme también en roles de soporte técnico.
                Busco integrarme a equipos dinámicos con enfoque en calidad, buenas prácticas y resultados."""),
    )