NAME="join.py"
AUTHOR="Osiris"
VERSION=".1"
LICENSE="GPL2"

import weechat

weechat.register(NAME, AUTHOR, VERSION, LICENSE, "Joins my favorite channels", "",  "")
myChannelFile = open("/root/.weechat/python/myChannelList.txt", "r")
for channel in myChannelFile:
    buffer = weechat.info_get("irc_buffer", "freenode,#weechat")
    weechat.command(buffer, "/join " +  channel)
