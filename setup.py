from setuptools import find_packages, setup

package_name = 'ros2_camera'

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
    maintainer='c3hod',
    maintainer_email='c3hodgins@gmail.com',
    description='Camera Package for ROS2 in python',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'camera_node = ros2_camera.camera_node:main'
        ],
    },
)
