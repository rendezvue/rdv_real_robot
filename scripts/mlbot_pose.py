#!/usr/bin/env python
from re import X
import rospy 
import rospkg 
from gazebo_msgs.msg import ModelState 
from gazebo_msgs.srv import SetModelState
from nav_msgs.msg import Odometry

def set_mlbot_pose(x,y,z, ori_x, ori_y, ori_z, ori_w ):
    state_msg = ModelState()
    state_msg.model_name = 'mlbot_sim'
    state_msg.pose.position.x = x
    state_msg.pose.position.y = y 
    state_msg.pose.position.z = z 
    state_msg.pose.orientation.x = ori_x
    state_msg.pose.orientation.y = ori_y
    state_msg.pose.orientation.z = ori_z
    state_msg.pose.orientation.w = ori_w

    rospy.wait_for_service('/gazebo/set_model_state')
    try:
        set_state = rospy.ServiceProxy('/gazebo/set_model_state', SetModelState)
        resp = set_state( state_msg )

    except rospy.ServiceException, e:
        print "Service call failed: %s" % e

def odometryCb(msg):
#    print msg.pose.pose
    pose = msg.pose.pose.position
    ori = msg.pose.pose.orientation

    set_mlbot_pose(pose.x, pose.y, pose.z, ori.x, ori.y, ori.z ,ori.w )

def test():
    set_mlbot_pose(-1.462, 7.51, 0.005, 0, 0, 0, 1 )

if __name__ == '__main__':
    try:
        rospy.init_node('set_pose')
        rospy.Subscriber('/rdvremote/hdl_odom',Odometry,odometryCb)
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
