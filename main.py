from robochat import *
import argparse
import os,sys,time,math
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--name', type=str, default='Robot')
    args = parser.parse_args()

    initial_prompt = "hello"
    
    with open('prompts/turtle_basic.txt', 'r') as f:
        initial_prompt = f.read()
    
    print("Initializing RobotChat...")
    
    # rc = RobotClientModule()
    bot = RobotChatBot('config/config.json',bot_name=args.name)

    while True:
        response = bot.interactive_prompt()
        code = bot.extract_python_code(response)

        if code:
            print("Please wait while I run the code ...")
            print("================================================")
            print(code)
            print("================================================")
            try:
                exec(code)
            except Exception as e:
                print(e)
            finally:
                print("Done!")
