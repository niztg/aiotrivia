"""
HTTPClient based on IDutchy's sr_api HTTPCient
Protected by the MIT License
Copyright (c) 2019 iDutchy
https://github.com/iDutchy/sr_api/blob/d7921c1ea886ab7df12cfea0d9e71dcfc2bb8b67/sr_api/http.py#L4
"""
import aiohttp


class HTTPClient:
    def __init__(self):
        self.session = aiohttp.ClientSession()
        self.url = 'https://opentdb.com/api.php'
