#tircbot module for znc

import znc


class Tircbot(znc.Module):
    desciption = "ZNC module for telegram bot"

    def __init__(self, api_key):
        api_key = None

