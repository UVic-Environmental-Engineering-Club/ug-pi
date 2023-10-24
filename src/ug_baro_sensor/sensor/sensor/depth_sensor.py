#!/usr/bin/env python3

"""
    Originally written by Anthony Cieri penguinmillion@gmail.com

    This creates a ros2 node that reads from the baromatric
    sensor and publishes the readings to the sensor topic.

    In its current state, this code can be used as a base for any
    sensor node.

    DONE: Create a ros2 node that publishes data to a topic.

    TODO: Develop the sensor topic with Rowan.
    TODO: Decide what types will be published to the topic.

    TODO: Get data from the sensor, requires appropriate libs
            and hardware (raspberry pi and sensor).
"""

import math  # May be removed later
import rclpy  # For ros2
from rclpy.node import Node  # To create the node
from std_msgs.msg import Float32  # TODO: Decide this type

# TODO: Import appropriate modules to interface with the sensor
# TODO: Import appropriate modules for any processing of raw data


"""
    Init the depthSensorNode class and spin it.
"""


def main(args=None):
    rclpy.init(args=args)
    node = depthSensorNode()
    rclpy.spin(node)
    rclpy.shutdown()


"""
    Currently all this does is publish arbitrary floats to a topic.

    TODO: Publish data from sensor
"""


class depthSensorNode(Node):
    def __init__(self):
        super().__init__("depth_sensor")

        # TODO: For demonstration only, replace with real data
        self.data_ = 5.598327

        # Create publisher for data
        self.depth_data_pub_ = self.create_publisher(Float32, "/sensors/depth", 10)

        # Every half second publish data to the topic
        # TODO: How often does this need to be updated?
        self.timer_ = self.create_timer(0.5, self.send_data_callback)

        # Advertise that the node has started
        # TODO: Standardize log messages with other team members
        self.get_logger().info("Depth sensor node started")

    # TODO: Need a method for reading data from sensor

    # Publish the data
    # TODO: Rename to something more clear
    def send_data_callback(self):
        # TODO: Change type
        msg = Float32()

        # TODO: Replace this variable with a method call
        msg.data = self.data_

        # Publish data
        # TODO: Format data
        self.depth_data_pub_.publish(msg)

        # Log data (Debugging)
        # TODO: Remove this, creates noise in log
        self.get_logger().info("Hello " + str(self.data_))

        # TODO: For demonstration only
        self.data_ /= self.data_ + math.modf(self.data_)[1]


"""
    TODO: Create a class to manage sensor data.
            Needs a method to read from sensor
            One to process data
            One to format data
            Maybe one to report status of sensor?

    TODO: How much processing needs to be done?
            Does it publish raw data?
            Calibrated?
            What units?
            Multiple streams of data?
            The sensor can give temp as well as pressure,
                does it need to publish that as well?
"""
