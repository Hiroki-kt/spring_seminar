#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Point
from std_msgs.msg import Int32

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "%s,%s,%s",data.x, data.y,data.z)

def pos_subscriber():
    rospy.init_node('test_sub', anonymous=True)
    rospy.Subscriber("sample_position", Point, callback)
    #rospy.Subscriber("position", Pos, callback)

    rospy.spin()

def state_subscriber():
    rospy.init_node('test_sub', anonymous=True)
    rospy.Subscriber("state", Int32, callback)

    rospy.spin()

if __name__ == "__main__":
    rospy.init_node('Test_Sub', anonymous=True)

    rospy.Subscriber("state", Int32, callback)
