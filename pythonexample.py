# pythonexample.py

import znc

class pythonexample(znc.Module):
    description = "Example python3 module for ZNC"

    def OnChanMsg(self, nick, channel, message):
        self.PutModule("Hey, {0} said {1} on {2}".format(nick.GetNick(), message.s, channel.GetName()))
        return znc.CONTINUE