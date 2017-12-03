"""This module will create instances of movie trailers"""

import media
import fresh_tomatoes

# creating favorite moview trailers list
VIVEGAM = media.Movie(
    'Vivegam',
    'Terror Friendship',
    'https://upload.wikimedia.org/wikipedia/en/b/be/Vivegam_poster.jpg',
    'https://www.youtube.com/watch?v=yJdHR8nCYWk'
    )
VEDHALAM = media.Movie(
    'Vedhalam',
    'Sister sentiment',
    'https://upload.wikimedia.org/wikipedia/en/7/72/Vedhalam.jpg',
    'https://www.youtube.com/watch?v=sGVO4-o8j1E'
    )
YENNAI_ARINTHAL = media.Movie(
    'Yennai Arinthaal',
    'Cop movie',
    'https://upload.wikimedia.org/wikipedia/en/4/4d/Yennai_Arindhaal.jpg',
    'https://www.youtube.com/watch?v=B7c87SWQg-Y'
    )
DIVERGENT = media.Movie(
    'Divergent',
    'American dystopian science fiction action film series 1',
    'https://upload.wikimedia.org/wikipedia/en/d/d4/Divergent.jpg',
    'https://www.youtube.com/watch?v=sutgWjz10sM'
    )
INSURGENT = media.Movie(
    'Insurgent',
    'American dystopian science fiction action film series 2',
    'https://upload.wikimedia.org/wikipedia/en/a/af/Insurgent_poster.jpg',
    'https://www.youtube.com/watch?v=suZcGoRLXkU'
    )
ALLEGIANT = media.Movie(
    'Alligiant',
    'American dystopian science fiction action film series 3',
    'https://upload.wikimedia.org/wikipedia/en/f/f8/Allegiantfilmposter.jpg',
    'https://www.youtube.com/watch?v=_fLg8PsLWQ0'
    )

# creating movie list array
MOVIE_TRAILERS_LIST = [
    VIVEGAM,
    VEDHALAM,
    YENNAI_ARINTHAL,
    DIVERGENT,
    INSURGENT,
    ALLEGIANT,
    ]

# call open movies page to list trailers
fresh_tomatoes.open_movies_page(MOVIE_TRAILERS_LIST)
