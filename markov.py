#extra libraries used
import queue
import tools
import random

"""
markov_chain class is a class that creates a(n) markov chain statistical
model on an inputted list of objects.

The class is then able to generate randomly a new list of objects based
on the analysis model of the inputted list.
"""
class markov_chain:
    
    """
    Class constructor, at the very minium, the class needs an inputted list of
    objects the level parameter is extra to specify the level of the markov
    chain
    """
    def __init__(self, obj_list: list, level:int = 1):
        self.level = level #level class variable
        self.obj_list = obj_list #list of objects
        self.transitions = {}
        self.generate_prob_table()

    """
    generate_prob_table goes through the list of objects and generates a probability
    table of current object to the previous object that can be used to look up again.
    
    NOTE: you might not need to keeptrack of a probability, just the count of one 
    object appearing after another
    """

    def generate_prob_table(self):
        for i in range(len(self.obj_list) - self.level):
            state = self.obj_list[i:i+self.level]
            next = self.obj_list[i+self.level]
            if tuple(state) not in self.transitions:
                self.transitions[tuple(state)] = {}
            if next not in self.transitions[tuple(state)]:
                self.transitions[tuple(state)][next] = 0
            self.transitions[tuple(state)][next] += 1


    """
    generate_random_list uses the probability table and returns a list of
    objects that adheres to the probability table generated in the previous
    method
    NOTE: the first object has to be selected randomly(the seed)
    NOTE: the count parameter is just to specify the length of the generated
    list
    """
    def generate_obj_list(self, count:int = 10):
        start = random.randrange(len(self.obj_list)-self.level)
        output = self.obj_list[start:start+self.level]
        state = self.obj_list[start:start+self.level]

        for i in range(count-self.level):
            choice = tools.weighted_choice(self.transitions[tuple(state)])
            output.append(choice)
            state.append(choice)
            state.pop(0)
        return output
