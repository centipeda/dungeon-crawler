class TurnManager:
    def __init__(self,level):
        self.level = level
        self.speedcheck = SpeedChecker()
        self.collector = ActionCollector()
        self.executor = ActionExecutor()

    def execute_turn(self):
        monsters = self.speedcheck.sort_speed(level)
        # reminder that get_actions should just call do() for all
        # monsters collected from
        actions = self.collector.get_actions(monsters)
        for action in actions:
            self.executor.execute(action)

class SpeedChecker:
    def __init__(self):
        pass

    def sort_speed(self,level):
        pass

class ActionCollector:
    def __init__(self):
        pass

    def get_actions(level,order):
        pass

class Executor:
    def __init__(self):
        pass
    
    def execute(self,action,level):
        pass
