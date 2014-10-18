#!/usr/bin/env python
#!/usr/bin/env python
import rospy
import numpy as np
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from turtlesim.srv import TeleportAbsolute

pub = rospy.Publisher('/turtle1/cmd_vel',Twist, queue_size=10)
rospy.init_node('master_splinter', anonymous=True)
s = rospy.ServiceProxy('/turtle1/teleport_absolute',TeleportAbsolute)
s = (20,15,0)


def leonardo():
	T = input('Please note that the magic number is 5. Enter a value for T: ')
	p = Twist()
	t_base = rospy.Time.now()
	while not rospy.is_shutdown():
		rospy.sleep(0.01)
		t = (rospy.Time.now() - t_base).to_sec()
		print 'time', t
		V = 6. * np.pi * np.sqrt((np.cos((2.* np.pi * t)/T)**2 + 4.* np.cos((4.* np.pi * t)/T)**2) / T**2) 
		w = 4.* np.pi * (3.*np.sin((2.*np.pi * t)/T) + np.sin((6.* np.pi*t)/T))/(T*(5 + np.cos((4.*np.pi*t)/T) + 4*np.cos((8.*np.pi*t)/T)))
		p.linear.x = V
		p.angular.z = w 	#since our robot is in a 2-D plane it rotates about its z axis
		pub.publish(p)


def main():
	leonardo()

if __name__ == '__main__':
	main()