#Task 3

class Environment:
  def __init__(self, state):
    self.state = state

  def get_percept(self):
    return self.state

class GoalBasedAgent:
  def __init__(self):
    self.goal = "Complete All Subjects"
    self.subjects = ["AI", "Math", "Physics"]   

  def formulate_goal(self, percept):
    if percept == "Not Completed Yet":
      self.goal = "Complete All Subjects"

    else:
      self.goal = "No action Needed"

  def act(self, percept):
    self.formulate_goal(percept)
    if self.goal == "Complete All Subjects":
      for subject in self.subjects:
        print(f"Studying {subject}")    
      print("Goal Achieved: All subjects Completed")

    else:
      print("Goal has already been achieved")


def run_agent(agent, environment):
  percept = environment.get_percept()
  print(f"Percept: {percept}\nAction: ")
  agent.act(percept)

agent = GoalBasedAgent()
environment = Environment("Not Completed Yet")   
run_agent(agent, environment)
