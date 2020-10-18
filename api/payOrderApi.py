from py import log

import config


class PayOrder:
    def __init__(self):
        self.url =config.JUMP_URL
        log.info(f'self.url的值是{self.url}')