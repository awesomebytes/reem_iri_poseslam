#!/usr/bin/env python
"""
Created on 26/04/14

@author: Sammy Pfeiffer
"""
import rospy

from nav_msgs.msg import Odometry
from geometry_msgs.msg import Quaternion

ODOM_TOPIC = '/mobile_base_controller/odom'
REL_ODOM_TOPIC = '/odom_rel'


class odom_rel():
    def __init__(self):
        self.subs = rospy.Subscriber(ODOM_TOPIC, Odometry, self.odom_cb)
        self.pub = rospy.Publisher(REL_ODOM_TOPIC, Odometry)
        self.last_odom_msg = None

    def odom_cb(self, data):
        if self.last_odom_msg:
            odom_msg = Odometry()
            odom_msg.pose.covariance = data.pose.covariance
            # TODO: learn how to do a one liner of this
            odom_msg.pose.pose.position.x = data.pose.pose.position.x - self.last_odom_msg.pose.pose.position.x
            odom_msg.pose.pose.position.x = data.pose.pose.position.y - self.last_odom_msg.pose.pose.position.y
            odom_msg.pose.pose.position.x = data.pose.pose.position.z - self.last_odom_msg.pose.pose.position.z

            odom_msg.pose.pose.orientation = Quaternion(w=1.0)

            odom_msg.twist.twist.linear.x = data.twist.twist.linear.x - self.last_odom_msg.twist.twist.linear.x
            odom_msg.twist.twist.linear.y = data.twist.twist.linear.y - self.last_odom_msg.twist.twist.linear.y
            odom_msg.twist.twist.linear.z = data.twist.twist.linear.z - self.last_odom_msg.twist.twist.linear.z

            odom_msg.twist.twist.angular.x = data.twist.twist.angular.x - self.last_odom_msg.twist.twist.angular.x
            odom_msg.twist.twist.angular.y = data.twist.twist.angular.y - self.last_odom_msg.twist.twist.angular.y
            odom_msg.twist.twist.angular.z = data.twist.twist.angular.z - self.last_odom_msg.twist.twist.angular.z

            odom_msg.twist.covariance = data.twist.covariance
            self.pub.publish(odom_msg)

        self.last_odom_msg = data


if __name__ == '__main__':
    rospy.init_node('odom_rel_from_odom')
    o = odom_rel()
    rospy.spin()
