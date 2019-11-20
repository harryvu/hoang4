while True:
    # ask for a command
    commandInput = input("Enter a command: .")
    argsStartIndex = commandInput.find('(')
    argsEndIndex = commandInput.find(')')
    command = commandInput[0:argsStartIndex]
    print(command)
    print(commandInput[argsStartIndex+1:argsEndIndex])
