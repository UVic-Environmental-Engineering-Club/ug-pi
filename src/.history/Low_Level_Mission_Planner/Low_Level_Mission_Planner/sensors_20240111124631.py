"""
    Finite State Machine to subscribe to sensors and publish to actuators.
    This sensors will be controly by hybrid control system. The structure of the control system is to be determined. My humble guess is that we will be using layered control system structure. PID for low level control and other forms of control for high-level behavior control.
    Written by David Kim daehwankim@uvic.ca
    Based on Demo subscriber Node written by Anthony Cieri penguinmillion@gmail.com. Thank you Anthony!
"""

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32 as depth_sensor_interface
from . import fsm


"""
    Init the depthSensorNode class and spin it.
"""


def main(args=None):
    rclpy.init(args=args)
    node = sensorSubscriberNode()
    fsm.CreateFSM()
    rclpy.spin(node)
    rclpy.shutdown()


"""
    Node that periodically publishes depth sensor data to the /sensors/depth topic

    TODO: Error handling
"""


class sensorSubscriberNode(Node):
    def __init__(self):
        super().__init__("sensors")

        # Create subscription for data. Interface need to be implemented
        self.subscription = self.create_subscription(
            depth_sensor_interface, "/sensors/depth", self.sensors_callback, 10
        )
        self.subscription # prevent unused variable warning

        # Advertise that the node has started
        # TODO: Standardize log messages with other team members
        self.get_logger().info("sensors subscriber node started")

    # listener callback
    def sensors_callback(self, msg: depth_sensor_interface):
        self.get_logger().info(str(msg))
        fsm.CreateAndRunFSM.ReportAndTransition(self)
