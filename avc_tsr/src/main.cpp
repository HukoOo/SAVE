#include <opencv2/highgui.hpp>
#include "ros/ros.h"
#include <std_msgs/Int32.h>
#include "save_msgs/tsr.h"

#include <sstream>

/**
 * This tutorial demonstrates simple sending of messages over the ROS system.
 */
int main(int argc, char **argv)
{

  ros::init(argc, argv, "TSR");

  /**
   * NodeHandle is the main access point to communications with the ROS system.
   * The first NodeHandle constructed will fully initialize this node, and the last
   * NodeHandle destructed will close down the node.
   */
  ros::NodeHandle n;

  ros::Publisher chatter_pub = n.advertise<save_msgs::tsr>("Vision_light", 1000);
  ros::Publisher mission_pub = n.advertise<std_msgs::Int32>("Mission_number", 1000);

  ros::Rate loop_rate(10);


  int count = 0;
  while (ros::ok())
  {
    save_msgs::tsr tsr_result;
    std_msgs::Int32 mission_num;
    mission_num.data = 2;

    tsr_result.recog = true;
    tsr_result.num = 4;


    ROS_INFO("Result=%s, Number=%d", tsr_result.recog? "true" : "false", tsr_result.num);
    ROS_INFO("Mission_number=%d", mission_num);


    chatter_pub.publish(tsr_result);
    mission_pub.publish(mission_num);
    ros::spinOnce();

    loop_rate.sleep();
    ++count;
  }


  return 0;
}
