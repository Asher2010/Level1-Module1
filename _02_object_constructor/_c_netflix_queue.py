class Movie:
    def __init__(self, title, stars):
        self.title = title
        self.stars = stars

    def to_string(self):
        return "\"" + self.title + "\" - " + str(self.stars) + " stars"

    def get_ticket_price(self):
        if self.stars > 2:
            return "That will be $12 please."
        elif 'twilight' in self.title.lower():

            return "This movie is so bad, we'll pay YOU to watch it!"
        else:
            return "Don't waste your money on this horrible rubbish."


class NetflixQueue:
    def __init__(self):
        self.movies = list()

    def get_best_movie(self):
        self.sort_movies_by_rating()
        return self.movies[0]

    def add_movie(self, movie):
        self.movies.append(movie)

    def get_movie(self, movie_number):
        return self.movies[movie_number]

    def sort_movies_by_rating(self):
        self.movies.sort(key=lambda movie: movie.stars, reverse=True)

    def print_movies(self):
        print("Your Netflix queue contains: ")

        for movie in self.movies:
            print(movie.to_string())


if __name__ == '__main__':

    # Use Movie and NetflixQueue classes above to complete the following changes:

    # TODO 1) Instantiate (create) at least 5 Movie objects.
    # TODO 2) Use the Movie class to get the ticket price of one of your movies.
    # TODO 3) Instantiate a NetflixQueue object.
    # TODO 4) Add your movies to the Netflix queue.
    # TODO 5) Print all the movies in your queue.
    # TODO 6) Use your NetflixQueue object to finish the sentence "the best movie is...."
    # TODO 7) Use your NetflixQueue to finish the sentence "the second best movie is...."

    GranTurismo = Movie("Gran Turismo", 4.9)
    print(GranTurismo.get_ticket_price())

    Barbie = Movie("Barbie", 0)
    print(Barbie.get_ticket_price())

    Twilight = Movie("twilight", 1)
    print(Twilight.get_ticket_price())

    SixthSense = Movie("Sixth Sense", 5)
    print(SixthSense.get_ticket_price())

    Aquaman = Movie("Aquaman", 1)
    print(Aquaman.get_ticket_price())

    Queue = NetflixQueue()
    Queue.add_movie(movie=GranTurismo)
    Queue.add_movie(movie=Barbie)
    Queue.add_movie(movie=Twilight)
    Queue.add_movie(movie=Aquaman)
    Queue.add_movie(movie=SixthSense)
    Queue.print_movies()
    Queue.sort_movies_by_rating()
    print("The best movie is", str(Queue.get_best_movie().to_string()))
    print("The second best movie is", Queue.get_movie(1).to_string())









