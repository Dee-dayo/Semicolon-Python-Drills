import unittest

from problem.Person import Person
from problem.Problem import Problem
from problem.Type import Type


class MyTestCase(unittest.TestCase):
    def test_that_problem_can_be_created(self):
        new_problem: Problem = Problem('SchoolFee', Type.FINANCIAL)
        self.assertEqual(new_problem.name, 'SchoolFee')
        self.assertEqual(new_problem.type, Type.FINANCIAL)
        self.assertFalse(new_problem.isSolved)

    def test_multiple_problems_can_be_added_by_person(self):
        new_problem1: Problem = Problem('SchoolFee', Type.EDUCATION)
        new_problem2: Problem = Problem('Valentine Gift', Type.FINANCIAL)
        new_problem3: Problem = Problem('Church Offering', Type.SPIRITUAL)

        new_Person = Person()
        new_Person.add_problem(new_problem1)
        new_Person.add_problem(new_problem2)
        new_Person.add_problem(new_problem3)

        problems = [new_problem1, new_problem2, new_problem3]
        self.assertListEqual(problems, Person.recount_unsolved_problems(new_Person))

    def test_person_can_create_multiple_problem_solve_problem_recount_unsolved(self):
        new_problem1: Problem = Problem('SchoolFee', Type.EDUCATION)
        new_problem2: Problem = Problem('Valentine Gift', Type.FINANCIAL)
        new_problem3: Problem = Problem('Church Offering', Type.SPIRITUAL)

        new_Person = Person()
        new_Person.add_problem(new_problem1)
        new_Person.add_problem(new_problem2)
        new_Person.add_problem(new_problem3)

        new_Person.solve_problem(new_problem3)

        problems = [new_problem1, new_problem2]
        self.assertListEqual(problems, Person.recount_unsolved_problems(new_Person))

    def test_person_cant_solve_problem_if_problem_is_invalid(self):
        new_problem1: Problem = Problem('SchoolFee', Type.EDUCATION)
        new_problem2: Problem = Problem('Valentine Gift', Type.FINANCIAL)

        new_person = Person()
        new_person.add_problem(new_problem1)
        new_person.add_problem(new_problem2)

        new_problem3: Problem = Problem('Church Offering', Type.SPIRITUAL)

        with self.assertRaises(ValueError): new_person.solve_problem(new_problem3)
