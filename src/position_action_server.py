#! /usr/bin/env python

from std_msgs.msg import String
from std_msgs.msg import Float64
#from urx.robotiq_two_finger_gripper import Robotiq_Two_Finger_Gripper

import rospy

import urx 

import sys

import actionlib

import actionlib_movement.msg

import socket

HOST = "172.22.22.2" # The remote host (arm IP address)
PORT = 30002 # The same port as used by the server



class MovementAction(object):
	_result = actionlib_movement.msg.MovementResult()



	def __init__(self, name):
		self._action_name = name
		self._as = actionlib.SimpleActionServer(self._action_name, 
		actionlib_movement.msg.MovementAction, execute_cb=self.execute_cb,
		auto_start = False)

		self._as.start()
		


	def execute_cb(self, goal):
		r = rospy.Rate(1)
		success = True

		#COMMENTED OUT FOR NOW when robot isn't present 
		#rob = urx.Robot("172.22.22.2")
		#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		#s.connect((HOST, PORT))

		rospy.loginfo("Sending robot pose!!")


		rospy.loginfo('%s: Executing, returning value of %s' %(self._action_name,
		goal.request))

		if self._as.is_preempt_requested():
                	rospy.loginfo('%s: Preempted' % self._action_name)
                	self._as.set_preempted()
                	success = False
	

		if success:

			
			rospy.loginfo('Print request of %s'%(goal.request))

			#commands to move the robot to the position here

			
			#code for when the request was an array of floats
			#cList = []
			#for x in goal.coordinates:
				#pos = Float64()
				#pos.data = goal.coordinates[0]
				#cList.append(pos)

			#rob.movel((cList[0], cList[1], cList[2], cList[3], cList[4], cList[5]), 0.05, 0.1, relative=True)
			#time.sleep(5)
			#data = s.recv(1024)
			
			a = 0.05
			v = 0.1

			#COMMENTED OUT FOR NOW 
			#pose = rob.getl()
			#rospy.loginfo("Current pose: %s"% (rob.getl()))
			#rob.movep(pose, acc=a, vel=v, wait=True)


			forwardString = String()
			forwardString.data = "forward"

			backwardString = String()
			backwardString.data = "backward"

			leftString = String()
			leftString.data = "left"

			rightString = String()
			rightString.data = "right"

			upString = String()
			upString.data = "up"

			downString = String()
			downString.data = "down"



			
			#COMMENTED OUT FOR NOW - all robot commands within 

			#moving forward and backward - adjust x coordinate 
			if (goal.request == forwardString):
				#move the arm to a certain pose
				#rob.movel((pose[0], pose[1], pose[2] + 0.1, pose[3], pose[4], pose[5]), a, v, relative=True)
				rospy.loginfo("forward")

			elif (goal.request == backwardString):
				#move the arm to a certain pose
				#rob.movel((pose[0], pose[1], pose[2] - 0.1, pose[3], pose[4], pose[5]), a, v, relative=True)
				rospy.loginfo("backward")


			#moving left and right - adjust x coordinate 
			elif (goal.request == leftString):
				#move the arm to a certain pose
				#rob.movel((pose[0]- 0.1, pose[1], pose[2], pose[3], pose[4], pose[5]), a, v, relative=True)
				rospy.loginfo("left")

			elif (goal.request == rightString):
				#move the arm to a certain pose
				#rob.movel((pose[0] + 0.1, pose[1], pose[2], pose[3], pose[4], pose[5]), a, v, relative=True)
				rospy.loginfo("right")


			#moving up and down - adjust y coordinate
			elif (goal.request == upString):
				#move the arm to a certain pose
				#rob.movel((pose[0], pose[1] + 0.1, pose[2], pose[3], pose[4], pose[5]), a, v, relative=True)
				rospy.loginfo("up")

			elif (goal.request == downString):
				#move the arm to a certain pose
				#rob.movel((pose[0], pose[1] - 0.1, pose[2], pose[3], pose[4], pose[5]), a, v, relative=True)
				rospy.loginfo("down")


			#COMMENTED OUT FOR NOW 
			#rob.close()
			#sys.exit() 	

		self._result.success = success
		rospy.loginfo('%s: Succeeded' % self._action_name)
	        self._as.set_succeeded(self._result)
		


if __name__ == '__main__':
	rospy.init_node('Position')
	server = MovementAction(rospy.get_name())

	rospy.spin()

	#while not rospy.is_shutdown():
    		#continue

