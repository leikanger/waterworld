using HDF5
PATH_FOR_Q_CHANNEL = "/tmp/channel_for_q_value.h5"

for x in 1:100
	q_vector = zeros(5);
	(x%5==1) && (q_vector[1] = 1.0)
	(x%5==2) && (q_vector[2] = 1.0)
	(x%5==3) && (q_vector[3] = 1.0)
	(x%5==4) && (q_vector[4] = 1.0)
	(x%5==0) && (q_vector[5] = 1.0)
	@show q_vector
	sleep(0.2)
	try 
		h5open(PATH_FOR_Q_CHANNEL, "w") do file
			#file.create_dataset("q_vector", data=q_vector)
			@write file q_vector
		end
	catch
		continue
	end
end
