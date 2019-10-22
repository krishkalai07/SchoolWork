Notes for exam 1 on October 30

# Details
- Paper test
- 1 sheet of notes allowed

# Requirement (SRS)
- Unconstructed (free from design) description of the system - contract
  - Functional -> what system must do
  - Non-functional -> external constraints that the system must adhere to
    - quality considerations
    - "good software" such as: (illities)<ul><li>reliability</li><li>availiability</li><li>safety</li><li>secity</li><li>usability</li><li>maintainability</li><li>efficeinty</li><li>etc</li></ul>
  - don't know how itll be done / external service / vendors / libraries -> impl. details

# Domain Model
- Focus purely on the problem domain
- From SRS, extract the nouns and noun phrases, then refine
- Example
  - The system shall be an electronic device designed for automatically serving users. 
  - A card holder shall be able to view balance in his/her accounts
  - Customers will interact with the system through a simple interface consisting of a card reader and a numeric keypad
- May be refined – use singular form
  - Duplicates (user, card holder, customer) -> merge to Customer
  - Get rid of or revisit/revise too big, general, out of scope terms (system, electronic device)
  - Get rid of “too small” words (balance)
  - Some may be actors (customer) for the use case – keep it, will revise later
- Remaining: customer, account, interface, card reader, keypad

# Notation
- UML (Unified Modeling Languange)
  - Class
  - Association
  - "has-a"
    - Aggregation: has owner, but doesn't die with owner (library has a book, but if library is destroyed, books still exist)
    - Composition: dies with the owner (book has a page, but if book is destroyed, pages are destroyed)
    - Multiplicty: optional
    - [A]-open diamond-line-[B] = A has a B
  - "is-a"
    - inheritance
    - [A]-open triangle-line[B] = A is a B
    - **Ex: Car is a vehicle**

# Use case
- Scenario-orienteddescription of expected functionality for the system 
  - Show *what* can be done (instead of *how* it works)
  - Disregard class, object, package, etc.
- **Triggered by actor**
- UML syntax
  - Actor (stick figure person)
    - Anything external to the program that interacts with the program
  - Use case (oval)
    - Provides value to actor
    - No implemention specified
  - Interaction (line)
  - Relationships between use cases, required in this course: include, 
extend, inheritance (override)
  - Relationships between actors (used rarely, but ref FCS) - inheritance

# Use Case Description
  - In this class, required items are: Use case name, Scenarios, Alternatives
    - must have them for all use case descriptions
 - Other items such as purpose/objective, actors, preconditions, post conditions are optional
 - Example
   - Name: Session use case
   - Scenarios: 
Item | Scenario
--- | ---
1 | Customer inserts an ATM card into the card reader slot of the machine
2 | The ATM pulls the card into the machine and reads it
3 | The customer is asked to enter his/her PIN
4 | The ATM passes the card number and the PIN to the banking system for validation
5 | Customer is then allowed to perform one or more transactions, choosing from a menu of possible types of transaction in each case
6 | Apply Transaction use case
7 | After each transaction, the customer is asked whether he/she would like to perform another. If yes, go to step 6.
8 | When the customer is through performing transactions, the card is ejected from the machine and the session ends

# Activity Diagram
- Model the procedural flow of actions 
  - Logic in a single use case or logic of a business rule
  - Like a UML flowchart
- Syntax (Example: Flight Check in and Boarding Procedures)
  - Initial node 
  - Activity 
  - Transition (optionally may have Guard Condition
  - Concurrency
  - Decision
  - Merge
  - Flow final (not used very often)
  - Activity final 
  - Swim lane (optional, to assign responsibilities to the activity)  
