import launch
import launch.actions
import launch.substitutions
import launch_ros.actions


def generate_launch_description():

    answer = launch_ros.actions.Node(
        package='mypkg',
        executable='answer',
        )
    problem = launch_ros.actions.Node(
        package='mypkg',
        executable='problem',
        output='screen'
        )

    return launch.LaunchDescription([answer, problem])
