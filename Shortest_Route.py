from sys import maxsize
from itertools import permutations
import random
import asyncio


# ShortestTour class provides the functionality of finding the shortest route
class ShortestTour:
    def __init__(self, num_of_cities, permutations_of_cities):
        self.__num_of_cities = num_of_cities
        self.__permutations_of_cities = permutations_of_cities

# shortest_route finds the shortest possible route that visits every city exactly once and returns to the starting point
    async def shortest_route(self):
        # store all cities apart from source city
        source_city = random.choice(range(1, self.__num_of_cities+1))
        cities = []
        for city in range(1, self.__num_of_cities+1):
            if city != source_city:
                cities.append(city)

        # store minimum weight/cost Path
        min_cost = maxsize
        next_permutation = permutations(cities)
        min_path = []
        for permutation in next_permutation:
            # store current Path weight(cost)
            current_pathweight = 0

            # compute current path weight
            k = source_city
            for city in permutation:
                current_pathweight += self.__permutations_of_cities[k-1][city-1]
                k = city
            current_pathweight += self.__permutations_of_cities[k-1][source_city-1]
            if current_pathweight < min_cost:
                min_cost = current_pathweight
                min_path = list(permutation)

            # update minimum
            min_cost = min(min_cost, current_pathweight)
        min_path = [source_city, ] + min_path + [source_city, ]
        return min_path, min_cost


async def main():
    # matrix representation of distance between all permutations of cities in form of graph
    num_of_cities = int(input("Enter the number of cities : "))
    permutations_of_cities = [[int(input(f"Enter the distance between City-{city1} and City-{city2} : "))
                               for city2 in range(1, num_of_cities+1)]
                              for city1 in range(1, num_of_cities+1)]

    try:
        shortest_route = ShortestTour(num_of_cities, permutations_of_cities)
        min_path, min_cost = await shortest_route.shortest_route()
        print("Shortest distance:", min_cost)
        print("Shortest path:", min_path)
    except ValueError as e:
        print("Error:", str(e))

if __name__ == "__main__":
    asyncio.run(main())
