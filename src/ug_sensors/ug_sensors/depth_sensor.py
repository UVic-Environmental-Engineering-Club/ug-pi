#!/usr/bin/env python3

"""
    Originally written by:
        Anthony Cieri penguinmillion@gmail.com

    This creates a ros2 node that reads from the depth
    sensor and publishes the readings to the sensor topic.

    In its current state, this code can be used as a base for any
    sensor node.

    DONE: Create a ros2 node that publishes data to a topic.

    TODO: Develop the sensor interface with David.

    DONE: Get data from the sensor, requires appropriate libs
            and hardware (raspberry pi and sensor).

    TODO: Should a separate node be created for temperature?
"""

import rclpy  # For ros2
from rclpy.node import Node  # To create the node
from std_msgs.msg import (
    Float32 as depth_sensor_interface,
)  # TODO: Create topic interface with David

# Sensor modules
# This should be a module between the actual sensor driver and this script that
# Translates whatever the sensor driver gives to what this script expects
# TODO: What does this script expect? (Specify abstract sensor)
import ug_sensors.ms5837_sensor as sensor_driver


"""
    Init the depthSensorNode class and spin it.
"""


def main(args=None):
    rclpy.init(args=args)
    node = depthSensorNode()
    rclpy.spin(node)
    rclpy.shutdown()


"""
    Node that periodically publishes depth sensor data to the /sensors/depth topic

    TODO: Error handling
"""


class depthSensorNode(Node):
    def __init__(self):
        super().__init__("depth_sensor")

        self.depth_sensor = depthSensor(fresh_water=False)

        # Create publisher for data
        self.depth_data_pub_ = self.create_publisher(
            depth_sensor_interface, "/sensors/depth", 10
        )

        # Every half second publish data to the topic
        # TODO: How often does this need to be updated?
        self.timer_ = self.create_timer(0.5, self.publish_depth_data)

        # Advertise that the node has started
        # TODO: Standardize log messages with other team members
        self.get_logger().info("Depth sensor node started")

    # Publish the data
    def publish_depth_data(self):
        msg = depth_sensor_interface()

        msg.data = self.depth_sensor.read_depth()

        # Publish data
        self.depth_data_pub_.publish(msg)

        # Log data (Debugging)
        self.get_logger().info(str(msg.data))


"""
    Simple class to manage the sensor driver and provide some abstraction

    TODO: Error handling. What happens if __sensor.read() is false?

    __sensor.read() must be called whenever new data is requested,
    but if both depth and temp are wanted simultaniously, theres no
    reason to call read() twice.
"""


class depthSensor:
    # Initalize the physical sensor, returns whether init was successful
    def __init__(self, fresh_water=True):
        self.__sensor = (
            sensor_driver.MS5837_30BA()
        )  # Default I2C bus is 1 (Raspberry Pi 3)

        # We must initialize the sensor before reading it
        if not self.__sensor.init():
            # Sensor could not be initialized
            exit(1)

        # We have to read values from sensor to update pressure and temperature
        if not self.__sensor.read():
            # Sensor read failed!
            exit(2)

        # Freshwater is default, but the glider would usually be in saltwater
        if fresh_water:
            self.__sensor.setFluidDensity(sensor_driver.DENSITY_FRESHWATER)
        else:
            self.__sensor.setFluidDensity(sensor_driver.DENSITY_SALTWATER)

    # Only call read() once for all data
    def read_depth_temp(self) -> tuple[float, float]:
        if self.__sensor.read():
            return (self.__sensor.depth(), self.__sensor.temp())

    # Read the depth in mBar from the sensor
    def read_depth(self) -> float:
        if self.__sensor.read():
            return self.__sensor.depth()

    # Read the temperature in Celcius from the sensor
    def read_temp(self) -> float:
        if self.__sensor.read():
            return self.__sensor.temperature()


"""
    TODO: How much processing needs to be done?
            Multiple streams of data? Depends on the topic interface
            The sensor can give temp as well as pressure,
                does it need to publish that as well? Yes.
"""
