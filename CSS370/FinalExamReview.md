# Use case
- Scenario-oriented description of expected functionality for the system 
  - Show “what” can be done (instead of “how” it works
  - Don’t care about class, object, package, etc. 
  - Triggered by an actor
  - UML syntax
    - Actor: anything external to the program that interacts with the program
    - Use case: Provides value to actors
    - Interaction
    - Relationship between use cases: include, extend, inheritance
    - Relationship between actors: inheritance

# Diagram comparisons

Diagram Type | Data | Proc. | Static | Dynamic | Iintegration | Level Of Disclousure | Scope
Domain | x |   | x |   |   | low | system
Use case |   |   |   |   | x | low | system
Activity |   | x |   | x |   | med | UC
Robustness | x | x |   | x | x | high | UC
Sequence | x | x |   | x | x | high | UC
Data Flow | x |   |   | x |   | low | system


