import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://www.gstatic.com/tv/thumb/movieposters/17420/p17420_p_v8_ab.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://www.labutaca.net/peliculas/wp-content/uploads/2010/01/avatar-cartel.jpg",
                     "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

apellidos = media.Movie("lidos catalanes",
                        "Spanish film",
                        "http://pics.filmaffinity.com/Ocho_apellidos_catalanes-640444128-large.jpg",
                        "https://www.youtube.com/watch?v=ebyALRLNdpA")

movies = [toy_story, avatar, apellidos]

fresh_tomatoes.open_movies_page(movies)
