### BASIC Arithmetic 

## Test values to add to the register
# ("00000100000000000000001010000000")
# ("00000100000000000000000101000000")

from register_origin import System

class Script:
    
    system = System()
    
    def running(self):
        while True:
            user_input = str(input(': '))

            user_input_formatted = user_input.strip(' ')
            
            if len(user_input_formatted) == 32:
                self.system.binary_reader(user_input_formatted)

            user_input_split = user_input_formatted.split(' ')


            if 'ADDI' in user_input_split:
                result = self.addi(user_input_split)
                if type(result) == str:
                    print(result)
                else:
                    pass 
            
            

    

    def addi(self, input_lst):                          # Format ADDI $1, [idx1], $2, [idx2], Const_val
        destination_register = 0
        destination_idx = 0 
        register_root = 0 
        register_root_idx = 0 
        val = 0
        for character in range(len(input_lst)):
            if character == 1:
                first_register = input_lst[character]
                first_register_cleaned = first_register.strip(', ')
                if '$' not in first_register_cleaned:
                    return 'invalid command'
                else:
                    destination_register = first_register_cleaned.strip('$')
            elif character == 2:
                first_register_idx = input_lst[character]
                if '[' in first_register_idx and ']' in first_register_idx:
                    first_register_idx = first_register_idx.strip('[')
                    first_register_idx = first_register_idx.strip('], ')
                    destination_idx = int(first_register_idx)
                else:
                    return 'invalid command'

            elif character == 3:
                second_register = input_lst[character]
                second_register_cleaned = second_register.strip(', ')
                if '$' in second_register_cleaned:
                    register_root = second_register_cleaned.strip('$')
                else:
                    return 'invalid command'

            elif character == 4:
                second_register_idx = input_lst[character]
                if '[' in second_register_idx and ']' in second_register_idx:
                    second_register_idx = second_register_idx.strip('[')
                    second_register_idx = second_register_idx.strip('], ')
                    register_root_idx = int(second_register_idx)
                else:
                    return 'invalid command'

                
            elif character == 5:
                if '$' in input_lst[character]:
                    return 'command invalid'
                else:
                    val = int(input_lst[character])

            else:
                continue 
    
        destination_register_lst = self.system.number_registers[int(destination_register)]
        if destination_idx >= len(destination_register_lst):
            return 'invalid command'
        
        root_register_lst = self.system.number_registers[int(register_root)]
        if register_root_idx > len(root_register_lst):
            return 'invalid command'
        try:
            root_value = root_register_lst[register_root_idx]
            summation = val + root_value 
        
            destination_register_lst.append(summation)
            self.system.store_to_history_register(summation)
            print('{} has been added succesfully to the register: {}'.format(summation, destination_register))
            return True
        
        except IndexError:
            return 'there is no value in register {}'.format(register_root)



 
process = Script()
print(process.running())
        

       

