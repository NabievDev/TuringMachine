class Machine:
    def __init__(self, string="", instructions=None):
        if instructions is None:
            instructions = {}
        self.string = string
        self.limits = 20
        self.lent = "λ" * self.limits + self.string + "λ" * self.limits
        self.alphabet = set(self.string)
        self.instructions = instructions

    def set_word(self, word: str):
        self.string = word

    def add_instruction(self, state: str, letter: str, replace_letter: str, direction: str, replace_state: str):
        if direction not in ("R", "L", "E"):
            return Exception("Direction of machine should be any R, L or E")

        if state not in self.instructions:
            self.instructions[state] = {}

        self.instructions[state][letter] = {
            "replace_letter": replace_letter,
            "direction": direction,
            "replace_state": replace_state
        }

    def start_machine(self):
        position = self.limits
        state = "q1"
        iterations = 0

        while iterations <= 100:
            letter = self.lent[position]
            replace_state = self.instructions[state][letter]["replace_state"]

            replace_letter = self.instructions[state][letter]["replace_letter"]
            direction = self.instructions[state][letter]["direction"]

            self.lent = self.lent[:position] + replace_letter + self.lent[position + 1:]
            if direction == "R":
                position += 1
            elif direction == "L":
                position -= 1

            iterations += 1
            if iterations >= 100:
                return Exception("Upper than 100 iterations")

            state = replace_state
            if state == '!':
                return self.lent
