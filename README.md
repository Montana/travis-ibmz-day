# IBM Z Day 2021

Travis CI + IBM Z (IBM Z Day) Project.

The purpose of this project is to show the ease of use and implementation of IBM Z into Travis CI projects.

* Using s390x (Z) 
* Breadth-first search in Python I wrote 
* Depth-first search in Python I wrote 
* Show the simplicity of implementation on 1 side (the first `.travis.yml` file we will build) 
* Show the flexibility via running parallel builds of a BFS & DFS search - both using IBM Z (building the 2nd `.travis.yml`)

## Things to Remember: 

* IBM Z build jobs are run in an LXD compliant Linux OS image, called `s390x` in the `.travis.yml` config file
* IBM Z based Docker builds, assuming all dependencies and/or a CPU architecture compliant base Docker images are extremely feasible

## Pushing with Quay:

* https://github.com/Montana/travis-s390x-auto
* quay.io/montana/montana-s390x
