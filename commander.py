def move(number_of_steps):
    print("Moved {}".format(number_of_steps))


func_dict = {'move': move}

if __name__ == "__main__":
    input("Press enter to begin.")
    currentEnvironment = "room"  # getNewEnvironment(environments)
    currentTimeOfDay = "1 A.M."  # getTime(timeTicks, timeOfDay)
    print("You are standing in the {0}. It is {1}.".format(
        currentEnvironment, currentTimeOfDay))
    commandInput = input("> ")
    argsStartIndex = commandInput.find('(')
    argsEndIndex = commandInput.find(')')
    command = commandInput[0:argsStartIndex]
    commandArgs = commandInput[argsStartIndex+1:argsEndIndex]
    print(command)
    print(commandArgs)
    func_dict[command](commandArgs)
