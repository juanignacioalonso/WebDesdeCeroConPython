import reflex as rx

config = rx.Config(
    app_name="link_bio",
    antd_mode=True,
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ],
)