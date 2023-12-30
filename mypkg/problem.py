import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16
import random
import time

class problem_publisher(Node):

    def __init__(self):
        super().__init__('talker')
        self.publisher = self.create_publisher(Int16, 'random_number', 10)
        self.timer = self.create_timer(1, self.timer_callback)
        self.start_time = time.time()

    def timer_callback(self):
        elapsed_time = time.time() - self.start_time
        if elapsed_time < 60:
            message = Int16()
            message.data = int(random.randint(0, 999))
            self.get_logger().info('Publishing: %s' % message.data)
            self.publisher.publish(message)
        else:
            self.get_logger().info('finish')
            self.destroy_node()
            rclpy.shutdown()

def main():
    rclpy.init()
    problem = problem_publisher()
    while rclpy.ok():
        rclpy.spin_once(problem, timeout_sec=1)

if __name__ == '__main__':
    main()

