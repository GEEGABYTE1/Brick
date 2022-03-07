# Brick - An Assembly Language for Math

Brick is an Assembly language for mathematical operations made in Python. Brick uses the MIPS architecture to maintain registries and for interaction.

Moreover, the interaction of registries is inspired by USCC's computations.

Brick does basic statistical, arithmetic, and series and sequence calculations at the moment.


To interact with registers, inputs must be in binary code as described in `systemback.py`. Assembly Language is to use basic arithmetic operations with different registers. There are specific commmands listed below:

# ADDI 

Add a value from the directory with a constant. In order for the process to run, there must be a value already in the root registry at the specific index, otherwise, the program will prompt an error.

Syntax : `ADDI $destination_registry_num, [index_for_destination_registry], $root_registry_num, [index_for_root_registry], constant_val` 

The resulting command will add the sum between desired values to the desired registry. 

To access and numbers to registry, you may use binary commands, which are listed on `systemback.py`

## Error 

There are possiblities of an error occuring most commonly if the syntax is typed wrong. However, possible errors can arise if 1) the desired destination registry is empty, or the index you specify is larger than the length of the registry itself. In both cases, these issues can be solved by adding values to registries by typing binary code with that start with `000001`. 

More information can be found under `systemback.py`

