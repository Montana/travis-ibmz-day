![Montana Mendy](https://user-images.githubusercontent.com/20936398/133368041-b943db58-767b-44f2-a746-c91c335cc915.png)


## IBM Z Day 2021: Testing open source apps with Travis CI with keynote speaker and presenter Montana Mendy:

The purpose of this project is to show the ease of use and implementation of IBM Z into Travis CI projects, in order to do so, we will be doing the following:

* Using IBM Z in our Travis build 
* Having an IBM Z build that has five jobs, running in parallel in Travis
* Utilize the breadth-first search in Python I wrote 
* Utilize the depth-first search in Python I wrote 
* Transpose a matrix in single line in Python with IBM Z 
* Show the simplicity of implementation on 1 side (the first `.travis.yml` file we will build) 
* Show the flexibility via running parallel builds of a BFS & DFS search - both using IBM Z (building the 2nd `.travis.yml`)
* Show off string slicing and string rotation in Python using IBM Z and Travis
* Counting uppercase, lowercase, special character and numeric values using `Regex`
* Use various Python versions (`3.5`, `3.7`, `3.9`)

## Things to Remember: 

* IBM Z build jobs are run in an LXD compliant Linux OS image, called `s390x` in the `.travis.yml` config file
* IBM Z based Docker builds, assuming all dependencies and/or a CPU architecture compliant base Docker images are extremely feasible
* Using `arch: s390x` routes your build to IBM Z-based LXD containers. You can specify which version of Ubuntu using the `dist` key, or in my case just define `linux`

## Pushing with Quay (Container Registry, the GitHub Repository must be left open):

In some cases, I prefer using Quay.io as my container registry instead of Dockerhub. One of the main reasons is the robot accounts that allow you to lock down automated access and audit each deployment. Since `quay.io` is meant for public access, this means the repo needs to be open for the build to complete and fetch the proper `env vars`. If the repo is private, the proper `env vars` will not be reached.

* https://github.com/Montana/travis-s390x-auto
* https://quay.io/montana/montana-s390x

## Author and Speaker at IBM Z Day 2021 - September 15th, 2021:

**Montana Mendy**<br>
_Software Engineer at Travis CI_<br>
_All of my code and projects will be left on GitHub as open source material, given the theme of the event_<br>
https://www.mmendy.com
