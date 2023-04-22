#This script helps to extract the velocity from the csv file generated
#for each time step and saves the data as a npy file

import numpy as np
import os

current_path = os.path.dirname(os.path.abspath(__file__))
print(current_path)

num_time_steps= 5000
reserved_steps=20
num_features=100
data_per_timestep = np.ones((num_features)).reshape(1,num_features)
test_train_data=np.zeros((num_time_steps-reserved_steps,num_features))
reserved_data=np.zeros((reserved_steps,num_features))
vel_mag_data=np.zeros((num_time_steps,num_features))


#get the velocity x and y values from the csv file and compute the velcity magnitude

for i in range(1,num_time_steps+1):
    print("the i value is",i)
    file_path="./re_200_csv/resampled_values_"+ str(i) + ".csv"
    my_array=np.loadtxt(file_path,skiprows=1,delimiter=',')
    temp_array=np.linalg.norm(my_array[:num_features,2:4],axis=1)
    vel_mag_data[i-1] =temp_array
    if i<=test_train_data.shape[0]:
        test_train_data[i-1] =temp_array
    else:
        reserved_data[i-test_train_data.shape[0]-1] =temp_array



#print(output_array)
print("Shape of vel mag data is : ",vel_mag_data.shape)
print("vel_mag_data is: ",vel_mag_data[20,:])

# Save the arrays as npy files
re_200_input=np.save('re_200_input_2.npy', test_train_data.data)
re_200_reserved=np.save('re_200_reserved_2.npy', reserved_data.data)
re_200_vel_mag=np.save('re_200_vel_mag_2', vel_mag_data.data)



