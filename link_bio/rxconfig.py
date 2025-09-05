import reflex as rx

config = rx.Config(
    app_name="link_bio",
    antd_mode=True,
    cors_allowed_origins = [
        "http://localhost:3000",
        "https://www.juandev.lat"
        "https://api.juandev.lat"
        "http://localhost:8000/"

    ],
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ],
)