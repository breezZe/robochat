from robochat.robot_client_wrapper import RobotClientWrapper

class RobotClientModule(RobotClientWrapper):
    def __init__(self) -> None:
        super().__init__()

        self.current_pose = [0.0,0.0,0.0]
    
    def moveto(self, position):
        print(position)
        
    def turn(self, angle:float) -> None:
        print(angle)
    
    def current_pose(self) -> list:
        print("Current pose is ",self.current_pose)
    
    def stop(self) -> None:
        print("stopping robot.")

    def get_point_pose(self, point_name: str) -> list:
        print(f"Getting point pose of {point_name}")
    