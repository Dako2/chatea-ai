def parse_answer_text_to_list(file_path = 'ju_answers.txt'):
    #data = []
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.read().strip().split('\n').split('\t')
    return lines

def parse_text_to_list(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.read().strip().split('\n')
        return ['\n'.join(lines[i:i+2]) for i in range(0, len(lines), 2)]

def main():
    file_path = 'ju_exam.txt'  # Replace with the path to your text file
    try:
        parsed_list = parse_text_to_list(file_path)
        for element in parsed_list:
            print(element)
            print("------")
    except FileNotFoundError:
        print("File not found. Please check the file path.")

if __name__ == "__main__":
    file_path = 'ju_exam.txt'  # Replace with the path to your text file
    try:
        parsed_list = parse_text_to_list(file_path)
        for element in parsed_list:
            print(element[3:])
            print("------")
    except FileNotFoundError:
        print("File not found. Please check the file path.")

