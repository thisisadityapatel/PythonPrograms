cityName = ["Surat", "Ahmedabad", "Mumbai", "Jaipur"]
ranks = [1, 13, 23, 22]
states = ["Gujarat", "Gujarat", "Maharashtra", "Rajasthan"]

city_tuples= zip(cityName, ranks, states)

class City:
    def __init__(self, city, rank, state):
        self.city = city
        self.rank = rank
        self.state = state

cities = []
for c, r, s in city_tuples:
    city = City(c, r, s)
    cities.append(city)

print(cities)