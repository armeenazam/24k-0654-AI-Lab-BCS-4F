#Task 1

class Environment:
  def __init__(self, traffic = 'heavy'):
    self.traffic = traffic

  def get_percept(self):
    if self.traffic == 'heavy':
      return "Heavy Traffic"

    else:
      return "Light Traffic"

class ReflexiveAgent:
    def __init__(self):
      pass

    def act(self, percept):
      if percept == "Heavy Traffic":
        return "Extend Green Time"
      else:
        return "Normal Green"

def run_agent(agent, environment):
  percept = environment.get_percept()
  action = agent.act(percept)
  print(f"Percept: {percept}, Action: {action}")      

agent1 = ReflexiveAgent()
environment1 = Environment("heavy")

agent2 = ReflexiveAgent()
environment2 = Environment("light")

run_agent(agent1, environment1)
run_agent(agent2, environment2)
