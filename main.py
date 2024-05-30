import colorama

import os

import telethon

import asyncio





from .. import loader, utils



# developer -> @zorotexr

# developer SCTex -> @daniilsivi

# developer mp42sc -> @daniilsivi



@loader.tds

class SCToolsMod(loader.Module):

    """SCTools for Brawl Stars"""



    strings = {"name": "SCTools"}



    @loader.owner

    async def sc2pngcmd(self, message):

        await message.edit("dudka technology")
        print("syka dinaxy")
