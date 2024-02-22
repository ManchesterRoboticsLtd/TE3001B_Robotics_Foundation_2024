import rclpy
from rclpy.node import Node
import numpy as np
from msg_srv_int.msg import Sphere

class SphereCustomMessages(Node):
    def __init__(self):
        super().__init__('Sphere_node')

        self.msg = Sphere()

        self.pub = self.create_publisher(Sphere, 'sphere', 10)
        self.timer_period = 0.1
        self.time = 0
        self.timer = self.create_timer(self.timer_period, self.radius_timer_callback)
        self.r = 2.0
        self.get_logger().info('Custom sphere messages initialized')

    def radius_timer_callback(self):
        self.r = 2.0 + np.sin(self.time)
        self.time += self.timer_period
        self.msg.radius = self.r
        self.msg.center.x = 10*np.cos(self.time)
        self.pub.publish(self.msg)

def main(args=None):
    rclpy.init(args=args)
    s_c_m = SphereCustomMessages()
    rclpy.spin(s_c_m)
    s_c_m.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
