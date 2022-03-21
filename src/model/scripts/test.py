#! /usr/bin/env python
# -*- coding:utf-8 -*-  

"""
    Python 版 HelloWorld

"""
import rospy
#python 脚本不需要更改cmakelist，也不需要catkin_make即可运行
if __name__ == "__main__":
    rospy.init_node("Hello")
    rospy.loginfo("Hello World!!!!")