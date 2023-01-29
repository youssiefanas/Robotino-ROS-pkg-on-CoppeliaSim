import rospy
from geometry_msgs.msg import Twist, Pose2D
import numpy as np
PI=np.pi
kp=1.5
ka=0.02
k_beta=0
def node_init():
    rospy.init_node('robotino',anonymous=True)
    rospy.Subscriber('/robotino/pose',Pose2D,pose_recieved_callback)
    rospy.Subscriber('/robotino/goal', Pose2D, goal_recieved_callback)
    global vel_pub
    vel_pub=rospy.Publisher('/turtle/cmd_vel', Twist,queue_size=10)
    rospy.spin()

def pose_recieved_callback(robotino_pose):
    global x_robotino, y_robotino, theta_robotino
    x_robotino=robotino_pose.x
    y_robotino=robotino_pose.y
    theta_robotino=robotino_pose.theta
    rospy.loginfo("I heard({:2f},{:2f},{:2f})".format(x_robotino,y_robotino,theta_robotino))


def goal_recieved_callback(robotino_goal):
    x_goal=robotino_goal.x
    y_goal=robotino_goal.y
    theta_goal=robotino_goal.theta
    dist_err=np.sqrt(np.power(x_goal-x_robotino,2)+np.power(y_goal-y_robotino,2))
    robotino_speed=Twist()
    while not abs(dist_err) <0.1:
        x_dist_err=x_goal-x_robotino
        y_dist_err=y_goal-y_robotino
        #dist_err=np.sqrt(np.power(x_goal-x_robotino,2)+np.power(y_goal-y_robotino,2))
        ang_err=np.arctan2((y_goal-y_robotino),(x_goal-x_robotino))
        ang_err=np.mod(ang_err+PI,2*PI)-PI
        robotino_speed.linear.x=x_dist_err*kp
        robotino_speed.linear.y=y_dist_err*kp
        robotino_speed.angular.z=ang_err*ka
        vel_pub.publish(robotino_speed)
        rospy.sleep(0.01)
    print("Reach position")   
    beta = theta_robotino - theta_goal
    while not np.abs(beta)<0.1:
        beta = theta_robotino - theta_goal
        robotino_speed.linear.x = 0
        robotino_speed.linear.y = 0
        robotino_speed.angular.z = (k_beta * beta)
        vel_pub.publish(robotino_speed)
        rospy.sleep(0.01)
    print("Reach orientation")   
    robotino_speed.linear.x = 0
    robotino_speed.linear.y = 0
    robotino_speed.angular.z = 0
    vel_pub.publish(robotino_speed)
    rospy.sleep(0.5)    


if __name__=='__main__':
    node_init()
