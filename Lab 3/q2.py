import random

class ModelBasedAgent:
    def __init__(self):
        self.model = {
            "students": "No",
            "lights": "OFF"
        }

    def update_model(self, students, lights):
        self.model["students"] = students
        self.model["lights"] = lights

    def act(self, students_present, light_status):
        action = "No Action"

        if students_present == "Yes" and light_status == "OFF":
            action = "Turn Lights ON"
            light_status = "ON"

        elif students_present == "No" and light_status == "ON":
            action = "Turn Lights OFF"
            light_status = "OFF"

        self.update_model(students_present, light_status)

        print(f"Agent Model (Memory): {self.model}")
        return action

class Environment:
    def __init__(self):
        self.light_status = "OFF"

    def get_student_presence(self):
        return random.choice(["Yes", "No"])

def run_agent(agent, environment, steps):
    for step in range(steps):
        print(f"\nStep {step + 1}")

        students_present = environment.get_student_presence()
        action = agent.act(students_present, environment.light_status)

        environment.light_status = agent.model["lights"]

        print(f"Students Present: {students_present}")
        print(f"Light Status: {environment.light_status}")
        print(f"Action Taken: {action}")


agent = ModelBasedAgent()
environment = Environment()

run_agent(agent, environment, 8)
