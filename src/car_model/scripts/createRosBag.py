import cv2
import time, sys, os
from ros import rosbag
import roslib
import rospy
from geometry_msgs.msg import Twist

def CreateBag():#img,imu, bagname, timestamps
    
    #use rosbag info test.bag to check whether is bag is right
    #rate is used to change the frequency , now is 60 ,means 1/60s per loop
    #use rosbag play test.bag to pub the topic to cmd_vel
    rospy.init_node('bag_data_saver')
    bag = rosbag.Bag("/home/lanpokn/Documents/2022/auto_parking/parking/test.bag", 'w')
    rate = rospy.Rate(60)
    for i in range(0,60):
        cmd_vel = Twist()
        cmd_vel.angular.x = 0
        cmd_vel.angular.y = 0
        cmd_vel.angular.z = 1
        cmd_vel.linear.x = 1
        cmd_vel.linear.y = 0
        cmd_vel.linear.z = 0
        bag.write('/smart/cmd_vel',cmd_vel)
        rate.sleep()
    bag.close()
    # try:
    #     for i in range(len(imudata)):
    #         imu = Imu()
    #         angular_v = Vector3()
    #         linear_a = Vector3()
    #         angular_v.x = float(imudata[i][0])
    #         angular_v.y = float(imudata[i][1])
    #         angular_v.z = float(imudata[i][2])
    #         linear_a.x = float(imudata[i][3])
    #         linear_a.y = float(imudata[i][4])
    #         linear_a.z = float(imudata[i][5])
    #         imuStamp = rospy.rostime.Time.from_sec(float(imutimesteps[i]))
    #         imu.header.stamp=imuStamp
    #         imu.angular_velocity = angular_v
    #         imu.linear_acceleration = linear_a

    #         bag.write("IMU/imu_raw",imu,imuStamp)

    #     for i in range(len(imgs)):
    #         print("Adding %s" % imgs[i])
    #         fp = open(imgs[i], "r")
    #         p = ImageFile.Parser()

    #         '''read image size'''
    #         imgpil = ImagePIL.open(imgs[0])
    #         width, height = imgpil.size
    #         # print "size:",width,height

    #         while 1:
    #             s = fp.read(1024)
    #             if not s:
    #                 break
    #             p.feed(s)

    #         im = p.close()

    #         Stamp = rospy.rostime.Time.from_sec(float(imagetimestamps[i]))

    #         '''set image information '''
    #         Img = Image()

    #         Img.header.stamp = Stamp
    #         Img.height = height
    #         Img.width = width
    #         Img.header.frame_id = "camera"

    #         '''for mono8'''
    #         Img.encoding = "mono8"
    #         Img_data = [pix for pixdata in [im.getdata()] for pix in pixdata]
    #         Img.step = Img.width


    #         Img.data = Img_data
    #         bag.write('camera/image_raw', Img, Stamp)
    # finally:

if __name__ == "__main__":
      print(sys.argv)
      CreateBag()