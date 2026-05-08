"""
4.2 Question: Function-Call Stack

Question: What happens if you keep pushing onto a stack, without enough popping?

Answer: 
If you keep pushing data onto the function-call stack without popping 
(removing) them, the stack will eventually run out of memory. This results 
in a fatal error known as a "Stack Overflow." This commonly happens if you 
write an infinite loop inside a recursive function (a function that calls itself) 
that never reaches its stopping condition.
"""
