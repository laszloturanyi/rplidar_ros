from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            name='rplidarNode',
            package='rplidar_ros',
            executable='rplidarNode',
            output='screen',
            parameters=[{
                'channel_type': 'tcp',
                'tcp_ip': '192.168.0.7',
                'tcp_port': 20108,
                'frame_id': 'laser',
                'inverted': False,
                'angle_compensate': True,
            }]
        ),
    ])
