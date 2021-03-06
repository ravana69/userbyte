# Copyright (C) 2020 by Team Devcode(Ayan Ansari, Adnan Ahmad) < https://github.com/DevcodeOfficial >.
#
# This file is part of project < https://github.com/DevcodeOfficial/UserByte > 
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/DevcodeOfficial/UserByte/blob/master/LICENSE >
#
# All rights reserved.

import pyrogram, time, os
from pyrogram import Client, Filters
from pyrogram.api import functions
from userbyte import byte, cmd, set_help
from userbyte.helpers.loader import progress_for_pyrogram
timesleep = 1
from datetime import datetime
thumb_image_path = "./DOWNLOADS/thumb.jpg"

set_help('upload', '⬆️ **Upload Files From Server\n\n👉 Command :** `.upload (file path | url)`\n\n👉 **Example :** `.upload ./DOWNLOADS/test.mp4`\n\n👉 **Example2 :** `.upload https://speed.hetzner.de/100MB.bin`')

@byte.on_message(Filters.command(["upload"], cmd) & Filters.me)
async def telegram_upload(client, message):
      msg = await message.edit("Processing ...")
      fname = message.text[8:]
      print(fname)
      thumb = None
      if os.path.exists(thumb_image_path):
         thumb = thumb_image_path
      if os.path.exists(fname):
         start = datetime.now()
         c_time = time.time()
         await message.reply_document(
               document=fname,
               quote=True,
               thumb=thumb,
               parse_mode="HTML",
               progress=progress_for_pyrogram,
               progress_args=(
                    msg,c_time, "Uploading... "
                )
         )
         end = datetime.now()
         ms = (end - start).seconds
         await msg.edit("Uploaded in {} seconds.".format(ms))
      else:
           await msg.edit("404: File Not Found")
           time.sleep(5)
           await msg.delete()
