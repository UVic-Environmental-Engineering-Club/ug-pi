from setuptools import find_packages, setup

package_name = "Low_Level_Mission_Planner"

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
    maintainer="Anthony Cieri", "David Kim",
    maintainer_email="penguinmillion@gmail.com", "daehwankim@uvic.ca",
    description="Package for reading and publishing data received from the onboard sensors.",
    license="MIT",
    tests_require=["pytest"],
    entry_points={
        "console_scripts": [
            "depth_sensor = Low_Level_Mission_Planner.depth_sensor:main",
            "fsm = Low_Level_Mission_Planner.fsm:main",
        ],
    },
)
