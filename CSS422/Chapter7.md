# Pipelineing and Performance

- Modern microprocessorrs
- Pipelines:: definiton and usage
- The effects of pipelinig on computer performance

- Chapter 5-5 by `NULL`

# Microprocessor Overview
- Range of speed, power, functionality, cost
  - $0.25 for a 4 bit controller
  - $10000 for a space-qualiified custom processor

# Differentiating among mocroproceessors
  - architectue: cics, riscm dsp
  - data path wirdth
  - addressing address space
  - instrcutvion set arcitecuter
  - processor speed

# Architecture
- CISC: Complex Instruction Set Computer
  - Many instruction and adressing modes
    - CISC Code is compact
    - Can be many clock cyckes oer instruction
    - Large silicon area
    - von Neumann Archinteucre : sane mam sa[ace serve instrution and data
- RISC: Reduced Instruction Set Computer
  - Modern architecture
  - 1 instruction per clock cycle (fast)
  - originally harvard architecture
    - seperate memeory space for instructions and data
    - avoid von Neumann bottleneck
  - may use von Newmann with specified cache
# Von Neumann bottleneck
- von Neumann CPU -> Instruction, Data
- Data <- Harvard CPU -> Instruction

# Characteristics of RISC
- very fast and efficient
  - risc images are larger
- RISC computers are better for data processing applications
- CISC computers are better for control applications
- RISC CPU cores tend to be small, since microcode ROM is not necessary
- RISC core are very prevalent in ASIC (Application-Specific Integrated Circuit) devices
  - ARM Ltd. sells RISC CPU designs as Intellectual Property to IC builders
  - iPhone uses an ARM-based RISC microcontroller

# Instruction set architecture (ISA)
- The PC world is dominated by the Intel Architecture
- The embedded processor world was dominated by the Motorola 68K instruction set architecture
  - 68000 > 68020 > 68030 >68040 > 68060 > ColdFire
  - ColdFire unites a modern CISC/RISC processor architecture with backwards compatibility to the original 68K (because there is still lots of 68k code
- ARM (Advanced RISC Machines) is now the dominant embedded microprocessor architecture
  - Owns smart phones, and maybe tablets
- Atmel (Arduino) and TI microprocessors

# Performance
- Why we have different architectures?
  - 
- How to design for speedup with these architectures?
  - 
  - Reduce propagation delay: IC fabrication process
  - Reduce the number of gates
  - Hire a better hardware designer?
  - Pipelining - the favorable approach

# Pipelining
- Processor is an expensive resource
  - Want to always keep it busy since an idle processor is wasting space, energy, time, etc.
  - Need a way to increase performance
- Idea
  - Break execution task into smaller tasks (stages)
  - In Each stage, a different hardware component is used (data path)
  - Overall time to execute any one instruction is the same
  - Next instruction is only one stage behind
  - Increase the throughput of the processor
    -  Multiple instructions within the pipeline at the same time

# Decomposition of a Process
- A computational process with three logical stages
- The same process is divided into three physical stages
  - Each stage is handled by dedicated hardware
  - Here TP = N x Tg
  - N = Number of stages
  - Tg = Process time per stage
- A computational process with series of logical stages (three processes):
  - Processing time of one logical state: Tp = 3 x Tg
  - Total processing time for 3 instructions: 3Tp = 9Tg

# Excersise
- 1A: 260ns
