# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 12:26:07 2021

@author: Cameron Cummins
"""

import numpy as np
import matplotlib.pyplot as plt
"""
    The following code is sourced from https://en.wikipedia.org/wiki/Euler%E2%80%93Maruyama_method
"""

# In-line function for second equation
equation_two = lambda theta, mu, yt, dt, sigma, noise : theta * (mu - yt) * dt + sigma * noise
def secondEquation(num_sims:int, num_points:int, t_init:float, t_final:float, y_init:float,
                  theta:float = 0.8, mu:float = 1.5, sigma:float = 0.06, noise_center:float = 0.0, noise_scale:float = 0.5):
    """
    Parameters
    ----------
    num_sims : int
        number of simulations to run and calculate data for
    num_points : int
        number of data points to calculate
    t_init : float
        initial time vlaue
    t_final : float
        final time value
    y_init : float
        initial function value
    theta : float, optional
        Value for theta. The default is 0.8.
    mu : float, optional
        Value for mu. The default is 1.5.
    sigma : float, optional
        Value for sigma. The default is 0.06.
    noise_center : float, optional
        Mean for Gaussian noise generator (numpy.random.normal). The default is 0.0.
    noise_scale : float, optional
        Scale for Gaussian noise generate (numpy.random.normal). The default is 0.5.

    Returns
    -------
    sims : list
        list of simulation results, each containing a dictionary with respective 't' and 'y' values
    """

    # In-line function to generate noise
    noise = lambda : np.random.normal(loc = noise_center, scale = noise_scale) #same noise as first equation

    equation_two = lambda theta, mu, yt, dt, sigma, noise : theta * (mu - yt) * dt + sigma * noise

    # Create list for simulations
    sims = []

    # Calculate time delta
    dt = (t_final - t_init) / num_points

    for j in range(num_sims): #going through each sim
        #array for time and y values for this run
        t_vals = []
        y_vals = []

        # Initialize
        t = t_init
        y = y_init
        t_vals.append(t)
        y_vals.append(y)

        #go through each step of the sim
        for i in range(num_points):
            t += dt
            yt = y
            dy = equation_two(theta, mu, yt, dt, sigma, noise()) #current value of y goes into the calculation of the dy
            y = y + dy
            #adding values to the list
            t_vals.append(t)
            y_vals.append(y)
        sims.append({"t_set":t_vals, "y_set":y_vals}) #for each sim, add the t and y values for each to a list of dictionaries
    return sims





def firstEquation(num_sims:int, num_points:int, t_init:float, t_final:float, y_init:float,
                  mu:float = 1.5, sigma:float = 0.06, noise_center:float = 0.0, noise_scale:float = 0.5):
    """
    Parameters
    ----------
    num_sims : int
        number of simulations to run and calculate data for
    num_points : int
        number of data points to calculate
    t_init : float
        initial time vlaue
    t_final : float
        final time value
    y_init : float
        initial function value
    mu : float, optional
        Value for mu. The default is 1.5.
    sigma : float, optional
        Value for sigma. The default is 0.06.
    noise_center : float, optional
        Mean for Gaussian noise generator (numpy.random.normal). The default is 0.0.
    noise_scale : float, optional
        Scale for Gaussian noise generate (numpy.random.normal). The default is 0.5.

    Returns
    -------
    sims : list
        list of simulation results, each containing a dictionary with respective 't' and 'y' values
    """
    # In-line function for first equation
    equation_one = lambda mu, dt, sigma, noise : mu * dt + sigma * noise

    # In-line function to generate noise
    noise = lambda : np.random.normal(loc = noise_center, scale = noise_scale)

    # Create list for simulations
    sims = []

    # Calculate time delta
    dt = (t_final - t_init) / num_points
    for sim in range(num_sims):
        # Create lists for storing points
        t_values = []
        y_values = []

        # Initialize
        t = t_init
        y = y_init
        t_values.append(t)
        y_values.append(y)

        # Iterate through 'N' to calculate values of 't' and 'y'
        for index in range(num_points):
            t += dt
            y = y + equation_one(mu, dt, sigma, noise())
            t_values.append(t)
            y_values.append(y)
        sims.append({"t_set":t_values, "y_set":y_values})
    return sims
"""
    End of sourced code.
"""

def plotAndOutputResults(simulation_results:list, path:str):
    """
    Parameters
    ----------
    simulation_results : list
        list of results for any number of simulations run
    path : str
        path to output image of figure to

    Returns
    -------
    None.
    """
    figure = plt.figure()
    figure_axis = figure.add_subplot()

    for result in simulation_results:
        figure_axis.plot(result["t_set"], result["y_set"])

    figure_axis.set_xlabel("time (s)")
    h = figure_axis.set_ylabel("y")
    h.set_rotation(0)

    figure.savefig(path)

# Example useage
plotAndOutputResults(secondEquation(5, 1000, 3, 7, 0), "output.png")
