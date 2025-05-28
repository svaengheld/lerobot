from lerobot.common.robot_devices.robots.utils import make_robot_from_config
from lerobot.common.robot_devices.robots.configs import So101RobotConfig

robot = make_robot_from_config(So101RobotConfig())
robot.connect()

for arm in robot.follower_arms.values():
    arm.write("P_Coefficient", 24)          # try 24 or higher
    print("Current P:", arm.read("P_Coefficient"))

robot.disconnect()