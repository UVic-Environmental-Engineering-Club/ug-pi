#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class DriverSubscriberNode(Node):
    def __init__(self):
        super().__init__("driver_subscriber")

def main(args=None):
    rclpy.init(args=None)

    rclpy.shutdown()

if __name__ == "__main__":
    main()
