from korok import VecDataBase
import openai
import json
from backend.llm.llm_agent import Conversation
import os 

os.environ["TOKENIZERS_PARALLELISM"] = "false"
DATA_PATH=['./datasets/tea.json','./datasets/ju_hackathon_train_data.json']
SYSTEM_DEFAULT_PROMPT = '做出专业的中医诊断，写出【按语】做出解释。根据查找出的相近病案和茶饮数据，写出【茶饮】返回茶饮药名，编号，功效，组成，适应症，按语，方源，和制作方法'

class Korok:
    def __init__(self, system_prompt=SYSTEM_DEFAULT_PROMPT, threshold=0.6, top_n=3, db_paths =DATA_PATH, update_db=False) -> None:
        self.convo = Conversation(system_prompt)
        self.v = VecDataBase(db_paths, update_db)
        self.threshold = threshold
        self.top_n = top_n

    def custom_system_prompt(self, user_input): #need to change depending on the project

        result, score = self.v.search_db(user_input, './datasets/ju_hackathon_train_data.json', threshold = self.threshold, top_n = self.top_n)
        result1, score1 = self.v.search_db(user_input, './datasets/tea.json', threshold = self.threshold, top_n = 1)
        
        return [result, result1], [score, score1]
       
    def chat_api_v2(self, user_input):

        loc1_found_db_texts, scores = self.custom_system_prompt(user_input)

        local_db_text = "查找出的相近病案和茶饮数据："
        for x in loc1_found_db_texts:
            local_db_text += x
 
        print(f"查找出的相近病案和茶饮数据：{local_db_text.encode('utf-8')} ")
        print(f"Score: {scores}") 
        
        output = self.convo.rolling_convo(user_input, local_db_text)
        
        return output


def recommend(user_input):
    recommendation = korok.chat_api_v2(user_input)
    return recommendation

if __name__ == "__main__":

    korok = Korok(threshold=0.6)
    user_input = 'green tea'
    recommendation = korok.chat_api_v2(user_input)