## RoboChat to control robot using chatGPT


### Dependencies

All dependencies is stored in `requirements.txt`. 

### Usage

1. Copy chatGPT session id to `access_token` field in the `config/config.json` file.

2. Implement a client derived from the `RobotClientWrapper` class from `robot_client_wrapper` file.

3. **IMPORTANT** Prepare the initial prompt for the robot.

4. Initialize the robot client in `main.py`.

5. Keep tunning chatGPT with interactive prompts or other interfaces.

