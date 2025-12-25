import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class TurtlePublisher(Node):
    def __init__(self):
        super().__init__('turtle_publisher_node')
        # /turtle1/cmd_vel konusuna Twist tipinde mesaj gönderen bir publisher oluşturuyoruz
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        # 0.5 saniyede bir mesaj göndermesi için timer kuruyoruz
        self.timer = self.create_timer(0.5, self.timer_callback)

    def timer_callback(self):
        msg = Twist()
        msg.linear.x = 2.0  # İleri gitme hızı
        msg.angular.z = 1.0 # Dönme hızı (daire çizmesi için)
        self.publisher_.publish(msg)
        self.get_logger().info('Hız verisi gönderildi: "%s"' % msg.linear.x)

def main(args=None):
    rclpy.init(args=args)
    turtle_publisher = TurtlePublisher()
    rclpy.spin(turtle_publisher)
    turtle_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
