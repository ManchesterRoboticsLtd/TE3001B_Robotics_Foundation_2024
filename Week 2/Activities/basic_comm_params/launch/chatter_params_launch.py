from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    talker_node = Node(
        package='basic_comm_params',
        executable='talker_params',
        output='screen',
        parameters=[{'my_param': 'profes!'}]
    )

    l_d = LaunchDescription([talker_node])
    return l_d