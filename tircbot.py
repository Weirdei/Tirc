#tircbot module for znc

#import znc
import json


highlighted_file = 'teleirc.db'

class tircbot():
    desciption = "ZNC module for telegram bot"

# On init we need only API key to send messages to telegram bot

    def __init__(self, api_key):
        self.api_key = api_key
        self.highlightedList = self.getHighlightedList()


    def OnChanMsg(self, Nick, Channel, sMessage):

        if sMessage in self.highlightedList:
            pass
            # send message to proper channel and highlight it
        else:
            # just forward to proper telegram channel
            pass

    def  getHighlightedList(self):

        with open(highlighted_file, 'r') as f:
            return f.read()
        # here we will get the list of hl strings to compare

    def addHighlightedString(self):
        # add some strings to db
        pass

    def receiver(self):
        pass

        # here we will be listening on messages we need to forward

