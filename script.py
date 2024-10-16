from dotenv import load_dotenv
import os

def organize_thousands(lines):
    '''
    This function receives a list of strings and returns a list of strings with the thousands separator organized.

    Like, if there is a number like 1.000,00, it will be transformed into 1000,00.

    csv files reader have a problem with the thousands separator, if it is not consistent.

    :param lines: list of strings
    '''

    processed_lines = []
    for line in lines:
        new_line = ''
        i = 0
        while i < len(line):
            if line[i] == '.' and i + 4 < len(line) and line[i + 4] == ',':
                new_line += ''
                i += 1
            else:
                new_line += line[i]
                i += 1
        processed_lines.append(new_line)
    return processed_lines

def substitute_commas(lines):
    '''
    This function receives a list of strings and returns a list of strings with the commas substituted by dots and semicolon substituted by commas.

    Banco Inter csv files are not separated by commas, but by semicolons. And the decimal separator is a comma.

    :param lines: list of strings
    '''

    first_processed_lines = []
    for line in lines:
        new_line = ''
        for char in line:
            if char == ',':
                new_line += '.'
            else:
                new_line += char
        first_processed_lines.append(new_line)
    
    processed_lines = []
    for line in first_processed_lines:
        new_line = ''
        for char in line:
            if char == ';':
                new_line += ','
            else:
                new_line += char
        processed_lines.append(new_line)


    return processed_lines

def formate_csv (input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()
    
    lines = lines[6:]
    pre_processed_lines = organize_thousands(lines)
    processed_lines = substitute_commas(pre_processed_lines)

    with open(output_file, 'w') as file:
        file.writelines(processed_lines)


if __name__ == "__main__":
    load_dotenv()
    month = os.getenv("MONTH")
    input_file = f"/Users/joaovitormesquita/Desktop/Workspace/financeManager/input.csv"
    output_file = f"/Users/joaovitormesquita/Desktop/Workspace/financeManager/Inter_{month}.csv"
    formate_csv(input_file, output_file)