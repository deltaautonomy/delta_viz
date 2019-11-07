#!/usr/bin/env python

import rospy
from diagnostic_msgs.msg import DiagnosticArray, DiagnosticStatus


def make_diagnostics_status(name, pipeline, fps, level=DiagnosticStatus.OK):
    msg = DiagnosticStatus()
    msg.level = DiagnosticStatus.OK
    msg.name = name
    msg.message = fps
    msg.hardware_id = pipeline
    return msg


def publish_diagnostics(pub):
    msg = DiagnosticArray()
    msg.header.stamp = rospy.Time.now()
    msg.status.append(make_diagnostics_status('object_detection', 'perception', '12'))
    msg.status.append(make_diagnostics_status('bounding_box_tracking', 'perception', '422.11'))
    pub.publish(msg)


def talker():
    topic = '/delta/perception/object_detection/diagnostics'
    pub = rospy.Publisher(topic, DiagnosticArray, queue_size=10)

    rospy.init_node('diagnostics_test_publisher', anonymous=True)
    rate = rospy.Rate(0.4)

    while not rospy.is_shutdown():
        publish_diagnostics(pub)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
