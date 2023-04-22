# MANE_6962_project
Flow Prediction using sequential neural network

#Brief Description
The goal of this project is to build a CNN-LSTM model that will be used predict flow at future time steps. The work flow is as follows:
1. Run the fluid test case using [OpenIFEM](https://github.com/OpenIFEM/OpenIFEM)
2. Postprocess the results to obtain the solution at the nodes.
3. Rearrange the data solution into a sequential data of shape (num_timesteps, sequence_length, num_features)
4. Use the sequential data to train an LSTM model to make predictions at future time steps.

