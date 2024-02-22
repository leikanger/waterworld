
using HDF5
PATH_FOR_SITAWARENESS = "/tmp/updated_situation.h5"

struct EoI
	_values::Vector{Float64}
	priority::Float64
end


for x in 1:1000
	# BRA: TODO Bruk gruppe for å kva EoI det er snakk om:
	#	data = h5read(PATH_FOR_SITAWARENESS, "mygroup2/A", (2:3:15, 3:5))

	all_eoi = Vector{EoI}()
	try 
		h5open(PATH_FOR_SITAWARENESS, "r") do file
			data = read(file)

			for elem in eachslice(data["positive_eoi"]; dims=2) 
				push!(all_eoi, EoI(elem, 1.0))
			end
			for elem in eachslice(data["negative_eoi"]; dims=2) 
				push!(all_eoi, EoI(elem, -1.0))
			end
			#read_accepted = true
		end
	catch
		continue
	end
		
	println("\n\n")
	for elem in all_eoi
		println(elem.priority, "\t for pos: ", elem._values)
	end
	sleep(0.1)
end
	#h5open(path, "r") do file
	#	println(read(file, "A"

