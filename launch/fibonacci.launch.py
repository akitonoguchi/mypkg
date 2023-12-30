import launch
import launch.actions
import launch.substitutions
import launch_ros.actions


def generate_launch_description():

    fibonacci = launch_ros.actions.Node(
        package='mypkg',
        executable='fibonacci',
        )

    return launch.LaunchDescription([fibonacci])
