#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Heethesh Vhavle
# @Date:   Nov 18, 2019
# @Last Modified by:   Heethesh Vhavle
# @Last Modified time: Nov 18, 2019

import rospy
from delta_msgs.msg import CollisionDetection


def make_collision_msg(track_id, ttc, probability):
    msg = CollisionDetection()
    msg.header.stamp = rospy.Time.now()
    msg.header.frame_id = 'ego_vehicle'
    msg.time_to_impact = rospy.Duration(ttc)
    msg.probability = probability
    msg.track_id = track_id
    return msg


def main():
    rospy.init_node('test_collision_detection', anonymous=True)

    pub = rospy.Publisher('/delta/prediction/collision', CollisionDetection, queue_size=5)
    r = rospy.Rate(10)

    try:
        while not rospy.is_shutdown():
            pub.publish(make_collision_msg(1, 2.4, 1.0))
            r.sleep()
    except rospy.ROSInterruptException:
        rospy.loginfo('Shutting down')


if __name__ == "__main__":
    main()
