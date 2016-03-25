""" ent_center.py - Builds a movie trailer website """

import media
import fresh_tomatoes

def show_movie_site():
    """ show_movie_site - constructs list of movies and builds a website to
        display their movie trailers
    """
    # Construct list of favorite movies
    lion_king = media.Movie([
        "The Lion King",
        "A young lion Prince is cast out of his pride by his cruel uncle, who "
        "claims he killed his father.",
        "Roger Allers and Rob Minkoff",
        "https://upload.wikimedia.org/wikipedia/en/3/3d/The_Lion_King_poster.jpg", # pylint: disable=C0301
        "https://www.youtube.com/watch?v=GaJWzJfoXlE"
    ])

    shawshank_redemp = media.Movie([
        "Shawshank Redemption",
        "Andy Dufresne is sent to Shawshank Prison for the murder of his wife "
        "and her secret lover.",
        "Frank Darabont",
        "https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg", # pylint: disable=C0301
        "https://www.youtube.com/watch?v=6hB3S9bIaco"
    ])

    lotr_rotk = media.Movie([
        "The Lord of the Rings: Return of the King",
        "The War of the Ring reaches its climax as the dark lord Sauron sets "
        "his sights on Minas Tirith, the capital of Gondor.",
        "Peter Jackson",
        "https://upload.wikimedia.org/wikipedia/en/9/9d/Lord_of_the_Rings_-_The_Return_of_the_King.jpg", # pylint: disable=C0301
        "https://www.youtube.com/watch?v=r5X-hFf6Bwo"
    ])

    good_bad_ugly = media.Movie([
        "The Good, the Bad and the Ugly",
        "During the American Civil War, three men set off to find $200,000 "
        "in buried gold coins.",
        "Sergio Leone",
        "https://upload.wikimedia.org/wikipedia/en/4/45/Good_the_bad_and_the_ugly_poster.jpg", # pylint: disable=C0301
        "https://www.youtube.com/watch?v=WCN5JJY_wiA"
    ])

    the_matrix = media.Movie([
        "The Matrix",
        "A programmer is brought back to reason and reality after learning he "
        "is living in a program created by sentient machines in order to "
        "enslave humans.",
        "Lilly and Lana Wachowski",
        "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
        "https://www.youtube.com/watch?v=m8e-FF8MsqU",
    ])

    spirited_away = media.Movie([
        "Spritied Away",
        "While moving to a new home in Japan, Chihiro and her parents take a "
        "wrong turn down a mysterious wooded path.",
        "Hayao Miyazaki",
        "https://upload.wikimedia.org/wikipedia/en/3/30/Spirited_Away_poster.JPG", # pylint: disable=C0301
        "https://www.youtube.com/watch?v=ByXuk9QqQkk"
    ])

    lives_of_others = media.Movie([
        "The Lives of Others",
        "An agent working for the Stasi spies on a famous artist in East "
        "Berlin.",
        "Florian Henckel von Donnersmarck",
        "https://upload.wikimedia.org/wikipedia/en/9/9f/Leben_der_anderen.jpg",
        "https://www.youtube.com/watch?v=FppW5ml4vdw"
    ])

    mockingbird = media.Movie([
        "To Kill A Mockingbird",
        "Atticus Finch, a lawyer in the Depression-era South, defends a black "
        "man against an undeserved rape charge, and his kids against "
        "prejudice. ",
        "Robert Mulligan",
        "https://upload.wikimedia.org/wikipedia/en/8/8e/To_Kill_a_Mockingbird_poster.jpg", # pylint: disable=C0301
        "https://www.youtube.com/watch?v=KR7loA_oziY"
    ])

    holy_grail = media.Movie([
        "Monty Python and the Holy Grail",
        "King Arthur and his knights embark on a low-budget search for the "
        "Grail, encountering many, very silly obstacles. ",
        "Terry Gilliam and Terry Jones",
        "https://upload.wikimedia.org/wikipedia/en/0/08/Monty-Python-1975-poster.png", # pylint: disable=C0301
        "https://www.youtube.com/watch?v=LG1PlkURjxE"
    ])

    fav_movies = [lion_king, shawshank_redemp, lotr_rotk, good_bad_ugly,
                  the_matrix, spirited_away, lives_of_others, mockingbird,
                  holy_grail]

    # Generate web page and open in browser
    fresh_tomatoes.open_movies_page(fav_movies)

show_movie_site()
