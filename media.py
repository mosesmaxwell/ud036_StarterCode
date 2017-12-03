"""This module will create movie class for trailer website"""

import webbrowser


class Movie():
    """Movie class for creating movie trailer list"""

    # initialize movie object
    def __init__(self, movie_title, plot, poster_image_url, trailer_youtube_url):
        self.title = movie_title
        self.plot = plot
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        #self.year = "2017"
        #self.starring = "Actors"

    # open tailer video
    def show_trailer(self):
        """open tailer video popup using webbrowser open method"""
        webbrowser.open(self.trailer_youtube_url)
