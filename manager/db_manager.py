import json


class Manager:
    def __init__(self, path_file="./files/config.json"):
        self.path_file = path_file

        try:
            with open(path_file, 'r') as file:
                self.config = json.load(file)
        except FileNotFoundError:
            print(f"File {path_file} can't found. Try download...")
            self.back_to_default()
            exit()

    def set_memory(self, memory=[]):
        self.config['memory'] = memory
        open(self.path_file, 'w').write(json.dumps(self.config))
        return 'success'
    
    def set_history(self, history=bool):
        self.config['history'] = True if history in [True, 'True', 'true', 'ture', 1] else False
        open(self.path_file, 'w').write(json.dumps(self.config))
        return 'success'
    
    def set_instruction(self, instruction=""):
        self.config['instruction'] = str(instruction)
        open(self.path_file, 'w').write(json.dumps(self.config))
        return 'success'
    
    def set_temperature(self, temperature=1.5):
        self.config['parameters']['temperature'] = temperature
        open(self.path_file, 'w').write(json.dumps(self.config))
        return 'success'
    
    def set_min_p(self, min_p=1.5):
        self.config['parameters']['min_p'] = min_p
        open(self.path_file, 'w').write(json.dumps(self.config))
        return 'success'
    
    def set_last_message(self, message):
        self.config['messages']['last_message'] = {
            "id": message[0],
            "text": message[1]
        }
        open(self.path_file, 'w').write(json.dumps(self.config))
        return 'success'



    def get_memory(self):
        return self.config['memory']
    
    def get_history(self):
        return self.config['history']
    
    def get_instruction(self):
        return self.config['instruction']
    
    def get_temperature(self):
        return self.config['parameters']['temperature']
    
    def get_min_p(self):
        return self.config['parameters']['min_p']
    
    def get_last_message(self) -> dict:
        """ Возвращает последнее сообщение. Пример:\n
        <code> {"id": 0, "message": "ai answer"} </code>"""
        return self.config['messages']['last_message']

    def get_token(self):
        return self.config['token']



    def back_to_default(self):
        import requests

        url = "https://raw.githubusercontent.com/MrStewie404/LLM_Playground/main/files/config_restore.json"
        response = requests.get(url)

        if response.status_code == 200:
            print("File has been received! I'll try saving them...")
            try:
                open("config.jsonl", "wb").write(response.content)
                print("")
            except Exception as e:
                print(f"Error occurred during saving: {e}")

        else:
            print(f"Problem: {response.status_code}. Try again later?")

if __name__ == "__main__":
    yes_answers = ['y', 'yes', '1']
    answer = input(f"U wanna restore data? (y/n)\n[{'/'.join(yes_answers)}]:")
    if answer in yes_answers:
        answer = input(f"You'r exist config can't be restore. Continue?\n[{'/'.join(yes_answers)}]:")
        if answer in yes_answers:
            Manager().back_to_default()

    else:
        print('Maybe u say no')