from robochat.robot_client_wrapper import RobotClientWrapper
from turtlesim.srv import TeleportRelative,TeleportAbsolute
from turtlesim.msg import Pose
from rclpy.node import Node
from geometry_msgs.msg import Twist
import rclpy

import math
import asyncio,_thread

class RobotClientTurtle(RobotClientWrapper):
    def __init__(self):
        super(RobotClientTurtle, self).__init__()
        rclpy.init()

        self.node = Node('robot_client_turtle')
        # Subscribe to the turtle's pose topic to keep track of its position
        self.subscription = self.node.create_subscription(
            Pose,
            'turtle1/pose',
            self.pose_callback,
            10)
        self.subscription  # prevent unused variable warning

        # Advertise on the turtle's command velocity topic to control its movement
        self.publisher = self.node.create_publisher(Twist, 'turtle1/cmd_vel', 10)
        self.client = self.node.create_client(TeleportAbsolute, 'turtle1/teleport_absolute')
        # Initialize the current pose of the turtle to (0, 0)
        
        self.current_pose = [0.0, 0.0, 0.0]
        self.moveto(self.current_pose)
        _thread.start_new_thread(self.spin,())

    def spin(self):
        # rclpy.spin(self.node)
        pass
    
    def pose_callback(self, msg):
        # Update the current pose of the turtle when a new pose message is received
        # print(msg)
        self.current_pose = [msg.x, msg.y,msg.theta]

    def moveto(self, position):
        request = TeleportAbsolute.Request()
        request.x = float(position[0])
        request.y = float(position[1])
        request.theta = float(position[2])
        future = self.client.call_async(request)
        rclpy.spin_until_future_complete(self.node, future,timeout_sec=1)

        
    def turn(self,angle):
        twist = Twist()
        twist.angular.z = angle
        self.publisher.publish(twist)

    def current_pose(self):
        return self.current_pose
    
    def stop(self):
        twist = Twist()
        twist.linear.x = 0.0
        twist.angular.z = 0.0
        self.publisher.publish(twist)

    def get_point_pose(self, point_name):
        pass

