
[![Build Status](https://travis-ci.org/jayventi/pydepordcalc.svg?branch=master)](https://travis-ci.org/jayventi/pydepordcalc)
##Python Dependency Order Calculator##

### Description ###
Python Dependency Order Calculator takes as parameters a project list, and a list of project to project dependencies and generates a dependency ordered lists of projects. if the projects were built in the output dependency order all dependent projects would be built first.

This tiny implementation of a classic build dependency problem was inspired by an exercise given in, Cracking The Code Interview problem 4.7 using the second solution method pp254. This is my Python 2.7 implementation on its solution. It includes unittests for all methods. 

###Unit Tests and Validating  Build Orders###
The interesting thing about this algorithm is that there are more than one valid arrangements of solution orderings. If there were no dependencies there would be n! valid arrangements since no project would be dependent on any other. this particular algorithm randomly chooses projects to explore for dependency chains, therefore the output order chain will produce randomly different valid build orderings. To check that any specific output does build in correct order a build order validation  method is included and used in the unit test to validate the output.

###Algorithm Method Description###

Before describing the method, a diagram will be presented showing the dependencies graphically which will make the description much clearer.

Given a set of projects:

projects = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

And a set of project dependencies:

dependencies = [['d', 'a'], ['b', 'f'], ['d', 'b'], ['a', 'f'], ['c', 'd']]

We can build a dependency diagram, however, the particular method is clear if the relationships in the dependencies are inverted in the diagram given here, the arrow points from the dependent project to the project requiring. It will be clear from the method of why this is a handy graph to consider. This gives the following graph:


![Dependency Diagram](https://raw.github.com/jayventi/pydepordcalc/master/dependency_diagram_1.png)

One of the several possible solutions to building this dependency tree is:
['f', 'e', 'a', 'b', 'd', 'c']

The method proceeds first inserting all projects into a list graph data structure, then randomly picking any particular node, from the available projects, without replacement, and follows the link recursively to the most dependent element in the chain. This final element will be the most dependent and in a list of build projects and should appear at the end. The full list from this random pick can be output from the most dependent to the least. 
Example if project 'b' were selected this would generate a partial list [b,d,c].

if the mark all of these projects as processed and removed them from the list of selectable projects we can proceed by choosing another random product project and continuing to build lists always inserting the new list to the left meaning earlier, or less dependent projects. An examination will show that this produces a coherent and complete list.  

This algorithm should run on the order of O(P + D) where T is the number of projects and D is the number of dependencies. 