using PyCall
pushfirst!(pyimport("sys")."path", "");
Env = pyimport("env_waterworld");

function run_main_loop(iterations::Int)
	for iter in 1:iterations
		try
			Env.step_control()
			sleep(0.03)
		catch err
			println("WaterWorld was terminated from the Python side. Goodbye.");
			break;
		end
	end
end






function main()
	@async run_main_loop(1000)
	for i in 1:100 
		println("ei av hundre uskrifter: " * string(i))
		sleep(0.2)
	end

	println("Ferdig")
end
main()
