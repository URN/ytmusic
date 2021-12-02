import tornado.ioloop
import tornado.web

import ytsearch
import downloader


def make_app():
    return tornado.web.Application([
        (r"/search/(.+)", ytsearch.YTSearchHandler),
        ("/downloader", downloader.DownloadHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()