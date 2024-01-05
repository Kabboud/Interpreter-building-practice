def gettoken():
    state = 0
    tokens = [None, None, None, "INTEGER", None, None, "DECIMAL", "ERROR"]

    while isFinalState(state) is False:
        c = getChar()     # Grabs a character from the input stream
        state = getNextState(state, c)

    if isConsumingState(state) is False:
        putBackChar()     # Places the character back in the input stream

    return tokens[state]


def getNextState(state, c):     # Brute Force Scanner
    nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    if state == 0:
        if c == '0':
            return 1
        elif c in nums:
            return 2
    elif state == 1:
        if c == '.':
            return 4
        else:
            return 3
    elif state == 2:
        if c == '.':
            return 4
        elif c in nums or c == "0":
            return 2
        else:
            return 3
    elif state == 4:
        if c in nums or c == "0":
            return 5
        else:
            return 7
    elif state == 5:
        if c in nums or c == "0":
            return 6
        else:
            return 7


def isConsumingState(state):
    if state == 6:
        return True
    return False


def isFinalState(state):
    finalStates = [3, 6, 7]

    if state in finalStates:
        return True
    return False
