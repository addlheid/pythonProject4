prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
prompt += "\n..........................."
prompt += "\n"
message = ""

while message != 'out':
    message = input(prompt)
    print(message)