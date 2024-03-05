import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import numpy as np
from scipy import signal
from signal_msg.msg import SignalDecomposed

class Signal_Reconstructor(Node):
    def __init__(self):
        super().__init__('signal_reconstruction_node')

        self.current_signal = 0
        self.a = 0
        self.f = 0
        self.offset = 0
        self.phase = 0
        self.t = 0
        self.signal_timer_period = 1e-2

        self.signal_msg = Float32()

        self.signal_pub = self.create_publisher(Float32, 'signal_reconstructed/wave', 10)
        self.signal_params_sub = self.create_subscription(SignalDecomposed, 'signal/params', self.signal_params_callback, 10)

        self.signal_timer = self.create_timer(self.signal_timer_period, self.signal_timer_callback)

    def signal_timer_callback(self):
        omega = 2 * np.pi * self.f
        if self.current_signal == 0:
            wave = self.a * np.sin(omega * self.t + self.phase) + self.offset
        elif self.current_signal == 1:
            wave = self.a * signal.square(omega * self.t + self.phase) + self.offset
        elif self.current_signal == 2:
            wave = self.a * signal.sawtooth(omega * self.t + self.phase) + self.offset
        
        self.signal_msg.data = wave
        self.signal_pub.publish(self.signal_msg)
    
    def signal_params_callback(self, msg):
        self.current_signal = msg.signaltype
        self.a = msg.amplitude
        self.f = msg.frequency
        self.offset = msg.offset
        self.phase = msg.phase
        self.t = msg.time

def main(args=None):
    rclpy.init(args=args)
    node = Signal_Reconstructor()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
