"""
    Demo subscriber Node.
    Written by Anthony Cieri penguinmillion@gmail.com etc etc whatever

    My code is beautiful, readable, and perfect, comments are not necessary.

    I'm hungry
"""

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32 as depth_sensor_interface

"""
    Init the depthSensorNode class and spin it.
"""


def main(args=None):
    rclpy.init(args=args)
    node = demoSubscriberNode()
    rclpy.spin(node)
    rclpy.shutdown()


"""
    Node that periodically publishes depth sensor data to the /sensors/depth topic

    TODO: Error handling
"""


class demoSubscriberNode(Node):
    def __init__(self):
        super().__init__("demo_sub")

        # Create publisher for data
        self.demo_subscriber_ = self.create_subscription(
            depth_sensor_interface, "/sensors/depth", self.demo_callback, 10
        )

        # Advertise that the node has started
        # TODO: Standardize log messages with other team members
        self.get_logger().info("Demo subscriber node started")

    # Publish the data
    def demo_callback(self, msg: depth_sensor_interface):
        self.get_logger().info(str(msg))
