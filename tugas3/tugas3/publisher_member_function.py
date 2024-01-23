import rclpy
from rclpy.node import Node
from turtlesim.srv import TeleportAbsolute
from std_srvs.srv import Empty
from geometry_msgs.msg import Twist
import math

class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        # self.pose = self.create_subscription(Pose, 'turtle1/pose', self.pose_callback, 10)
        self.timer = self.create_timer(2.0, self.timer_callback)
        self.count = 0

    def teleport_absolute(self, x, y, theta):
        teleport_service = self.create_client(TeleportAbsolute, '/turtle1/teleport_absolute')
        while not teleport_service.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Waiting for the teleport_absolute service...')

        request = TeleportAbsolute.Request()
        request.x = x 
        request.y = y 
        request.theta = theta  

        future = teleport_service.call_async(request)
        rclpy.spin_until_future_complete(self, future)
        self.get_logger().info('Teleportation complete.')


    def clear_turtlesim(self):
        clear_service = self.create_client(Empty, '/clear')
        while not clear_service.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Waiting for the clear service...')

        empty_request = Empty.Request()
        clear_future = clear_service.call_async(empty_request)
        rclpy.spin_until_future_complete(self, clear_future)
        self.get_logger().info('Clearing complete.')

    def timer_callback(self):
        if self.count < 6:
            if self.count % 2 ==0:
                msg = Twist()
                msg.angular.z = 2.07774
                self.get_logger().info('Rotating...')
            else:
                msg = Twist()
                msg.linear.x = 4.0
                self.get_logger().info('Moving Forward...')
        elif self.count >= 6 and self.count < 12:
            if self.count % 2 == 1:
                msg = Twist()
                msg.angular.z = math.radians(177.5)
                msg.linear.x = 2 * math.pi - 0.1
                self.get_logger().info('Moving...')
            elif self.count == 6:
                msg=Twist()
                msg.angular.z = math.radians(30)
                self.get_logger().info('Rotating...')
            else:
                msg=Twist()
                msg.angular.z = math.radians(-60)
                self.get_logger().info('Rotating...')
        elif self.count == 12: 
            return
        
        self.count += 1
        self.publisher.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    minimal_publisher = MinimalPublisher()
    try:
        minimal_publisher.teleport_absolute(7.5, 5.0, 0.0)
        minimal_publisher.clear_turtlesim()
        rclpy.spin(minimal_publisher)

    finally:
        minimal_publisher.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()