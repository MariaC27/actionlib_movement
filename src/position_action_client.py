#! /usr/bin/env python

from __future__ import print_function
from std_msgs.msg import String
from std_msgs.msg import Float64
import rospy

import actionlib
import actionlib_movement.msg



def position_client():
	client = actionlib.SimpleActionClient('Position', actionlib_movement.msg.MovementAction)
	
	client.wait_for_server()

	retStr = String()
	retStr.data = "forward"
	#options: forward, backward, left, right, up, down


	goal = actionlib_movement.msg.MovementGoal(request = retStr)
	

	client.send_goal(goal)

	client.wait_for_result()

	return client.get_result()



if __name__ == '__main__':
	try:
		#initializes a node so the client can publish and subscribe using ROS
		rospy.init_node('position_client_py')
		result = position_client()
	except rospy.ROSInterruptException:
        	print("program interrupted before completion", file=sys.stderr)

