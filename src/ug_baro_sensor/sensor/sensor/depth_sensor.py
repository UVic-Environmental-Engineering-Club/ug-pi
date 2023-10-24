#!/usr/bin/env python3

import math
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

# TODO: Add comments

class depthSensorNode(Node):
    def __init__(self):
        super().__init__("depth_sensor")
        self.data_ = 5.598327

        # Create publisher for data
        # Line split temporarily
        self.depth_data_pub_ \
            = self.create_publisher(Float32, "/sensors/depth", 10)

        self.timer_ = self.create_timer(0.5, self.send_data_callback)
        self.get_logger().info("Depth sensor node started")

    def send_data_callback(self):
        msg = Float32()
        msg.data = self.data_
        self.depth_data_pub_.publish(msg)

        self.get_logger().info("Hello " + str(self.data_))
        self.data_ /= self.data_ + math.modf(self.data_)[1]


def main(args=None):
    rclpy.init(args=args)
    node = depthSensorNode()
    rclpy.spin(node)
    rclpy.shutdown()


# Topic type is a dictionary, expected to change
