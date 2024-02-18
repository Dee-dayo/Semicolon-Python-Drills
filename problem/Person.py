from problem import Problem


class Person:
    def __init__(self):
        self.list_of_problems = []

    def add_problem(self, problem):
        self.list_of_problems.append(problem)

    def solve_problem(self, problem):
        if problem in self.list_of_problems:
            problem.change_status()
        else:
            raise ValueError("No such problem")

    def recount_unsolved_problems(self):
        unsolved_problems = []
        for problem in self.list_of_problems:
            if not problem.check_status():
                unsolved_problems.append(problem)

        return unsolved_problems
