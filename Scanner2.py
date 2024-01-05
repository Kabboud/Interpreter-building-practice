def gettoken():
    state = 0
    tokens = [None, None, None, "INTEGER", None, None, "DECIMAL", "ERROR"]
    nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    while isFinalState(state) is False:
        c = getChar()     # Grabs a character from the input stream

        if c in nums:
            value = int(c)
        elif c == ".":
            value = 10
        else:
            value = 11

        state = getNextState(state, value)

    if isConsumingState(state) is False:
        putBackChar()     # Places the character back in the input stream

    return tokens[state]


def getNextState(state, c):  # Table Based Scanner
    nextStates = [
        # 0 1  2  3  4  5  6  7  8  9  .  other       <-------- INPUTS
        [1, 2, 2, 2, 2, 2, 2, 2, 2, 2],         # State 0 transitions
        [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 3],   # State 1 transitions
        [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 4, 3],   # State 2 transitions
        [],                                     # State 3 transitions
        [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 7, 7],   # State 4 transitions
        [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7],   # State 5 transitions
        [],                                     # State 6 transitions
        []                                      # State 7 transitions
    ]
    return nextStates[state][c]


def isConsumingState(state):
    if state == 6:
        return True
    return False


def isFinalState(state):
    finalStates = [3, 6, 7]

    if state in finalStates:
        return True
    return False
