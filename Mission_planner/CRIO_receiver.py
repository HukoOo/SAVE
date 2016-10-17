#!/usr/bin/env python

import rospy
import socket
import std_msgs.msg
from std_msgs.msg import Float64
import tf
import math

def CRIO_receiver():
    pub_enc=rospy.Publisher('Lidar_encorder', Float64, queue_size=10)
    pub_str = rospy.Publisher('Can_steering', Float64, queue_size=10)
    pub_ap = rospy.Publisher('Can_ap', Float64, queue_size=10)
    pub_bp = rospy.Publisher('Can_bp', Float64, queue_size=10)
    pub_gear = rospy.Publisher('Can_gear', Float64, queue_size=10)
    pub_acc = rospy.Publisher('Can_accel_speed', Float64, queue_size=10)
    pub_speed = rospy.Publisher('Can_speed', Float64, queue_size=10)
    pub_yaw = rospy.Publisher('Can_yawrate', Float64, queue_size=10)
   # pub = rospy.Publisher('velocity', Float64, queue_size=10)

    UDP_IP = "115.145.177.10"                         # Jetson IP address
   #UDP_IP = "localhost"                              # Do not need in a listener case
    UDP_PORT = 8081	                              # Lidar, Unity port

    sock = socket.socket(socket.AF_INET,              # Internet
                         socket.SOCK_DGRAM)           # UDP
    sock.bind((UDP_IP, UDP_PORT))

    array = std_msgs.msg.Int16MultiArray
 
    br = tf.TransformBroadcaster()                    # assign tf broadcaster to br
    rospy.init_node('unity_listener', anonymous=True)
    rate = rospy.Rate(200)                             # 50hz loop Hz

    while not rospy.is_shutdown():
        data = sock.recv(1024)                        # buffer size is 1024 bytes
        data_list = [ord(s) for s in data]            # make list 
        # to UD(encoder data)
        encoder_udp = float (data_list[2]*256+data_list[3])/100  # rebuild necessary data(ex. LiDAR encoder ..)
        br.sendTransform((0, 0, 0), (tf.transformations.quaternion_from_euler(0, 0, 0*(math.pi/180))),
                          rospy.Time.now(), "base_car", "world")
                                                      # translation, rotation, time, child, parent 
        br.sendTransform((0, 0, 1.8),                     
                          (tf.transformations.quaternion_from_euler(180*(math.pi/180), 0, 
                           -(encoder_udp)*(math.pi/180))),
                             rospy.Time.now(), "base_encoder", "base_car")          
                                                      # translation, rotation, time, child, parent 
        br.sendTransform((-0.2, 0, 0),                     
                          (tf.transformations.quaternion_from_euler(90*(math.pi/180), 0, 0)),
                           rospy.Time.now(), "base_lidar1", "base_encoder")          
                                                      # translation, rotation, time, child, parent
        br.sendTransform((0, -0.2, 0),                     
                          (tf.transformations.quaternion_from_euler(90*(math.pi/180), 0, 90*(math.pi/180))),
                           rospy.Time.now(), "base_lidar2", "base_encoder")          
                                                      # translation, rotation, time, child, parent
        br.sendTransform((0.2, 0, 0),                     
                          (tf.transformations.quaternion_from_euler(90*(math.pi/180), 0, 180*(math.pi/180))),
                           rospy.Time.now(), "base_lidar3", "base_encoder")          
                                                      # translation, rotation, time, child, parent
        br.sendTransform((0, 0.2, 0),                     
                          (tf.transformations.quaternion_from_euler(90*(math.pi/180), 0, 270*(math.pi/180))),
                           rospy.Time.now(), "base_lidar4", "base_encoder")          
                                                      # translation, rotation, time, child, parent
	#print "encoder data:" , encoder_udp, "/raw data:", data_list[0], data_list[1]
        # CAN data
	Can_steering = float (float(data_list[4])-1)*(data_list[5]*256+data_list[6])/100
	Can_ap=float (data_list[7]*256+data_list[8])/100
	Can_bp=float (data_list[9]*256+data_list[10])/100
	Can_acc = float (float(data_list[11])-1)*(data_list[12]*256+data_list[13])/100
	Can_gear=float (data_list[14]*256+data_list[15])/100 # ?????
	Can_speed = float (data_list[16]*256+data_list[17])/100
	Can_yawrate = float (float(data_list[18])-1)*(data_list[19]*256+data_list[20])/100

        rate.sleep() 
	pub_enc.publish(encoder_udp)
	pub_str.publish(Can_steering)
	pub_ap.publish(Can_ap)
	pub_bp.publish(Can_bp)
	pub_gear.publish(Can_gear)
	pub_acc.publish(Can_acc)
	pub_speed.publish(Can_speed)
	pub_yaw.publish(Can_yawrate)

if __name__ == '__main__':
    try:
        CRIO_receiver()
    except rospy.ROSInterruptException:
        pass
