
[![Build Status](https://travis-ci.org/jayventi/pydepordcalc.svg?branch=master)](https://travis-ci.org/jayventi/pydepordcalc)##Python Dependency Order Calculator##

### Description ###
Python Dependency Order Calculator takes as parameters a project list, and a list of project to project dependencies and generates a dependency ordered lists of projects. if the projects were built in the output dependency order all dependent projects would be built first.

This tiny implementation of a classic build dependency problem was inspired by an exercise given in, Cracking The Code Interview problem 4.7 using the second solution method pp254. This is my Python 2.7 implementation on its solution. It includes unittests for all methods. 

###Unit Tests and Validating  Build Orders###
The interesting thing about this algorithm is that there are more than one valid arrangements of solution orderings. If there were no dependencies there would be n! valid arrangements since no project would be dependent on any other. this particular algorithm randomly chooses projects to explore for dependency chains, therefore the output order chain will produce randomly different valid build orderings. To check that any specific output does build in correct order a build order validation  method is included and used in the unit test to validate the output.
