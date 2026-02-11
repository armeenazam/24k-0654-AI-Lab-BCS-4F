# Task 6

class Environment:
    def __init__(self):
        self.rooms = {
            'a': 'safe', 'b': 'safe', 'c': 'fire',
            'd': 'safe', 'e': 'fire', 'f': 'safe',
            'g': 'safe', 'h': 'safe', 'j': 'fire'
        }

    def check_room(self, room):
        return self.rooms[room]

    def put_out_fire(self, room):
        if self.rooms[room] == 'fire':
            self.rooms[room] = 'safe'

    def show_environment(self, robot_pos=None):
        print("Building Status:")
        layout = [['a','b','c'], ['d','e','f'], ['g','h','j']]

        for row in layout:
            for r in row:
                if r == robot_pos:
                    print("R", end=" ")
                elif self.rooms[r] == 'fire':
                    print("F", end=" ")
                else:
                    print(" ", end=" ")
            print()
        print("-----------")


class FireAgent:
    def __init__(self):
        self.path = ['a','b','c','d','e','f','g','h','j']

    def start_mission(self, environment):
        for room in self.path:
            print(f"Robot entered room {room}")

            if environment.check_room(room) == 'fire':
                print("Fire detected! Extinguishing...")
                environment.put_out_fire(room)
            else:
                print("Room is safe")

            environment.show_environment(room)

        print("All fires extinguished")


env = Environment()
robot = FireAgent()
robot.start_mission(env)
