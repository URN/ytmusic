import json

import ytmusicapi
from tornado.web import RequestHandler

yt = ytmusicapi.YTMusic()

class YTSearchHandler(RequestHandler):
    def __init__(self, application, request, **kwargs):
        # cache yt object
        global yt

        super().__init__(application, request, **kwargs)
        self.yt = yt

    def prepare(self):
        header = "Content-Type"
        body = "application/json"
        self.set_header(header, body)

    def get(self, searched_term):
        r = self.yt.search(searched_term, "songs")
        self.write(json.dumps(r))