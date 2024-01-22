import random
import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(String, 'topic', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        num1 = random.randint(1,100000)
        num2 = random.randint(1,100000)
        num3 = random.randint(1,100000)

        list_op = ['+', '-', '*', '/', '%']
        operator1 = random.choice(list_op)
        operator2 = random.choice(list_op)

        msg = String()
        msg.data = f'{num1} {operator1} {num2} {operator2} {num3}'
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)


def main(args=None):
    rclpy.init(args=args)
    minimal_publisher = MinimalPublisher()
    rclpy.spin(minimal_publisher)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
