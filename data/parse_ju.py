import json

def parse_text(text):
    paragraphs = text.split('\n')  # Assuming paragraphs are separated by new lines
    input_output_pairs = []
    input_paragraph = None

    for i, paragraph in enumerate(paragraphs):
        # Check for input paragraph
        if any(gender in paragraph[:6] for gender in ["男", "女"]):
            input_paragraph = paragraph
            input_start_index = i
        # Check for end of output paragraphs
        elif paragraph.startswith("【按语") and input_paragraph is not None:
            output_paragraphs = paragraphs[input_start_index + 1:i + 1]
            input_output_pairs.append((input_paragraph.strip(), '\n'.join(output_paragraphs).strip()))
            input_paragraph = None
        # Reset input paragraph if it was set in the last iteration
        elif input_paragraph is not None:
            continue

    return input_output_pairs

def read_text_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return "File not found."

def save_list_to_json(data_list, file_path):
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data_list, file, ensure_ascii=False, indent=4)
        return "Data saved successfully to " + file_path
    except Exception as e:
        return f"An error occurred: {e}"

# Usage
file_path = 'ju_hackathon_main_data.txt'  # Replace with your file path
content = read_text_file(file_path)
print(content)

parsed_pairs = parse_text(content)

file_path = 'ju_hackathon_main_data.json'
data_list = []
prompt = "根据病患的个人信息，如年龄，性别，工作，以及提供的病情描述，做出专业的中医诊断并且开出治疗方案和治疗处方，写出【按语】做出解释。"
for pair in parsed_pairs:
    print("Input:", pair[0])
    print("Output:", pair[1])
    print("------")
    data_list.append({"instruction":prompt,"input":pair[0],"output":pair[1]})
        
result = save_list_to_json(data_list, file_path)

