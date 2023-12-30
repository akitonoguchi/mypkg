# SPDX-FileCopyrightText: 2023 Akito Noguchi
# SPDX-License-Identifier: BSD-3-Clause
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class FibonacciNode(Node):

    def __init__(self):
        super().__init__('Fibonacci')
        self.publisher = self.create_publisher(Int32, 'fibonacci_number', 10)
        self.timer = self.create_timer(1, self.timer_callback)
        self.current_index = 0

    def timer_callback(self):

        current_number = self.calculate_fibonacci(self.current_index)

        message = Int32()
        message.data = current_number
        self.publisher.publish(message)

        self.get_logger().info('計算結果: {}'.format(current_number))

        self.current_index += 1

    def calculate_fibonacci(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            a, b = 0, 1
            for _ in range(2, n + 1):
                a, b = b, a + b
            return b

def main():
    rclpy.init()
    fibonacci = FibonacciNode()
    rclpy.spin(fibonacci)
    fibonacci.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

