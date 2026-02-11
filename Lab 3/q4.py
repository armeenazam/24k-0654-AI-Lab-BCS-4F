#Task 4
class Environment:
  def __init__(self, name, rating, distance):
    self.name = name
    self.rating = rating
    self.distance = distance

class UtilityBasedAgent:
   def calculate_utility(self, restaurant):
        return restaurant.rating - restaurant.distance

   def select_restaurant(self, restaurants):
        u = self.calculate_utility(restaurants[0])
        selected = restaurants[0].name

        for r in restaurants:
            utility = self.calculate_utility(r)
            print(f"Restaurant {r.name} Utility = {utility}")

            if utility > u:
                u = utility
                selected = r.name

        print(f"Selected Restaurant: {selected}")


restaurant_A = Environment("A", 7, 3)
restaurant_B = Environment("B", 9, 5)

utility_agent = UtilityBasedAgent()
utility_agent.select_restaurant([restaurant_A, restaurant_B])
