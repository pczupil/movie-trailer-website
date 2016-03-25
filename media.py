"""media - Only contains the Movie class """

import webbrowser

class Movie(object):
    """ Movie - Used to represent a film

    Attributes:
        title               (str): The movie's title
        storyline           (str): A brief description of the film's plot
        poster_image_url    (str): Specifies the location of the movie's
                               promotional image.
        trailer_youtube_url (str): Specifies the location of the movie's
                               promotional trailer.
        director             (str): The video's director
    """
    def __init__(self, video_attr_list):
        self.title = video_attr_list[0]
        self.storyline = video_attr_list[1]
        self.poster_image_url = video_attr_list[2]
        self.trailer_youtube_url = video_attr_list[3]
        self.director = video_attr_list[4]

    def __cmp__(self, other):
        if self.title < other.title:
            return -1
        elif self.title == other.title:
            return 0
        else:
            return 1

    def play_movie_trailer(self):
        """ play_movie_trailer - opens a web browser to play a movie trailer"""
        webbrowser.open(self.trailer_youtube_url, new=2)

    def show_image(self):
        """ show_image - displays movie image in browser """
        webbrowser.open(self.poster_image_url, new=2)
