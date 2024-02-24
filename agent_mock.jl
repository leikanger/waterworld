using HDF5
PATH_FOR_Q_CHANNEL = "/tmp/neoRL/channel_for_q_value.h5"
# Har gått vekk fra dette: PATH_FOR_EVENT_REPORTING =  "/tmp/neoRL/new_event.h5"
using ZMQ
ctx = Context()
s1 = Socket(ctx, PULL)
connect(s1, "tcp://localhost:5555")


for x in 1:1000
	q_vector = zeros(5);
	(x%5==1) && (q_vector[1] = 1.0)
	(x%5==2) && (q_vector[2] = 1.0)
	(x%5==3) && (q_vector[3] = 1.0)
	(x%5==4) && (q_vector[4] = 1.0)
	(x%5==0) && (q_vector[5] = 1.0)
	#@show q_vector
	sleep(0.2)
	try 
		h5open(PATH_FOR_Q_CHANNEL, "w") do file
			#file.create_dataset("q_vector", data=q_vector)
			@write file q_vector
		end
	catch
		continue
	end

	# Receive request
    msg = recv(s1, String)
    println("Received from Python: $msg")
	received_event_id = parse(Int, msg[9:end]);

	#while true
	#	try 
	#		h5open(PATH_FOR_EVENT_REPORTING, "r") do file
	#			#file.create_dataset("q_vector", data=q_vector)
	#			data = read(file);
	#			if(data["new_event"]!=4)
	#				println("new action: ", data["new_event"]);
	#			end
	#		end
	#		break
	#	catch
	#		continue
	#	end
	#end
end
