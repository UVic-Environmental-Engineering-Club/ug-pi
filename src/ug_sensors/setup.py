from setuptools import find_packages, setup

package_name = "ug_sensors"

setup(
    name=package_name,
    version="0.0.1",
    packages=find_packages(exclude=["test"]),
    data_files=[
        ("share/ament_index/resource_index/packages", ["resource/" + package_name]),
        ("share/" + package_name, ["package.xml"]),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="Anthony Cieri",
    maintainer_email="penguinmillion@gmail.com",
    description="Package for reading and publishing data received from onboard sensors.",
    license="MIT",
    tests_require=["pytest"],
    entry_points={
        "console_scripts": ["depth_sensor = ug_sensors.depth_sensor:main"],
    },
)
