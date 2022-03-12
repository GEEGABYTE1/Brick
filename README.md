# Brick - An Assembly Language for Math

Brick is an Assembly language for mathematical operations made in Python. Brick uses the MIPS architecture to maintain registries and for interaction.

Moreover, the interaction of registries is inspired by USCC's computations.

Brick does basic statistical, arithmetic, and series and sequence calculations at the moment.


To interact with registers, inputs must be in binary code as described in `systemback.py`. Assembly Language is to use basic arithmetic operations with different registers. There are specific commmands listed below:

# ADDI 

Add a value from the directory with a constant. In order for the process to run, there must be a value already in the root registry at the specific index, otherwise, the program will prompt an error.

Syntax : `ADDI $destination_registry_num, [index_for_destination_registry], $root_registry_num, [index_for_root_registry], constant_val` 

The resulting command will add the sum between desired values and save it to the desired registry. 

To access and numbers to registry, you may use binary commands, which are listed on `systemback.py`

# ADD 

Add a value from a directory to another value from *another* directory. In order for the process to run, there must be a values already in each directory specified. 

Syntax: `ADD $destination_registry_num, [index_for_destination_registry], $root_registry_num, [index_for_root_registry], $root_registry_num2, [index_for_root_registry2]` 

The resulting command will add the sum between desired values and save it to the desired registry.

# SUB

Subtracts a constant from a value specified in a directory. There must be values in the specified directory in order for the program to fetch the value. 

Syntax : `SUBI $destination_registry_num, [index_for_destination_registry], $root_registry_num, [index_for_root_registry], constant_val` 

# SUB

Subtracts a value from one registry with another value from a different registry. It should be noted that both registries that are being worked with must have values within.

Syntax: `SUB $destination_registry_num, [index_for_destination_registry], $root_registry_num, [index_for_root_registry], $root_registry_num2, [index_for_root_registry2]` 

# MULT 

Multiplies a value from a specific registry with a constant, and saves it to a destination registry.

Syntax : `MULT $destination_registry_num, [index_for_destination_registry], $root_registry_num, [index_for_root_registry], constant_val` 

# MUL

Multiplies a value from one registry with another value from another registry. The final product gets saved to specified destination registry.

Syntax: `MUL $destination_registry_num, [index_for_destination_registry], $root_registry_num, [index_for_root_registry], $root_registry_num2, [index_for_root_registry2]` 

# DIVT 

Divides a value from one registry with a constant. The final quotient gets saved to a destination registry specified. 

Syntax: `DIVT $destination_registry_num, [index_for_destination_registry], $root_registry_num, [index_for_root_registry], constant_val` 

*Note*: The program will output an error message if eith value being divided is 0, or there is no value at all.

# DIV

Divides a value from one registry with another value in another registry. The resulting quotient will be saved in another destination registry.

Syntax: `DIV $destination_registry_num, [index_for_destination_registry], $root_registry_num, [index_for_root_registry], $root_registry_num2, [index_for_root_registry2]` 

# LW

Loads a value from register to another register.

Syntax: `LW $destination_register_num, ($root_registry), [root_register_index]`

*Note*: It should be worth mentioning that the destination registry should be surrounded by brackets in order for the program to know that the destination registry is specified explicitly.

# SW

Stores a value from a registry to another desired register.

Syntax: `SW $root_register, [root_register_index],($destination_register)`

*Note*: It should be worth mentioning that the destination registry should be surrounded by brackets in order for the program to know that the destination registry is specified explicitly.

# XOR

Reset a desired register. All the contents in the register specified will be removed.

Syntax: `XOR $desired_register`

# J 

Jumps to a desired register, and executes the instruction within.

Syntax: `J $desired_register, [desired_register_idx]`




# Error 

There are possiblities of an error occuring most commonly if the syntax is typed wrong. However, possible errors can arise if 1) the desired destination registry is empty, or the index you specify is larger than the length of the registry itself. In both cases, these issues can be solved by adding values to registries by typing binary code with that start with `000001`. 

More information can be found under `systemback.py`




