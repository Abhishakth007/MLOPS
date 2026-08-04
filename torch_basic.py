import torch
import time
x = torch.cuda.is_available()
y = torch.rand(1,10)
print(x)
print(y)

data = [[1,2,3,], [4,5,6]]
tensor_data = torch.tensor(data)
print(tensor_data.type())


import numpy as np
print(np.__version__)


np_to_tensor = np.array(data) 
x_np = torch.from_numpy(np_to_tensor)
print(x_np.type())

tensor_ones_data = torch.ones_like(tensor_data)   #Ones like will create a tensor of ones with the same shape as the input tensor(tensor_data)
print(tensor_ones_data)

tensor_rand_data = torch.rand_like(tensor_data , dtype = torch.float)  
print(tensor_rand_data)

x_shape = (2)
print(type(x_shape))
rand_tensor = torch.rand(x_shape)
print(rand_tensor)



rand_tensor = torch.rand(5000,5000)

# CPU Operation
print(rand_tensor.device)
rand_tensor_cpu = rand_tensor.to('cpu')

time_start = time.perf_counter()
rand_tensor_cpu = rand_tensor_cpu * rand_tensor_cpu *rand_tensor_cpu
time_end = time.perf_counter()
print(f"Cpu Time taken = {time_end - time_start:.6f} seconds")

# GPU Operation
print(rand_tensor.device)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
rand_tensor_gpu = rand_tensor.to(device)
torch.cuda.synchronize()  # Synchronize the GPU before starting the timer

time_start = time.perf_counter()
rand_tensor_gpu = rand_tensor_gpu * rand_tensor_gpu*rand_tensor_gpu
torch.cuda.synchronize()

time_end = time.perf_counter()
print(rand_tensor_gpu.device)
print(f"GPU Time taken = {time_end - time_start:.6f} seconds")


device_test = torch.accelerator.current_accelerator().type if torch.accelerator.is_available() else "No accelerator available"
print(device_test)

tensor_slicing = torch.ones(5,5)
tensor_slicing[:,2:3] = 0
print(tensor_slicing)