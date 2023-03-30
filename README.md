# MANE_6962_project
An implementation of a CNN-LSTM model to predict fluid flow

#Brief Description
The goal of this project is to build a CNN-LSTM model that will be used predict flow at future time steps. The work flow is as follows:
1. Run the fluid test case using [OpenIFEM](https://github.com/OpenIFEM/OpenIFEM)
2. Postprocess the results to obtain the solution at the nodes.
3. Feed the postprocessed results into a CNN to reduce the dimensionality 
4. Feed the output of the CNN into the LSTM model to make prediction at the next time step.

