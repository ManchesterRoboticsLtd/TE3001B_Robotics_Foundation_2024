import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import numpy as np
from scipy import signal
from signal_msg.msg import SignalDecomposed

class Signal_Generator(Node):
    def __init__(self):
        super().__init__('signal_generator_node')

        self.time = 0
        self.signal_timer_period = 1e-3
        self.decomposed_timer_period = 1e-2
        self.current_signal = 0

        self.declare_parameters(
            namespace='',
            parameters=[
                ('signal_type', rclpy.Parameter.Type.INTEGER),
                ('default.amplitude', rclpy.Parameter.Type.DOUBLE ),
                ('default.frequency', rclpy.Parameter.Type.DOUBLE ),
                ('default.offset', rclpy.Parameter.Type.DOUBLE ),
                ('default.phase', rclpy.Parameter.Type.DOUBLE ),
                ('default.time', rclpy.Parameter.Type.DOUBLE ),
                ('square.amplitude', rclpy.Parameter.Type.DOUBLE ),
                ('square.frequency', rclpy.Parameter.Type.DOUBLE ),
                ('square.offset', rclpy.Parameter.Type.DOUBLE ),
                ('square.phase', rclpy.Parameter.Type.DOUBLE ),
                ('square.time', rclpy.Parameter.Type.DOUBLE ),
                ('sawtooth.amplitude', rclpy.Parameter.Type.DOUBLE ),
                ('sawtooth.frequency', rclpy.Parameter.Type.DOUBLE ),
                ('sawtooth.offset', rclpy.Parameter.Type.DOUBLE ),
                ('sawtooth.phase', rclpy.Parameter.Type.DOUBLE ),
                ('sawtooth.time', rclpy.Parameter.Type.DOUBLE ),
            ]
        )

        self.signal = 0
        self.t = 0
        self.signal_msg = Float32()
        self.signal_dec_msg = SignalDecomposed()

        self.signal_pub = self.create_publisher(Float32, 'signal/wave', 10)
        self.signal_params_pub = self.create_publisher(SignalDecomposed, 'signal/params', 10)

        self.signal_timer = self.create_timer(self.signal_timer_period, self.signal_timer_callback)
        self.signal_timer = self.create_timer(self.decomposed_timer_period, self.pub_timer_callback)

    def signal_timer_callback(self):
        self.t += self.signal_timer_period
        self.current_signal = self.get_parameter('signal_type').get_parameter_value().integer_value
        if self.current_signal == 0:
            #self.get_logger().info('default')
            self.f = self.get_parameter('default.frequency').get_parameter_value().double_value
            self.a = self.get_parameter('default.amplitude').get_parameter_value().double_value
            self.offset = self.get_parameter('default.offset').get_parameter_value().double_value
            self.phase = self.get_parameter('default.offset').get_parameter_value().double_value
            omega = 2 * np.pi * self.f
            wave = self.a * np.sin(omega * self.t + self.phase) + self.offset
        elif self.current_signal == 1:
            #self.get_logger().info('square')
            self.f = self.get_parameter('square.frequency').get_parameter_value().double_value
            self.a = self.get_parameter('square.amplitude').get_parameter_value().double_value
            self.offset = self.get_parameter('square.offset').get_parameter_value().double_value
            self.phase = self.get_parameter('default.offset').get_parameter_value().double_value
            omega = 2 * np.pi * self.f
            wave = self.a * signal.square(omega * self.t + self.phase) + self.offset
        elif self.current_signal == 2:
            #self.get_logger().info('square')
            self.f = self.get_parameter('sawtooth.frequency').get_parameter_value().double_value
            self.a = self.get_parameter('sawtooth.amplitude').get_parameter_value().double_value
            self.offset = self.get_parameter('sawtooth.offset').get_parameter_value().double_value
            self.phase = self.get_parameter('default.offset').get_parameter_value().double_value
            omega = 2 * np.pi * self.f
            wave = self.a * signal.sawtooth(omega * self.t + self.phase) + self.offset
        
        self.signal_msg.data = wave
        self.signal_pub.publish(self.signal_msg)

    def pub_timer_callback(self):
        self.signal_dec_msg.signaltype = self.current_signal
        self.signal_dec_msg.amplitude = self.a
        self.signal_dec_msg.frequency = self.f
        self.signal_dec_msg.offset = self.offset
        self.signal_dec_msg.phase = self.phase
        self.signal_dec_msg.time = self.t
        self.signal_params_pub.publish(self.signal_dec_msg)

def main(args=None):
    rclpy.init(args=args)
    node = Signal_Generator()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
