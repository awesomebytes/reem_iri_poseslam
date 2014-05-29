#!/usr/bin/env python
"""
Created on 29/04/14

@author: Sammy Pfeiffer
"""
import rospy

import copy
from sensor_msgs.msg import LaserScan

LASER_TOPIC = '/scan_filtered'
INVERTED_LASER_TOPIC = '/inverted_scan_filtered'


class invert_laser():
    def __init__(self):
        self.subs = rospy.Subscriber(LASER_TOPIC, LaserScan, self.laser_cb)
        self.pub = rospy.Publisher(INVERTED_LASER_TOPIC, LaserScan)

    def laser_cb(self, data):
        laser_msg_inverted = copy.deepcopy(data)
        laser_msg_inverted.angle_min, laser_msg_inverted.angle_max = laser_msg_inverted.angle_max, laser_msg_inverted.angle_min
        self.pub.publish(laser_msg_inverted)


if __name__ == '__main__':
    rospy.init_node('laser_inverter_of_truth')
    i = invert_laser()
    rospy.spin()
