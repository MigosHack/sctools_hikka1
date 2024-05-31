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
        """Decode SC""" 
        print("динаху декодим ск") 
        await message.edit("dudka technolog(decodesc)") 
 
        # эм чо ну типо асунк селф таскс чето там вообще 
 
    async def png2sccmd(self, message): 
        """Encode SC""" 
        print("динаху енкодим ск") 
        await message.edt("dudkaaaaaa(encode sc)") 
 
    async def mp42sccmd(self, message): 
        """Сделать SC из MP4, GIF""" 
        while True: 
            print("ааа коляски") 
 
            continue
