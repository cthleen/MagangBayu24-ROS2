import random
import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher1 = self.create_publisher(String, 'topic1', 10)
        self.publisher2 = self.create_publisher(String, 'topic2', 10)
        timer_period = 1 # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        self.i += 1

        istrue1 = self.i % 2 == 0
        istrue2 = self.i % 3 == 0

        msg1 = String()
        msg1.data = str(istrue1)
        self.publisher1.publish(msg1)
        self.get_logger().info('Publisher - 1 - (%d sec) -> "%s"' % (self.i, msg1.data))
        
        msg2 = String()
        msg2.data = str(istrue2)
        self.publisher2.publish(msg2)
        self.get_logger().info('Publisher - 2 - (%d sec) -> "%s"' % (self.i, msg2.data))

def main(args=None):
    rclpy.init(args=args)
    minimal_publisher = MinimalPublisher()
    rclpy.spin(minimal_publisher)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
