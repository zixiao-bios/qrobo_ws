#!/usr/bin/env python
import rospy
from std_msgs.msg import String


def callback(data):
    rospy.loginfo(f'{rospy.get_caller_id()} get msg: {data}')


def listener():
    rospy.init_node('Qlistener')
    rospy.Subscriber('qmsg', String, callback)
    rospy.spin()


if __name__ == '__main__':
    listener()
