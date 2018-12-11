from abc import ABCMeta, abstractmethod


class Agent(metaclass=ABCMeta):
    def __init__(self, criticality=1):
        self.criticality = criticality
        self.state = None  # IDLE, RUNNING, DONE

    def cycle(self):
        if self.state == "RUNNING":
            self.perceive()
            self.decide()
            self.act()

            self.criticality = self.compute_criticality()

    @abstractmethod
    def perceive(self):
        pass

    @abstractmethod
    def decide(self):
        pass

    @abstractmethod
    def act(self):
        pass

    @abstractmethod
    def compute_criticality(self):
        pass
