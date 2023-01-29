function Message_callback(vel)
        x_vel = vel.linear.x
       y_vel = vel.linear.y
       t_vel = vel.angular.z
      
        V1= (x_vel+0.3*t_vel)/0.1
        V2=(-0.5*x_vel+0.866*y_vel+0.3*t_vel)/0.1
        V3=(-0.5*x_vel-0.866*y_vel+0.3*t_vel)/0.1
        if (V1>1) or (V2>1 ) or (V3>1) then
        V1=V1/3
       V2=V2/3
       V3=V3/3
       end
        sim.setJointTargetVelocity(Motor1,V1)
        sim.setJointTargetVelocity(Motor2,V2)
        sim.setJointTargetVelocity(Motor3,V3)
    end
    
function tele_callback(msg)
        x_vel = msg.linear.x
       y_vel = msg.linear.y
       t_vel = msg.angular.z
      
        V1= (x_vel+0.3*t_vel)/0.1
        V2=(-0.5*x_vel+0.866*y_vel+0.3*t_vel)/0.1
        V3=(-0.5*x_vel-0.866*y_vel+0.3*t_vel)/0.1
        if (V1>1 ) or(V2>1) or (V3>1 )then
        V1=V1/3
       V2=V2/3
       V3=V3/3
       end
        sim.setJointTargetVelocity(Motor1,V1)
        sim.setJointTargetVelocity(Motor2,V2)
        sim.setJointTargetVelocity(Motor3,V3)
    end

function sysCall_init()
    -- do some initialization here
    robot = sim.getObjectHandle('/omniRob')
    Motor1 = sim.getObjectHandle('/omniRob/OmniWheel[0]')
    Motor2 = sim.getObjectHandle('/omniRob/OmniWheel[1]')
    Motor3 = sim.getObjectHandle('/omniRob/OmniWheel[2]')
    if simROS then
        sim.addLog(sim.verbosity_scriptinfos,"ROS interface was found.")
        pub=simROS.advertise('/robotino/pose', 'geometry_msgs/Pose2D')
        sub=simROS.subscribe('/turtle/cmd_vel', 'geometry_msgs/Twist', 'Message_callback')
        sub=simROS.subscribe('/turtle1/cmd_vel', 'geometry_msgs/Twist', 'tele_callback')

    else
        sim.addLog(sim.verbosity_scripterrors,"ROS interface was not found. Cannot run.")
    end
end

function sysCall_actuation()
    -- put your actuation code here
    pos = sim.getObjectPosition(robot,-1)
	eulerAngles=sim.getObjectOrientation(robot, -1)
	alpha, beta, gamma= sim.yawPitchRollToAlphaBetaGamma(eulerAngles[1], eulerAngles[2], eulerAngles[3])
	local msg = {}
	msg['x'] = pos[1]
	msg['y'] = pos[2]
	msg['theta'] = alpha -- rotation around z
	simROS.publish(pub,msg)

end

function sysCall_sensing()
    -- put your sensing code here
end

function sysCall_cleanup()
    -- do some clean-up here
end

-- See the user manual or the available code snippets for additional callback functions and detail
