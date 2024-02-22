import rclpy
from rclpy.node import Node

class YamlParams(Node):
    def __init__(self):
        super().__init__('example_node_params')
        self.declare_parameters(
            namespace='',
            parameters=[
                ('bool_value', rclpy.Parameter.Type.BOOL),
                ('float_number', rclpy.Parameter.Type.DOUBLE),
                ('float_array', rclpy.Parameter.Type.DOUBLE_ARRAY),
            ]
        )

def main(args=None):
    rclpy.init(args=args)
    y_p = YamlParams()
    rclpy.spin(y_p)
    y_p.destroy_node()
    rclpy.shutdown()
    
if __name__ == '__main__':
    main()