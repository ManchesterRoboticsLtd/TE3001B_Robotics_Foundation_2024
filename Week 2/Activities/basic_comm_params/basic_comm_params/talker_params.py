import rclpy
from rclpy.node import Node
from std_msgs.msg import String, Int32

class ExamplePublisher(Node):
    def __init__(self):
        super().__init__('talker_node_param')
        self.pubisher = self.create_publisher(String, 'chit_chat', 10)
        self.declare_parameter('my_param', 'gente')
        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.get_logger().info('Talker node initialized')
        self.msg = String()
    
    def timer_callback(self):
        my_param = self.get_parameter('my_param').get_parameter_value().string_value
        self.msg.data = "Holaaaaaa {}".format(my_param)
        self.pubisher.publish(self.msg)

def main(args=None):
    rclpy.init(args=args)
    e_p = ExamplePublisher()
    rclpy.spin(e_p)
    e_p.destroy_node()
    rclpy.shutdown()
    
if __name__ == '__main__':
    main()
