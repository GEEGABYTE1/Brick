### BASIC Arithmetic 

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
                if result == 'invalid command':
                    print(result)
            

    

    def addi(self, input_lst):
        destination_register = 0
        register_root = 0 
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
                second_register = input_lst[character]
                second_register_cleaned = second_register.strip(', ')
                if '$' in second_register_cleaned:
                    register_root = second_register_cleaned.strip('$')
                else:
                    return 'invalid command'
            elif character == 3:
                val = input_lst[character]
                if '$' in val:
                    return 'command invalid'

            else:
                continue 
    
        ## Fetching vals needs to be done




 
process = Script()
print(process.running())
        

       

