import openai
client = openai.OpenAI()

def translate_chinese_to_english1(chinese_text):
    openai.api_key = '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'  # Replace with your OpenAI API key

    try:
        response = client.chat.completions.create(
          model="gpt-3.5-turbo",  # You can choose the latest available engine
          prompt=f"Translate the following Chinese text into English:\n\n{chinese_text}\n\n",
          max_tokens=60  # Adjust as needed based on the length of the output
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return str(e)

def translate_chinese_to_english(chinese_text):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Translate the following Chinese text into English:\n\n{chinese_text}"},
        ]
    )
    return response['choices'][0]['message']['content']

# Example usage
chinese_text = "根据病患的个人信息，如年龄，性别，工作，以及提供的病情描述，做出专业的中医诊断并且开出治疗方案和治疗处方，写出【按语】做出解释。"
english_translation = translate_chinese_to_english(chinese_text)
print(english_translation)
