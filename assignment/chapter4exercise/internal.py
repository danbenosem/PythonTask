"""
4.18 Internal vs. External Iteration

Question: Why is internal iteration preferable to external iteration in 
functional-style programming?

Answer: 
External iteration (like writing your own 'for' or 'while' loops manually) 
requires you to manage the looping logic, counters, and stopping conditions, 
which introduces room for bugs (like off-by-one errors). 

Internal iteration (using built-in tools like 'map' or 'filter') hides the 
looping logic under the hood. It is preferable because it results in cleaner, 
more concise code, and it allows the programming language to automatically 
optimize the loop for performance behind the scenes.
"""
