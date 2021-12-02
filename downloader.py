import json

from tornado.web import RequestHandler
import ytdownloader

dl = ytdownloader.YTDownloader()

class DownloadHandler(RequestHandler):
    def __init__(self, application, request, **kwargs):
        # cache yt object
        global dl

        super().__init__(application, request, **kwargs)
        self.dl = dl

    def prepare(self):
        header = "Content-Type"
        body = "application/json"
        self.set_header(header, body)

    def post(self):
        dl.add_to_queue(json.loads(self.request.body.decode('utf-8')))
        print(dl)
        self.write(json.dumps(dl.get_queue()))

    def get(self):
        self.write(json.dumps(dl.get_queue()))
    