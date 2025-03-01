import json


class Manager:
    def __init__(self, path_file="./files/config.json"):
        self.path_file = path_file

        try:
            with open(path_file, 'r') as file:
                self.config = json.load(file)
        except FileNotFoundError:
            print(f"File {path_file} not found.")
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
        try:
            self.set_memory([])
            self.set_instruction("")
            self.set_temperature(1.5)
            self.set_min_p(0.5)
            self.set_history(False)
            print('All was back to default!')
        except Exception as e:
            print(f'System return error: {e}. Create a "config.json" if doesn`t exist and try again.')

if __name__ == "__main__":
    answer = input("U wanna restore data? (y/n)\n:")

    if answer == "y":
        Manager().back_to_default()
    else:
        print('Maybe u say no')