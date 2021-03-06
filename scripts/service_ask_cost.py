#!/usr/bin/env python

try:
    import selectors
except ImportError:
    import selectors2 as selectors
import rospy
import socket
import types
import json
import time as ti

from ros_wifi.msg import CtrlData
from std_msgs.msg import Header
from ros_wifi.srv import WifiNodeCost,WifiNodeCostResponse

import random
COST = random.uniform(1,15)

def ad(req):
    global COST
    rospy.loginfo('ask cost recv ')
    #rospy.loginfo(req)
    send_b = WifiNodeCostResponse()
    send_b.error_code = 'O'
    send_b.cost = COST
    COST = COST + 1
    return send_b

def main():
    rospy.init_node('service_ask_cost', anonymous = True)
    rospy.Service('robot_wifi_nodecost_inner', WifiNodeCost, ad)
    rospy.spin()

if __name__ == '__main__':
    main()

