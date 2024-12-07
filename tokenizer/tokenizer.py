import json
import re

class Tokenizer:

    def __init__(self, alphabet = "abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщъыьэюяәіңғүұқөһ1234567890!@#$%^&*()_+=-?/>.<,`|\\\'\"[]{} "):

        self.alphabet = alphabet


    def generate_tokens(self):
        result1 = {}
        result2 = {} 
        counter = 1
        n = len(self.alphabet)
        for r in range(1, 4):
            for i in range(n):
                if r == 1:
                    key = self.alphabet[i]
                    result1[key] = counter
                    result2[counter] = key
                    counter += 1
                elif r == 2:
                    for j in range(n):
                        key = self.alphabet[i] + self.alphabet[j]
                        result1[key] = counter
                        result2[int(counter)] = key
                        counter += 1
                        
        with open("tokens_encode.json", 'w', encoding='utf-8') as file:
            json.dump(result1, file, ensure_ascii=False, indent=4)

        with open("tokens_decode.json", 'w', encoding='utf-8') as file:
            json.dump(result2, file, ensure_ascii=False, indent=4)


    def encode(self, text, tokens_dict_path_e):
        with open(tokens_dict_path_e, 'r', encoding='utf-8') as file:
            tokens = json.load(file)

        text = text.lower()
        text = [text[i:i+2] for i in range(0, len(text), 2)]
        encoded_text = []
        
        for el in text:
            encoded_text.append(tokens[el])

        return encoded_text



    def decode(self, encoded_text, tokens_dict_path_d):
        with open(tokens_dict_path_d, 'r', encoding='utf-8') as file:
            tokens = json.load(file)

        decoded_text = ""

        for token in encoded_text:
            decoded_text = decoded_text + tokens[str(token)]
        return decoded_text
