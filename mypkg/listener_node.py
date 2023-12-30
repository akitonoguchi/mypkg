import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

class ListenerNode(Node):

    def __init__(self):
        super().__init__('listener')
        self.subscription = self.create_subscription(
            Int16, 'random_number', self.listener_callback, 10)
        self.subscription  # prevent unused variable warning

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


def main(args=None):
    rclpy.init(args=args)
    listener_node = ListenerNode()
    rclpy.spin(listener_node)
    listener_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

