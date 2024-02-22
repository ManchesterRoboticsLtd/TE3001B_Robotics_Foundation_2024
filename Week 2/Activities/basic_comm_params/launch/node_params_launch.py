import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    config = os.path.join(
        get_package_share_directory('basic_comm_params'),
                                    'config',
                                    'params.yaml')

    param_node = Node(
        package='basic_comm_params',
        executable='node_params',
        name = 'example_node_params',
        output='screen',
        parameters=[config]
    )

    l_d = LaunchDescription([param_node])
    return l_d