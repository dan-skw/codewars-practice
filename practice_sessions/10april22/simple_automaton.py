"""
Design a Simple Automaton (Finite State Machine): https://www.codewars.com/kata/5268acac0d3f019add000203
Create a finite automaton that has three states. Finite automatons are the same as finite state machines for our purposes.

"""

class Automaton(object):
    def q1(input):
        if input == '1':
            return Automaton.q2
        return Automaton.q1
    
    def q2(input):
        if input == '0':
            return Automaton.q3
        return Automaton.q2
    
    def q3(input):
        return Automaton.q2
    
    def __init__(self, initial_state):
        self.current_state = initial_state

    def read_commands(self, inputs):
        for input in inputs:
            self.current_state = self.current_state(input)
            
        return self.current_state == Automaton.q2

my_automaton = Automaton(initial_state=Automaton.q1)