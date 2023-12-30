import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16
import time

class answer_subscription(Node):

    def __init__(self):
        super().__init__('listener')
        self.subscription = self.create_subscription(
            Int16, 'random_number', self.listener_callback, 10)
        self.start_time = time.time()

    def listener_callback(self, msg):
        number = msg.data
        is_prime = self.is_prime(number)
        if is_prime:
            self.get_logger().info('%d は素数です' % number)
        else:
            self.get_logger().info('%d は素数ではないです' % number)

    def is_prime(self, n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True


def main():
    rclpy.init()
    answer = answer_subscription()
    while rclpy.ok():
        rclpy.spin_once(answer, timeout_sec=1)


if __name__ == '__main__':
    main()
