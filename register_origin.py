class System:
    def __init__(self):
        self.number_registers = [[] for i in range(21)]
        self.history_registers = [[] for i in range(10)]
        self.number_index = 1
        self.history_index = 0 
        self.temp_history_index = 0
        self.user_display = ''
        self.empty = None

    def update_display(self, to_update):
        if to_update == 'Invalid OPCODE':
            print("Invalid OPCODE")
        else:
            self.user_display = to_update
            print(self.user_display)
            print('-'*24)
            print('\n')

    def store_value_to_register(self, value_to_store):
        if self.number_index >= 21:
            self.number_index = 1
        
        value = self.bin_to_int(value_to_store)
        self.number_registers[self.number_index].append(value)
        print("{value} was added to register {number_add}".format(value=value, number_add=self.number_index))
        self.number_index += 1
        self.empty = True

    def load_value_from_register(self, register_address):
        index = self.bin_to_int(register_address)
        int_value = int(self.number_registers[index])
        return int_value

    def store_to_history_register(self, result_to_store):
        if self.history_index >= 9:
            self.history_index = 0
        bin_history = self.int_to_bin(result_to_store)
        self.store_to_history_register[self.history_index].append(bin_history)
        self.history_index += 1
        self.temp_history_index = self.history_index

 
    def get_last_calculation(self):
        self.temp_history_index -= 1
        val = self.bin_to_int(self.history_registers[self.temp_history_index][-1])
        last_value = "Last value: {}".format(val)
        self.update_display(last_value)

    def binary_reader(self, instruction):
        if len(instruction) == 32:
            opcode = instruction[:6]
            source_one = instruction[6: 11]
            source_two = instruction[11: 16]
            store = instruction[16: 26]
            function_code = instruction[26: 32]

            if opcode == '000001':
                self.store_value_to_register(store)
                return
            elif opcode == '100001':
                self.get_last_calculation()
                return
            elif opcode != '000000':
                self.update_display("Invalid OPCODE")
                return
            
            result = 0
            if function_code == '100000':
                result = self.add(source_one, source_two)
            elif function_code == '100010':
                result = self.subtraction(source_one, source_two)
            elif function_code == '011000':
                result = self.multiply(source_one, source_two)
            elif function_code == '011010':
                result = self.divide(source_one, source_two)
            else:
                print("Invalid Instruction")
            
            self.store_to_history_register(result)
            self.user_display = result

        else:
            print("Invalid Length")
            return

    def int_to_bin(self, integer):
        exponents = []
        counter = 0
        remainder = 0
        mod = 0
        while integer >= 1:
            while mod != 1:
                result_mod = integer // (2 ** counter)
                mod = result_mod
                counter += 1
            counter -= 1
            exponents.append(counter)
            integer = integer - (2 ** counter)
            counter = 0 
            mod = 0
        
        binary_num = ''
        for i in range(max(exponents), -1, -1):
            if i in exponents:
                binary_num += '1'
            else:
                binary_num += '0'
        
        return binary_num
        
        

    def bin_to_int(self, binary):
        binary = str(binary)
        binary_split = []
        for num in range(len(binary) - 1, -1, -1):
            binary_split.append(binary[num])
        max_exponent = len(binary_split)
        
        exponents = []
        for exponent in range(max_exponent - 1, -1, -1):
            if binary_split[exponent] == '1':
                exponents.append(exponent)
            else:
                continue
        
        result = 0 
        for exponent in exponents:
            result += 2 ** int(exponent)
        
        return result






# Test Inputs

'''
test.binary_reader("00000100000000000000001010000000")
test.binary_reader("00000100000000000000000101000000")


test.binary_reader("00000000001000100000000000100000")
test.binary_reader("00000000001000100000000000100010")
test.binary_reader("00000000001000100000000000011000")
test.binary_reader("00000000001000100000000000011010")

test.binary_reader("10000100000000000000000000000000")
test.binary_reader("10000100000000000000000000000000")'''