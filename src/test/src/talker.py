#!/usr/bin/env python
import rospy
from std_msgs.msg import String


def talker():
    pub = rospy.Publisher('qmsg', String, queue_size=10)
    rospy.init_node('Qtalker')
    rate = rospy.Rate(1)
    
    while not rospy.is_shutdown():
        msg = f'hello from {rospy.get_caller_id()}, time is {rospy.get_time()}'
        pub.publish(msg)
        rospy.loginfo(msg)
        rate.sleep()


if __name__ == '__main__':
    talker()
