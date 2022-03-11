### BASIC Arithmetic 

## Test values to add to the register
# ("00000100000000000000001010000000")
# ("00000100000000000000000101000000")
# ("0000010000000000000000010111111")

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


            if 'ADDI' in user_input_split or 'ADD' in user_input_split:
                result = self.addi(user_input_split)
                if type(result) == str:
                    print(result)
                else:
                    pass 

            if 'SUB' in user_input_split or 'SUBI' in user_input_split:
                result = self.subi(user_input_split)
                if type(result) == str:
                    print(result)
                else:
                    pass 
                    
            if 'MUL' in user_input_split or 'MULT' in  user_input_split:
                result = self.multi(user_input_split)
                if type(result) == str:
                    print(result)
                else:
                    pass 

            if 'DIV' in user_input_split or 'DIVT' in user_input_split:
                result = self.multi(user_input_split) 
                if type(result) == str:
                    print(result)
                else:
                    pass 
            
            if 'LW' in user_input_split:
                result = self.lw(user_input_split)
                if type(result) == str:
                    print(result)
                else:
                    pass   

            elif 'SW' in user_input_split:
                result = self.sw(user_input_split)
                if type(result) == str:
                    print(result)
                else:
                    pass

            elif 'XOR' in user_input_split:
                result = self.xor(user_input_split)
                if type(result) == str:
                    print(result)
                else:
                    pass

            elif 'J' in user_input_split:
                result = self.j(user_input_split)
                if type(result) == str:
                    print(result)
                else:
                    pass


    
    def xor(self, input_list):
        desired_register = 0 
        for character in input_list:
            if character == 1:
                desired_val = input_list[character]
                if '$' in desired_val:
                    desired_val = desired_val.strip('$')
                    desired_register = int(desired_val)
                else:
                    return 'invalid command'

            elif character > 1:
                break
            else:
                continue
        
        try:
            self.system.number_registers[desired_register] = []
            print("{} register has been resetted completely".format(desired_register))
            return True
        except:
            return 'invalid command'
        

        


    
    def sw(self, input_list):
        root_register = 0 
        root_register_idx = 0 
        desired_register = 0 
        desired_register_idx = 0 

        for character in range(len(input_list)):
            if character == 1:
                root_register_sample = input_list[character]
                root_register_sample = root_register_sample.strip(', ') 
                if '$' in root_register_sample:
                    root_register = root_register_sample.strip('$')
                    root_register = int(root_register)
                else:
                    return 'invalid command'

            elif character == 2:
                root_idx_sample = input_list[character]
                if '[' in root_idx_sample or ']' in root_idx_sample:
                    root_idx_sample = root_idx_sample.strip('], ')      
                    root_idx_sample = root_idx_sample.strip('[')
                    root_register_idx = int(root_idx_sample)
                else:
                    return 'invalid command'  
            elif character == 3:
                desired_register_sample = input_list[character]
                if '(' in desired_register_sample or ')' in desired_register:
                    desired_register_sample = desired_register_sample.strip('), ')
                    desired_register_sample = desired_register_sample.strip('(')
                    if '$' in desired_register_sample:
                        desired_register_sample = desired_register_sample.strip('$')
                        desired_register = int(desired_register_sample)
                    else:
                        return 'invalid command'
                else:
                    return 'invalid command'

            elif character == 4:
                desired_reg_idx = input_list[character]
                if '[' in desired_reg_idx or ']' in desired_reg_idx:
                    desired_reg_idx = desired_reg_idx.strip('], ')
                    desired_reg_idx = desired_reg_idx.strip('[')
                    desired_register_idx = int(desired_reg_idx)
                else:
                    return 'invalid command'

        try:
            root_register_lst = self.system.number_registers[root_register]
            root_value = root_register_lst[root_register_idx]

            desired_register_lst = self.system.number_registers[desired_register]
            
            desired_register_lst.append(root_value)

            print("{} has been saved to the register {}".format(root_value, desired_register))
            return True

        except:
            return 'invalid command'        


    def lw(self, input_lst):
        destination_register = 0 
        desired_register = 0 
        desired_register_idx = 0

        for character in range(len(input_lst)):
            if character == 1:
                destination_reg = input_lst[character]
                destination_reg = destination_reg.strip(', ')
                if '$' in destination_reg:
                    destination_reg = destination_reg.strip('$')
                    destination_register = destination_reg
                else:
                    return 'invalid command'
            elif character == 2:
                desired_register = input_lst[character]
                if '(' in desired_register or ')' in desired_register:
                    desired_register = desired_register.strip(', ')
                    desired_register = desired_register.strip('(')
                    desired_register = desired_register.strip(')')
                    if '$' in desired_register:
                        desired_register = desired_register.strip('$')
                    else:
                        return 'invalid command'
            elif character == 3:
                des_reg_idx = input_lst[character]
                if '[' in des_reg_idx or ']' in des_reg_idx:
                    des_reg_idx = des_reg_idx.strip(']')
                    des_reg_idx = des_reg_idx.strip('[')
                    desired_register_idx = int(des_reg_idx)
                else:
                    return 'invalid command'
            
            else:
                continue 
        

        try:
            register = self.system.number_registers[int(desired_register)]
            desired_val = register[desired_register_idx]

            destination_register_lst = self.system.number_registers[int(destination_register)]
            destination_register_lst.append(desired_val)
            print("{} has been added to register {}".format(desired_val, destination_register))
            return True 
        
        except:
            return "{} register did not save successfully - index error".format(destination_register)

            
               
            

    def addi(self, input_lst):                          # Format ADDI $1, [idx1], $2, [idx2], Const_val
        destination_register = 0                        # Third Root needs to specified 
        destination_idx = 0                             
        register_root = 0 
        register_root_idx = 0 
        third_root = None
        third_root_idx = None
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
            if input_lst[0] == 'ADDI':  
                if character == 5:
                    if '$' in input_lst[character]:
                        return 'command invalid'
                    else:
                        val = int(input_lst[character])
            elif input_lst[0] == 'ADD':
                if character == 5:
                    if '$' in input_lst[character]:
                        third_root_cleaned = input_lst[character].strip(', ')
                        third_root_cleaned = third_root_cleaned.strip('$')
                        third_root = third_root_cleaned
                    else:
                        return 'invalid command'
                elif character == 6:
                    third_register_idx = input_lst[character]
                    if '[' in third_register_idx or ']' in third_register_idx:
                        third_register_idx = third_register_idx.strip('], ')
                        third_register_idx = third_register_idx.strip('[')
                        third_root_idx = int(third_register_idx)
            else:
                continue 
    
        destination_register_lst = self.system.number_registers[int(destination_register)]
        if destination_idx >= len(destination_register_lst):
            return 'invalid command'
        
        root_register_lst = self.system.number_registers[int(register_root)]
        if register_root_idx > len(root_register_lst):
            return 'invalid command'
        root_value = root_register_lst[register_root_idx]
        try:
            if third_root == None:
                
                summation = val + root_value 
            else:
                third_register_lst = self.system.number_registers[int(third_root)]
                third_register_val = third_register_lst[third_root_idx]

                summation = root_value + third_register_val
            destination_register_lst.append(summation)
            self.system.store_to_history_register(summation)
            print('{} has been added succesfully to the register: {}'.format(summation, destination_register))
            return True
        
        except IndexError:
            return 'there is no value in register {}'.format(register_root)

    
    def subi(self, input_lst):                          # Format ADDI $1, [idx1], $2, [idx2], Const_val
        destination_register = 0                        # Third Root needs to specified 
        destination_idx = 0                             
        register_root = 0 
        register_root_idx = 0 
        third_root = None
        third_root_idx = None
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
            if input_lst[0] == 'SUBI':  
                if character == 5:
                    if '$' in input_lst[character]:
                        return 'command invalid'
                    else:
                        val = int(input_lst[character])
            elif input_lst[0] == 'SUB':
                if character == 5:
                    if '$' in input_lst[character]:
                        third_root_cleaned = input_lst[character].strip(', ')
                        third_root_cleaned = third_root_cleaned.strip('$')
                        third_root = third_root_cleaned
                    else:
                        return 'invalid command'
                elif character == 6:
                    third_register_idx = input_lst[character]
                    if '[' in third_register_idx or ']' in third_register_idx:
                        third_register_idx = third_register_idx.strip('], ')
                        third_register_idx = third_register_idx.strip('[')
                        third_root_idx = int(third_register_idx)
            else:
                continue 
    
        destination_register_lst = self.system.number_registers[int(destination_register)]
        if destination_idx >= len(destination_register_lst):
            return 'invalid command'
        
        root_register_lst = self.system.number_registers[int(register_root)]
        if register_root_idx > len(root_register_lst):
            return 'invalid command'
        root_value = root_register_lst[register_root_idx]
        try:
            if third_root == None:
                
                summation = val - root_value 
            else:
                third_register_lst = self.system.number_registers[int(third_root)]
                third_register_val = third_register_lst[third_root_idx]

                summation = root_value - third_register_val
            destination_register_lst.append(summation)
            self.system.store_to_history_register(summation)
            print('{} has been added succesfully to the register: {}'.format(summation, destination_register))
            return True
        
        except IndexError:
            return 'there is no value in register {}'.format(register_root)

    
    def mult(self, input_lst):                          # Format ADDI $1, [idx1], $2, [idx2], Const_val
        destination_register = 0                        # Third Root needs to specified 
        destination_idx = 0                             
        register_root = 0 
        register_root_idx = 0 
        third_root = None
        third_root_idx = None
        val = 0
        for character in range(len(input_lst)):
            if input_lst[0] == 'MULT':
                if character == 5:
                    break
            elif character == 1:
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
                    third_root_cleaned = input_lst[character].strip(', ')
                    third_root_cleaned = third_root_cleaned.strip('$')
                    third_root = third_root_cleaned
                else:
                    return 'invalid command'
            elif character == 6:
                third_register_idx = input_lst[character]
                if '[' in third_register_idx or ']' in third_register_idx:
                    third_register_idx = third_register_idx.strip('], ')
                    third_register_idx = third_register_idx.strip('[')
                    third_root_idx = int(third_register_idx)
            else:
                continue 
    
        destination_register_lst = self.system.number_registers[int(destination_register)]
        if destination_idx >= len(destination_register_lst):
            return 'invalid command'
        
        root_register_lst = self.system.number_registers[int(register_root)]
        if register_root_idx > len(root_register_lst):
            return 'invalid command'
        root_value = root_register_lst[register_root_idx]
        try:
            if third_root == None:
                product = root_value * destination_register_lst[destination_idx]
                print('Computed Product: {}'.format(product))
            else:
                third_register_lst = self.system.number_registers[int(third_root)]
                third_register_val = third_register_lst[third_root_idx]

                product = root_value * third_register_val
                destination_register_lst.append(product)
                self.system.store_to_history_register(product)
                print('{} has been added succesfully to the register: {}'.format(product, destination_register))
                return True
            
        except IndexError:
            return 'there is no value in register {}'.format(register_root)


    def div(self, input_lst):                          # Format ADDI $1, [idx1], $2, [idx2], Const_val
        destination_register = 0                        # Third Root needs to specified 
        destination_idx = 0                             
        register_root = 0 
        register_root_idx = 0 
        third_root = None
        third_root_idx = None
        val = 0
        for character in range(len(input_lst)):
            if input_lst[0] == 'DIVT':
                if character == 5:
                    break
            elif character == 1:
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
                    third_root_cleaned = input_lst[character].strip(', ')
                    third_root_cleaned = third_root_cleaned.strip('$')
                    third_root = third_root_cleaned
                else:
                    return 'invalid command'
            elif character == 6:
                third_register_idx = input_lst[character]
                if '[' in third_register_idx or ']' in third_register_idx:
                    third_register_idx = third_register_idx.strip('], ')
                    third_register_idx = third_register_idx.strip('[')
                    third_root_idx = int(third_register_idx)
            else:
                continue 
    
        destination_register_lst = self.system.number_registers[int(destination_register)]
        if destination_idx >= len(destination_register_lst):
            return 'invalid command'
        
        root_register_lst = self.system.number_registers[int(register_root)]
        if register_root_idx > len(root_register_lst):
            return 'invalid command'
        root_value = root_register_lst[register_root_idx]
        try:
            if third_root == None:
                divisor = root_value / destination_register_lst[destination_idx]
                print('Computed Divisor: {}'.format(divisor))
            else:
                third_register_lst = self.system.number_registers[int(third_root)]
                third_register_val = third_register_lst[third_root_idx]

                divisor = root_value / third_register_val
                destination_register_lst.append(divisor)
                self.system.store_to_history_register(divisor)
                print('{} has been added succesfully to the register: {}'.format(divisor, destination_register))
                return True
            
        except IndexError:
            return 'there is no value in register {}'.format(register_root)



 
process = Script()
print(process.running())
        

       

