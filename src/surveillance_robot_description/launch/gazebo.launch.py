from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():

    pkg_path = get_package_share_directory('surveillance_robot_description')
    urdf_file = os.path.join(pkg_path, 'urdf', 'robot.urdf')

    return LaunchDescription([

        # Start Gazebo
        ExecuteProcess(
            cmd=['gazebo', '--verbose'],
            output='screen'
        ),

        # Spawn Robot
        Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            arguments=['-entity', 'surveillance_robot',
                       '-file', urdf_file],
            output='screen'
        ),
    ])
