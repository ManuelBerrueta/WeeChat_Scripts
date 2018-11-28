NAME="auth.py"
AUTHOR="Osiris"
VERSION=".1"
LICENSE="GPL2"

import weechat

weechat.register(NAME, AUTHOR, VERSION, LICENSE, "Sends message to NickServ and authenticates me", "",  "")

myTokenFile = open("/root/.weechat/python/myIrcToken.txt", "r")
myToken = myTokenFile.read()
buffer = weechat.info_get("irc_buffer", "freenode,#weechat")
weechat.command(buffer, "/msg NickServ identify " +  myToken)
