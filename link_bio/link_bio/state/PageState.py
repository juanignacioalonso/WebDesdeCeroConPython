import reflex as rx
import link_bio.utils as utils
from link_bio.api.api import  featured
from link_bio.model.Featured import Featured


USER = "mouredev"


class PageState(rx.State):

    featured_info: list[Featured]


    async def featured_links(self):
        self.featured_info = await featured()
        