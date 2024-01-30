import openai
import os 
from dotenv import load_dotenv
from backend.llm.llm_tools import num_tokens_from_messages, num_tokens_from_string

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
print(OPENAI_API_KEY)
print()

class LLM:
    def __init__(self, system_prompt = 'be a helpful assistant', max_tokens=500, temperature=0, model_name = "gpt-3.5-turbo-1106"):
        self.client = openai.OpenAI(api_key = OPENAI_API_KEY,) 
        self.system_prompt = system_prompt
        self.default_messages = [
            {'role': 'system', 'content': self.system_prompt},
            ]
        self.max_tokens=max_tokens
        self.temperature=temperature
        self.model_name = model_name

    def __example__(self):
        client = openai.OpenAI(api_key = os.environ.get("OPENAI_API_KEY")) 
        completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
            {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
            ]
            )
        print(completion.choices[0].message)
 
    def openai_api(self, messages): #core function
        try:
            response = self.client.chat.completions.create(
                model=self.model_name,
                messages=messages,
                max_tokens=self.max_tokens,
                temperature=self.temperature
            )
            print(response.usage)
            return response.choices[0].message.content, response.usage
        except Exception as e:
            print(f"Error during API call: {e}")
            return None, None

    #construct the messages
    def chat(self, user_input, system_prompt = None):
        if not system_prompt:    
            messages = [
            {'role': 'system', 'content': "be a helpful assistant"},
            ]
        else:
            messages = [
            {'role': 'system', 'content': system_prompt},
            ]
        messages.append({"role": "user", "content": user_input})
        return self.openai_api(messages)
    
    #construct the messages
    def chat_fake(self, user_input, system_prompt = None):
        if not system_prompt:    
            messages = [
            {'role': 'system', 'content': "be a helpful assistant"},
            ]
        else:
            messages = [
            {'role': 'system', 'content': system_prompt},
            ]
        messages.append({"role": "user", "content": user_input})
        return "loopback: "+user_input, num_tokens_from_messages(messages)
        
    def rolling_chat(self, user_input, added_system_prompt = None):
        if added_system_prompt: #for example, custom database
            self.default_messages.append({"role": "system", "content": added_system_prompt})
        self.default_messages.append({"role": "user", "content": user_input})
        return self.openai_api(self.default_messages)
    
if __name__ == "__main__":
    llm = LLM('translate Chinese into English and keep the same format')
    message, usage = llm.chat('你好')
    print(message, usage)
    #CompletionUsage(completion_tokens=1, prompt_tokens=22, total_tokens=23)
