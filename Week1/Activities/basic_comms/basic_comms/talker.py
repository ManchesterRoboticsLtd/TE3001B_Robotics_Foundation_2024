import rclpy
from rclpy.node import Node
from std_msgs.msg import String, Int32

class ExamplePublisher(Node):
    def __init__(self):
        super().__init__('talker_node')
        self.pubisher = self.create_publisher(String, 'chit_chat', 10)
        self.pubisher_counter = self.create_publisher(Int32, 'counter', 10)
        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self.timer_callback)

        timer_period = 0.1
        self.timer_2 = self.create_timer(timer_period, self.timer_callback_counter)
        self.get_logger().info('Talker node initialized')
        self.msg = String()
        self.msg_counter = Int32()
        self.i = 0
    
    def timer_callback_counter(self):
        self.msg_counter.data = self.i
        self.pubisher_counter.publish(self.msg_counter)
        self.i += 2

    def timer_callback(self):
        self.msg.data = "Holaaaaaa :)"
        self.pubisher.publish(self.msg)

def main(args=None):
    rclpy.init(args=args)
    e_p = ExamplePublisher()
    rclpy.spin(e_p)
    e_p.destroy_node()
    rclpy.shutdown()
    
if __name__ == '__main__':
    main()
