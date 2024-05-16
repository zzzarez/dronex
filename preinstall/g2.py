import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped
from mavros_msgs.srv import CommandLong, SetMode
from mavros_msgs.msg import State

class DroneEmulator(Node):
    def __init__(self, clock):
        super().__init__('drone_emulator', clock)
        self.state_sub = self.create_subscription(State, '/mavros/state', self.state_callback, 10)
        self.pose_pub = self.create_publisher(PoseStamped, '/mavros/set_position_target_local_ned', 10)
        self.set_mode_client = self.create_client(SetMode, '/mavros/set_mode')
        self.command_long_client = self.create_client(CommandLong, '/mavros/send_command')

    # ...

def main(args=None):
    rclpy.init(args=args)
    clock = rclpy.create_clock()
    drone_emulator = DroneEmulator(clock)
    start_time = drone_emulator.get_clock().now().to_sec()
    drone_emulator.takeoff()
    rclpy.spin_once(drone_emulator, timeout_sec=15)
    drone_emulator.land()
    drone_emulator.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()