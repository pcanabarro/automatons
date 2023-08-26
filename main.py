def even_number_of_zeros_automaton(string):
    current_state = 0
    for symbol in string:
        if current_state == 0 and symbol == '0':
            current_state = 1
        elif current_state == 1 and symbol == '0':
            current_state = 0
            
    return current_state == 0


def main():
    input_filename = "input_file.txt"
    try:
        with open(input_filename, "r") as file:
            input_strings = file.readlines()
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
        return
    
    for string in input_strings:
        string = string.strip() 
        if even_number_of_zeros_automaton(string):
            print(f"'{string}' accepted")
        else:
            print(f"'{string}' rejected.")

main()
