# Dependency Resolver

Imagine you have a list of task which you need to perform. But, one task may be
dependent on other tasks. As there is a dependency between the tasks, it must be
resolved, so that all the tasks can be completed.

For example: <br/>
In linux, when we install a package, we see that several other packages needs to be installed which are the dependencies to the package we want to install. Again, those dependency packages might have dependency with each other.  

This is a typical graph topological sorting problem.

The script topsort_using_bfs.py helps to resolve the dependency.
