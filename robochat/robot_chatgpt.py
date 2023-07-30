from revChatGPT.V1 import Chatbot
import re,json,os,sys
from robochat.robot_client_module import RobotClientModule

class colors:  # You may need to change color settings
    RED = "\033[31m"
    ENDC = "\033[m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"

class RobotChatBot():
    def __init__(self,config_file,bot_name='robot',initial_prompt:str=None):
        self.name = bot_name
        try:
            with open(config_file,"r") as f:
                self.config = json.load(f)
            self.chatgpt = Chatbot(config=self.config)
        except Exception as e:
            print(colors.RED + "Loading config file Error: " + str(e) + colors.ENDC)
            sys.exit(1)

        if initial_prompt:
            print("Asking initial prompt...")
            self.ask(initial_prompt)

        print("Welcome to RobotChatBot. Ready to help you.")
        print("You can press",colors.RED, "[Enter] once", colors.ENDC, "to continue your prompt, or press",colors.RED,"[Enter] twice",colors.ENDC,"to send a prompt.")
        
    def extract_python_code(self,content):
        code_block_regex = re.compile(r"```(.*?)```", re.DOTALL)
        code_blocks = code_block_regex.findall(content)
        if code_blocks:
            full_code = "\n".join(code_blocks)
            if full_code.startswith("python"):
                full_code = full_code[7:]
            return full_code
        else:
            return None
        
    def ask(self,prompt):
        for data in self.chatgpt.ask(prompt):
            response = data["message"]

        return response

    def send_prompt(self,prompt):
        response = self.ask(prompt)
        return response

    def interactive_prompt(self):
        response = str()
        while True:
            print(colors.YELLOW,"RoboChat> ",colors.ENDC,end="")
            question = str()
            quit = False
            while not quit:
                d = input()
                if d == '': 
                    quit = True
                else:
                    question+=d

            if question == '':
                continue

            if question == "!quit" or question == "!exit":
                break

            if question == "!clear":
                os.system("cls")
                continue
            
            print(colors.BLUE,"===== wait for response =====",colors.ENDC)
            response = self.ask(question)
            print(colors.BLUE,"chatgpt>",colors.ENDC,f"{response}")

            return response

        
        
    
        