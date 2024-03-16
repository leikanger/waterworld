using Hugin
using PyCall
pushfirst!(pyimport("sys")."path", "");
Env = pyimport("env_waterworld");

exception_channel = Channel{Any}(1);

function run_main_loop(iterations::Int)
	for iter in 1:iterations
		try
			Env.step_control()
			sleep(0.03)
		catch err
			println("WaterWorld was terminated from the Python side. Goodbye.");
			put!(exception_channel, err);
			break;
		end
	end
end






function main()
	try
		@async run_main_loop(1000)
		for i in 1:100 
			println("ei av hundre uskrifter: " * string(i))
			@show typeof(Env.observe_situation()["EoI+"])
			sleep(0.2)

			# Check if there's an exception in the channel
			if isready(exception_channel)
				# Handle the exception
				e = take!(exception_channel)
				throw(e);
				#println("Caught exception from async task: ", e)
			end
		end
	catch err
		if err isa PyCall.PyError
			println("Terminating HAL for WaterWorld");
		end
	end
	println("Ferdig")
end
main()
