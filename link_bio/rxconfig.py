import reflex as rx

config = rx.Config(
    app_name="link_bio",
    antd_mode=True,
    cors_allowed_origins = [
        "http://localhost:3000",
        "https://link-bio-teal-apple.reflex.run/"
    ],
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ],
)