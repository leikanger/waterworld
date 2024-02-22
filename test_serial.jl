using HDF5

case_data = [.1, .2, .4, .1]

PATH_FOR_SITAWARENESS = "/tmp/updated_situation.h5"
    #PATH_FOR_Q_INPUT = "/tmp/new_q_value.h5"

path = "/tmp/liaison.h5";
# file = File(format"JLD2", path)

h5open(path, "w") do file
	write(file, "mydataset", case_data)
end

function write_new_q_vector(path::String, data::Vector{Float64})
	h5open(path, "w") do file
		write(file, "Q-values", data)
	end
end


write_new_q_vector("/tmp/liaison.h5", [1.,1.,1.,1.])



for x in 1:1000
	# BRA: TODO Bruk gruppe for å kva EoI det er snakk om:
	#	data = h5read(PATH_FOR_SITAWARENESS, "mygroup2/A", (2:3:15, 3:5))

	try 
		h5open(PATH_FOR_SITAWARENESS, "r") do file
			data = read(file)
			#data = h5read(PATH_FOR_SITAWARENESS)
			@show data
			#read_accepted = true
		end
	catch
		continue
	end
		
	sleep(0.1)
end
	#h5open(path, "r") do file
	#	println(read(file, "A"

