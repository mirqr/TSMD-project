# TSMD Course Project: Analysis of Aircraft Flight Data


## Overview

This repository contains two Jupyter notebooks developed for the **Time Series and Mobility Data (TSMD)** course project. The project focuses on analyzing aircraft flight data provided by the OpenSky Network, using mobility data analysis and time series analysis techniques.

### PART 1 - Mobility Data
In this part, we explore and analyze a dataset containing aircraft flight data. The analysis includes data interpolation, stop detection, and visualization of aircraft flow between countries using the `skmob` library.

### PART 2 - Time Series Analysis
This part focuses on clustering and classification of flight route trajectories using the same OpenSky dataset, emphasizing the variable length of time series data.

## OpenSky Network
We utilize aircraft flight data provided by the OpenSky Network, which offers real-time and historical flight data collected by a global network of sensors. More details about the dataset and its usage can be found within the notebooks.

More detailed explanations and comments can be found within the notebooks.



## Installation

To set up the environment, use the provided `environment.yml` file. It is recommended to run this project on a server.

```sh
conda env create -f environment.yml
