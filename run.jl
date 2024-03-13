using PyCall
pushfirst!(pyimport("sys")."path", "");
Env = pyimport("env_waterworld");


for iter in 1:1000
	try
		Env.step_control()
		sleep(0.03)
	catch err
		println("WaterWorld was terminated from the Python side. Goodbye.");
		break;
	end
end
