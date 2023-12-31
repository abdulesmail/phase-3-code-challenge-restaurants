class Review:
    reviews = []
    def __init__(self, customer, restaurant, rating):
        """
        initializes customer, restaurant, and a rating (a number)
        """
        self.__customer = customer
        self.__restaurant = restaurant
        self.__rating = rating

        Review.__add_reviev(self)

    def rating(self):
        return self.__rating
    
    def customer(self):
        return self.__customer
    
    def restaurant(self):
        return self.__restaurant
    
    @classmethod
    def all(cls):
        return cls.reviews
    
    @classmethod
    def __add_reviev(cls, review):
        cls.reviews.append(review)