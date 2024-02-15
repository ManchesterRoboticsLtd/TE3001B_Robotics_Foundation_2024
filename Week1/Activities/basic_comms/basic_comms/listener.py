import rclpy
from rclpy.node import Node
from std_msgs.msg import String, Int32

class ExampleSubscriber(Node):
    def __init__(self):
        super().__init__('listener_node')
        self.sub = self.create_subscription(String, 'chit_chat', self.listener_callback, 10)
        self.get_logger().info('Listener node initialized')

    def listener_callback(self, msg):
        self.get_logger().info('Message: {}'.format(msg.data))

def main(args=None):
    rclpy.init(args=args)
    e_s = ExampleSubscriber()
    rclpy.spin(e_s)
    e_s.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()