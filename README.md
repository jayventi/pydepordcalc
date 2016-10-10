
[![Build Status](https://travis-ci.org/jayventi/pydepordcalc.svg?branch=master)](https://travis-ci.org/jayventi/pydepordcalc)
##Python Dependency Order Calculator##

### Description ###
Python Dependency Order Calculator takes as parameters a project list, and a list of project to project dependencies and generates a dependency ordered lists of projects. If the projects were built in the output dependency order all dependent projects would be built first.

This implementation of a classic build dependency problem was inspired by an exercise given in, Cracking The Code Interview problem 4.7 using the second solution method pp254. This is a Python 2.7 implementation, it includes unittests for all methods. 

###Unit Tests and Validating  Build Orders###
The interesting thing about this algorithm is that there are more than one valid arrangements of solution orderings. If there were no dependencies there would be n! valid arrangements since no project would be dependent on any other. This particular algorithm randomly chooses projects to explore for dependency chains, therefore the output order chain will produce randomly different valid build orderings. To check that any specific output does build in correct order a build order validation  method is included and used in the unit test to validate the output.

###Algorithm Method Description###

Before describing the method, a diagram will be presented showing the dependencies graphically which will make the description much clearer.

Given a set of projects:

projects = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

And a set of project dependencies:

dependencies = [['d', 'a'], ['b', 'f'], ['d', 'b'], ['a', 'f'], ['c', 'd']]

We can build a dependency diagram,where the links point from the dependent project to the project requiring them. It will be clear from the method why this is a handy graph to consider. This gives the following graph:

Note, this particular method utilizes a dependency graphs where the dependencies are inverted from what might be expected. 

![Dependency Diagram](https://raw.github.com/jayventi/pydepordcalc/master/dependency_diagram_1.png)

One of the several possible solutions to building this dependency tree is:
['f', 'e', 'a', 'b', 'd', 'c']

The method proceeds first inserting all projects into a list graph data structure, then randomly picking any particular node, from the available projects, without replacement, and follows the link recursively to the most dependent element in the chain. This final element will be the most dependent and in a list of build projects and should appear at the end. The full list from this random pick can be output from the most dependent to the least. 
Example if project 'b' were selected this would generate a partial list [b,d,c].

After all are processed and removed from the list of selectable projects we can proceed by choosing another random project and continuing to build partial lists, always merging the new list to the left of earlier list. Since we can't go wrong assuming the remaining projects might be more dependent than those already processed. An examination will show that this produces a coherent and complete dependency build order list. 

It should be noted that in most cases many different valid lists can be produced and as this algorithm proceeds randomly different runs may produce different but still valid buildable output lists.

This algorithm should run on the order of O(P + D) where P is the number of projects and D is the number of dependencies. building the graph object will be On the order of P + D and processing the graph will be on the order of D.