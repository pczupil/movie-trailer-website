import webbrowser
import os
import re


# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Fresh Tomatoes!</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">
        body {
            padding-top: 80px;
        }
        #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .movie-tile {
            margin-bottom: 20px;
            padding-top: 20px;
        }
        .movie-tile:hover {
            background-color: #EEE;
            cursor: pointer;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }

    </style>
    <script type="text/javascript" charset="utf-8">
        // When the "Storyline" button is pressed, hide movie poster, director etc.
        // and show the movie's storyline text instead.
        $(document).on('click', '.movie-tile > #storyline-btn', function(){
            $(this).hide("slow", function() {
                $(this).siblings().hide("fast");
                $(this).siblings("#storyline, button").show("slow")
            });
        });
        // When the poster button is clicked, hide the storyline text and
        // bring back the poster, director etc. for showing to the user.
        $(document).on('click', '.movie-tile > #poster-btn', function(){
            $(this).hide("slow", function() {
                $(this).siblings("#storyline, #poster-btn").hide("fast");
                $(this).siblings("#movie-trailer, #storyline-btn").show("slow")
            });
        });
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });

        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.movie-tile div', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });

        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });

        // When a sorting link is pressed, hide current films and animate in
        // the  ascending/descending order movie tiles.
        $(document).on('click', '#asc', function () {
          $('#about-text').hide('fast')
          $('.movie-tile').hide('fast')
          $('#movie_tiles_sorted .movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });
        $(document).on('click', '#desc, #home', function () {
          $('#about-text').hide('fast')
          $('.movie-tile').hide('fast')
          $('#movie_tiles_rev .movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });
        $(document).on('click', '#about', function () {
          $('.movie-tile').hide('fast')
          $('#about-text').show('fast')
        });
    </script>
</head>
'''


# The main page layout and title bar
main_page_content = '''
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>

    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#" id="home"
            color="#BBB">Fresh Tomatoes Movie Trailers</a>
            <a class="navbar-brand" href="#" id="about"
            color="#BBB">About Site</a>
          </div>
          <div class="dropdown btn-group pull-right">
            <button class="btn btn-primary dropdown-toggle"
            name="sort-button" type="button" data-toggle="dropdown">Sort Movies
            <span class="caret"></span></button>
            <ul class="dropdown-menu">
              <li><a href="#" id="desc">TITLE(DESC)</a></li>
              <li class="divider"></li>
              <li><a href="#"  id="asc">TITLE(ASC)</a></li>
          </div>
        </div>
      </div>
    </div>
    <div class="container" id="movie_tiles_rev">
      {movie_tiles_rev}
    </div>
    <div class="container" id="movie_tiles_sorted">
      {movie_tiles_sorted}
    </div>
    <div class="container" id="about-site">
      <p id="about-text" style="display:none">The project uses the provided
      "fresh_tomatoes.py" file to generate an HTML
      file that displays a grid of movie posters, along with other information
      about the movies. Clicking on a poster will bring up the movie's trailer (via
      youtube). Clicking on a movie's "storyline" button will replace the poster
      with some text briefly describing the film's storyline. The poster is
      brought back by clicking the movie's "poster" button. The movies can be
      sorted by clicking the sort button in the upper right corner and selecting
      which an order to sort the movies by (the sorting is done by using two movie
      lists, whose ordering differs, and rendering them in two separate bootstrap
      containers). Clicking on "About Site" will replace the movie-tiles with this
      text. To bring back the movie-tiles, click on "Fresh Tomatoes Movie Trailers"
      in the navbar.</p>
    </div>
  </body>
</html>
'''


# A single movie entry html template
movie_tile_content = '''
<div class="col-md-6 col-lg-4 movie-tile text-center">
  <div id="movie-trailer" data-trailer-youtube-id="{trailer_youtube_id}"
  data-toggle="modal" data-target="#trailer">
    <img src="{poster_image_url}" width="220" height="342">
    <h2>{movie_title}</h2>
    <h4>Directed by</h5>
    <h3>{director}</h4>
  </div>
  <div id="storyline" style="display:none" data-trailer-youtube-id="{trailer_youtube_id}"
  data-toggle="modal" data-target="#trailer">
    <h2>{movie_title}</h2>
    <p>{movie_storyline}</p>
  </div>
  <button class="btn btn-primary" id="storyline-btn">Storyline</button>
  <button class="btn btn-primary" id="poster-btn" style="display:none">Poster</button>
</div>
'''


def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            movie_storyline=movie.storyline,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id,
            director=movie.director
        )
    return content


def open_movies_page(movies):
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(
        movie_tiles_sorted=create_movie_tiles_content(sorted(movies)),
        movie_tiles_rev=create_movie_tiles_content(sorted(movies, reverse=True))
    )
    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
