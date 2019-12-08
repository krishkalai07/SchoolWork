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

Diagram Type | Data | Proc. | Static | Dynamic | Integration | Level Of Disclousure | Scope
--- | --- | --- | --- | --- | --- | --- | ---
Domain | x |   | x |   |   | low | system
Use case |   |   |   |   | x | low | system
Activity |   | x |   | x |   | med | UC
Robustness | x | x |   | x | x | high | UC
Sequence | x | x |   | x | x | high | UC
Data Flow | x |   |   | x |   | low | system

# Use Case Description

- Required: use case name, scenarious, alternatives
- Optional: purpose/objective, actors, preconditoins, postconditions, system behavior
- Always have actor and action

# Data Flow Diagrams

- Not UML
- Shows how a system’s entities (external), processes, and storages (internal) are 
interconnected 
- Syntax
  - Entity (People, roles, organizations, external systems, etc.)
  - Data flow (input, output)
  - Process
  - Storage (Databases, files, folders, etc.)
- Leveled
  - Level 0 (Context diagram) - system level (only one process, no storage)
  - Level 1
  - Level 2
  - etc.
- Rules
  - No direct link between nouns (entity, storage)
  - Storage introduced at level 1+ (not at context)
  - Process
    - No black hole (all in, no out)
    - no white hole (no in, all out)
    - Add numbers to procesess for tracking across levels (in the same level, no order)
