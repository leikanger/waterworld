using HDF5

case_data = [.1, .2, .4, .1]

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
