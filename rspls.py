def name_to_number(name):
    """
    Take string name as input (rock-Spock-paper-lizard-scissors)
    and returns integer (0-1-2-3-4)
    """
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4

    
print(name_to_number("rock"))		
print(name_to_number("Spock"))		
print(name_to_number("paper"))		
print(name_to_number("lizard"))	
print(name_to_number("scissors"))	