class Machine:
    """
    string - word that will be handled
    lent - infinity void symbols in left and right direction with our word
    limits - limit to infinity of void symbols
    instructions - dictionary of instructions for handled word:
        state - first key in dict - this is present state of handler
        letter - second key in dict - this is present letter in handled word
            replace_letter - the value in letter key for replacement
            direction - the value in letter key for set direction of handler
            replace_state - the value in letter key for replacement of handler's state
    """

    def __init__(self, string="", instructions=None):
        if instructions is None:
            instructions = {}
        self.string = string
        self.limits = 20
        self.lent = "λ" * self.limits + self.string + "λ" * self.limits
        self.instructions = instructions

    def set_word(self, word: str) -> None:
        """
        Set the value of word and lent for handler

        :param word: str
        :return None
        """
        self.string = word
        self.lent = "λ" * self.limits + self.string + "λ" * self.limits

    def add_instruction(self, state: str, letter: str, replace_letter: str, direction: str, replace_state: str):
        """
        Addition one instruction to handler dictionary of instructions

        :param state:
        :param letter:
        :param replace_letter:
        :param direction:
        :param replace_state:
        :return:
        """
        # Direction may be only R (Right), L (Left), E (Empty)
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
        """
        Start machine work and return the handler's result

        :return:
        """
        position = self.limits   # Because all left symbols before limits is void
        state = "q1"             # Start state
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
            if state == '!':     # State '!' mean stop of handler's work
                return self.lent
