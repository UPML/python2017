class SlipDecoder:
    states = {
        0: "not_started",
        1: "operate",
        2: "end_operate",
        3: "shield"
    }

    def __init__(self):
        self.current_package = ''
        self.decode_state = self.states[0]

    def operate_symbol(self, symbol):
        if self.decode_state == self.states[0]:
            if symbol == '~':
                self.decode_state = self.states[1]
            else:
                return False
        elif self.decode_state == self.states[1]:
            if symbol == '|':
                if len(self.current_package) > 0:
                    self.packages.append(self.current_package)
                self.current_package = ''
                self.decode_state = self.states[0]
            elif symbol == '}':
                self.decode_state = self.states[3]
            else:
                self.current_package += symbol
        elif self.decode_state == self.states[3]:
            self.decode_state = self.states[1]
            self.current_package += chr(32 ^ ord(symbol))
        return True

    def decode_message(self, input_message):
        self.packages = []
        old_cur_package = self.current_package
        for s in input_message:
            if not self.operate_symbol(s):
                self.current_package = old_cur_package
        return self.packages

# decoder = SlipDecoder()
# print(decoder.decode_message('~hell'))
# print(decoder.decode_message('o'))
# print(decoder.decode_message('|'))
# print(decoder.decode_message('~hello|cruel world~again|'))
