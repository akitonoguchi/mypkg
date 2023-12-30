import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16
import random

class TalkerNode(Node):

    def __init__(self):
        super().__init__('talker')
        self.publisher = self.create_publisher(Int16, 'random_number', 10)
        self.timer = self.create_timer(1, self.timer_callback)

    def timer_callback(self):
        message = Int16()
        message.data = int(random.randint(0, 999))
        self.get_logger().info('Publishing: %s' % message.data)
        self.publisher.publish(message)

def main(args=None):
    rclpy.init(args=args)
    talker_node = TalkerNode()
    rclpy.spin(talker_node)
    talker_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

