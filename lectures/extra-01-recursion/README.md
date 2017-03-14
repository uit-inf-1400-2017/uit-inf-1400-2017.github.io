The question leading up to this extra lecture popped up when using the Fibonacci example with decorators (oop-07).

If you are checking out this code, please watch the lecture. 

The general plan for the lecture was: 

- Explain heap.
- Explain stack and relation to function calls.
  - local variables on stack (many languages)
  - save state when calling a new function (push cur position)
  - when entering function: push new variables onto stack.

The implication is that a function can call itself.

Demonstration code: 
- Simple graph: [1,2,[3,[4,5],[6,[7]]]]
- Use decorators to decorate recursive function. 
- fibonacci

Kahoot for predict results.



