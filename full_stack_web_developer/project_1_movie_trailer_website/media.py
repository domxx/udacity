class Movie(object):
    """Class containing all movie information."""
    def __init__(self, title, poster_url, yt_url):
        self.title = title
        self.poster_image_url = poster_url
        self.trailer_youtube_url = yt_url
