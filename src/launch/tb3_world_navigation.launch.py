from launch import LaunchDescription
from launch_ros.actions import Node
import os
from ament_index_python.packages import get_package_share_directory
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():
    config_dir = os.path.join(get_package_share_directory('my_autonomous_car'), 'config')
    map_file = os.path.join(config_dir, 'robot_world.yaml')
    param_file = os.path.join(config_dir, 'robot_navigation_params.yaml')
    rviz_config = os.path.join(config_dir, 'robot_navigation_view.rviz')
    
    return LaunchDescription([

    # Bringing up our robot
    IncludeLaunchDescription(
        PythonLaunchDescriptionSource([get_package_share_directory('turtlebot3_gazebo'), '/launch','/turtlebot3_world.launch.py'])
    
    ),
    # Integrating nav2 stack
    IncludeLaunchDescription(
        PythonLaunchDescriptionSource([get_package_share_directory('nav2_bringup'), '/launch','/bringup_launch.py']),
        launch_arguments={
        'map': map_file,
        'params_file': param_file}.items(),
                                                             
    ),

    # rviz2 bringup
    Node(
        package='rviz2',
        output='screen',
        executable='rviz2',
        name='rviz2_node',
        arguments=['-d', rviz_config]   
            
    ),

    ])
