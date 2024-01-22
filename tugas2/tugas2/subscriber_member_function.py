import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        self.subscription1 = self.create_subscription(
            String,
            'topic1',
            self.listener_callback1,
            10)
        self.subscription1 

        self.subscription2 = self.create_subscription(  
            String,
            'topic2',
            self.listener_callback2,
            10)
        self.subscription2

        self.received1 = None
        self.received2 = None
        
    def listener_callback1(self, msg):
        self.received1 = msg.data

    def listener_callback2(self, msg):
        self.received2 = msg.data
        self.check()

    def check(self):
        if self.received1 == 'True' and self.received2 == 'True':
            self.get_logger().info(f'pub1 - {self.received1} | pub2 - {self.received2} -> sudah siap nih gass min!')
        else:
            self.get_logger().info(f'pub1 - {self.received1} | pub2 - {self.received2} -> tunggu dulu, kami belum ready!')
        self.received1 = None
        self.received2 = None

def main(args=None):
    rclpy.init(args=args)
    minimal_subscriber = MinimalSubscriber()
    rclpy.spin(minimal_subscriber)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
