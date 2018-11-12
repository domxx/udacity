from media import Movie
from fresh_tomatoes import open_movies_page


def main():
    hp1 = Movie(
        "Harry Potter 1",
        "https://images-na.ssl-images-amazon.com/images/I/51asM9eJMXL.jpg",
        "https://www.youtube.com/watch?v=VyHV0BRtdxo"
    )

    hp2 = Movie(
        "Harry Potter 2",
        "https://i.ytimg.com/vi/zX_PHrUTbLM/movieposter.jpg",
        "https://www.youtube.com/watch?v=1bq0qff4iF8"
    )

    hp3 = Movie(
        "Harry Potter 3",
        "https://cdn.europosters.eu/image/750/posters/harry-potter-3-forest-i621.jpg",  # noqa
        "https://www.youtube.com/watch?v=lAxgztbYDbs"
    )

    hp4 = Movie(
        "Harry Potter 4",
        "https://i.ytimg.com/vi/gPhXYeoCDlQ/movieposter.jpg",
        "https://www.youtube.com/watch?v=3EGojp4Hh6I"
    )

    hp5 = Movie(
        "Harry Potter 5",
        "https://i.ytimg.com/vi/Ak6vjFiZUqM/movieposter.jpg",
        "https://www.youtube.com/watch?v=y6ZW7KXaXYk"
    )

    hp6 = Movie(
        "Harry Potter 6",
        "https://i.ytimg.com/vi/TA7uBS2hfik/movieposter.jpg",
        "https://www.youtube.com/watch?v=jpCPvHJ6p90"
    )

    hp71 = Movie(
        "Harry Potter 7 pt.1",
        "https://imgc.allpostersimages.com/img/print/posters/harry-potter-7-part-2-one-sheet_a-G-8554781-0.jpg",  # noqa
        "https://www.youtube.com/watch?v=MxqsmsA8y5k"
    )

    hp72 = Movie(
        "Harry Potter 7 pt.2",
        "https://static.posters.cz/image/1300/plagaty/harry-potter-7-part-2-teaser-i11030.jpg",  # noqa
        "https://www.youtube.com/watch?v=VGBLczT_sLo"
    )

    # Open movie trailer page with list of provided movie instances
    open_movies_page([hp1, hp2, hp3, hp4, hp5, hp6, hp71, hp72])


if __name__ == '__main__':
    main()
