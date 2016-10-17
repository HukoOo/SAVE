#-*-coding: utf-8 -*-
#!/usr/bin/env python

import sys
import rospy
from save_msgs.msg import tsr
from std_msgs.msg import Int32
from std_msgs.msg import Float64
from sensor_msgs.msg import LaserScan




class TopicData(object):
    def __init__(self,topicName, topicType, topicData):
        self.data = topicData
        self.type =topicType
        self.name =topicName


        rospy.init_node("Planner", anonymous=True)
        self.listener()

    def updateData(self, index, data):
        self.data[index] = data

    def buildCallback(self, topic_index):
        def callback(data):
            value = data
            #print data
            self.updateData(topic_index, value)
        return callback


    def listener(self):

        for i, j in enumerate(self.data):
            rospy.Subscriber(self.name[i], self.type[i], self.buildCallback(i))


    def talker(self):

        pub = rospy.Publisher('Stop_distance',Float64, queue_size=10)
        rate = rospy.Rate(10) # 10hz

        #pub.publish(distance)