# Instruction pipelining

A nonpipeline system takes 300ns to process a task. 

The same task can be processed in a 5-segment pipline with a clock cycle of 60ns. 

What is the maximum speedup that could be acheived with the pipeline unut over the nonpipeline unit

# Data Hazards

RAW (Read after write): true depndency

WAW (Write after write): output dependency

WAR (Write after read): (rare) ignore error

# Instruction pipeline

1  | 2  | 3  | 4  | 5  | 6  | 7  | 8  | 9  | 10 | 11 | 12 | 13 | 14
IB | DC | OA | EX |    |    |    |    |    |    |    |    |    |
   | IA | DC | OA | EX |    |    |    |    |    |    |    |    |
   |    | IA | DX | OA | EX |    |    |    |    |    |    |    |
   |    |    | IA | DC |    | OA | EX |    |    |    |    |    |
   |    |    |    | IA | DC |    |    | OA | EX |    |    |    |
   |    |    |    |    | IA | DC |    |    | OA | EX |    |    |
   |    |    |    |    |    | IA | DC |    |    |    | OA | EX |


# Memory management

Computer uses byte-addressing virtual memory sys with 2 entry TLBl, a 2 way set associative cache amd a page table for a proceess P.

Assume cache blocked of size 8 bytes. 

Assume pages of size 16 bytes and a main memory of 4 frames. 

Assume the follwing TLB and page table for Process P:

Physical address bits:

4\*16 = 6 bits

2 bits for frame

virtual address bits

8\*16 bytes = 7 bits

Assume a cache of 32 bytes, show the bit structure of physical memory address

```

| | | | | | |
 - - 
 tag - -
     set - -
        offset
```

Show the ds used to impl lru replce start on the tlb and phs mem lvls.

# Combinatiobal circuit

F = (~xz)y  + (y + xz)

   | ~x~y  | x~y  | xy | ~xy
z  |       |      |    |
~z |       |      |    |
