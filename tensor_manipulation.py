import torch
import numpy as np
import torchvision
import cv2
import torchvision.transforms.functional as F
data = [[[1,2,3,], [4,5,6], [7,8,9]],[[1,2,3,], [4,5,6], [7,8,9]]]

np_array = np.array(data)
print(np.shape(np_array))
print(np.ndim(np_array))


tensor_data = torch.tensor(data)
print(tensor_data.shape)
print(tensor_data.type())

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
np_to_tensor = torch.as_tensor(np_array,device=device)
print(np_to_tensor)
print(np_to_tensor.device)
print(np_to_tensor.shape)   #Size and shape are same for a tensor.
print(np_to_tensor.size())



# np_arr_on_gpu = np_array.to(device=device)   #Can't be possible to move a numpy array directly to the GPU. You need libraries like CuPy to convert a numpy array to a GPU array.
# print(np_arr_on_gpu)
# print(np_arr_on_gpu.device)


print(np_to_tensor[0][0][0])

image_path = r"C:\Users\rayde\OneDrive\Desktop\label_studio\label-studio-data\data\EMCD_2\frame_4920.jpg"

img = torchvision.io.read_image(image_path)
print(f"Original Image Shape {img.shape}")
print(img.type())
print(img)
img_cv2 = img.permute(1,2,0).numpy()
# cv2.imshow("Image", img_cv2)
# cv2.waitKey(0)


reshaped_img = torch.reshape(img , (3, 848,478))
print(reshaped_img.shape)
    
reshaped_img_cv2 = reshaped_img.permute(1,2,0).numpy()
# cv2.imshow("Reshaped Image", reshaped_img_cv2)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# USE 1
rand_img = torch.rand(3,4)
flattened_rand_img = torch.reshape(rand_img ,(-1,))
print(rand_img,rand_img.shape)
print(flattened_rand_img,flattened_rand_img.shape)


#Use 2

rand_img2 = torch.arange(12)
reshaped_rand_img2 = torch.reshape(rand_img2, (4, -1))   #Replace 4 with 5 to see how the reshape function throws an error when the number of elements in the original tensor is not compatible with the new shape.
print(rand_img2,rand_img2.shape)
print(reshaped_rand_img2,reshaped_rand_img2.shape)


resized_img = F.resize(img,[2])
print(resized_img)

print(rand_img2.view)