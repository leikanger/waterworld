
using HDF5
PATH_FOR_SITAWARENESS = "/tmp/updated_situation.h5"

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

