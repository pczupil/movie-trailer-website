"""media - Used to create and store miscellaneous data about movies and shows"""

import webbrowser

class Video(object):
    """ Video - Abstract class used for Movie and TVshow

    Attributes:
        title     (str): The movie's title
        storyline (str): A brief description of the film's plot
        director  (str): The video's director
    """
    def __init__(self, video_attr_list):
        self.title     = video_attr_list[0]
        self.storyline = video_attr_list[1]
        self.director  = video_attr_list[2]

class Movie(Video):
    """ Movie - Used to represent a film

    Attributes:
        title               (str): The movie's title
        storyline           (str): A brief description of the film's plot
        director            (str): The video's director
        poster_image_url    (str): Specifies the location of the movie's
                                   promotional image.
        trailer_youtube_url (str): Specifies the location of the movie's
                                   promotional trailer.
    """

    def __init__(self, movie_attr_list):
        super(Movie, self).__init__(movie_attr_list[:3])
        self.poster_image_url    = movie_attr_list[3]
        self.trailer_youtube_url = movie_attr_list[4]

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



class TVshow(Video):
    """ TVshow - Used to represent an episode from a television show

    Attributes:
        title     (str): The show's title
        storyline (str): A brief description of the show's plot
        director  (str): The video's director
        episode   (str): The video's episode number
    """
    def __init__(self, show_attr_list):
        super(TVshow, self).__init__(self, show_attr_list[:3])
        self.episode = show_attr_list[3]
