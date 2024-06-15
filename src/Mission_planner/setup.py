from setuptools import find_packages, setup

package_name = 'Mission_planner'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='DavidKim',
    maintainer_email='daehwankim@uvic.ca',
    description='Dynamic and Kinematic mission planner. Control strategy is to be determined',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'fsm = Mission_planner.fsm:main'
        ],
    },
)
