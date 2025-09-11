import reflex as rx
from link_bio.api.api import feactured


class PageState(rx.State):

    feactured_info:list

    async def feactured_links(self):
        self.feactured_info = await feactured()