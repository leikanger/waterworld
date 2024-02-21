import h5py
import numpy as np

path = "/tmp/liaison.h5"
with h5py.File(path, 'r') as f:
    the_var = f["Q-values"]

    print(np.size(the_var))
    print(the_var[:])
