# Basic Network Simulator 

This project provides a simple network simulation tool implemented using Python and FastAPI. It allows users to interactively add devices, connect devices, remove devices, remove connections between devices, and visualize the network graph.

### Prerequisites

- Python 3.12 or higher
- `git` installed on your machine

## Files

1. `main.py`: This file contains the FastAPI application setup and defines the API endpoints for interacting with the network simulation.

2. `network_simulation.py`: This file defines the `NetworkSimulation` class, which encapsulates the logic for managing the network graph and performing operations such as adding/removing devices and connections, and plotting the network.

3. `index.html`: This file contains the HTML and JavaScript code for the front-end interface of the network simulation. It provides buttons for adding devices, connecting devices, removing devices, removing connections, and plotting the network graph.


## Installation

Install Aihcon Patients Service Project

Step 1: Clone the Repository
```shell
git clone https://github.com/aihcon-jahid/Basic-Network-Simulator.git
```

Step 2: Navigate to the Project Directory
```shell
cd Basic-Network-Simulator
```

Step 3: Create a Virtual Environment
```shell
python -m venv .venv
```

Step 4: Activate the Virtual Environment

- On Windows:
```shell
.venv\Scripts\activate
```

Step 5: Install Dependencies
```shell
pip install -r requirements.txt
```


Step 6: Executing the Program
```shell
python main.py
```
- or

```shell
uvicorn main:app --host 127.0.0.1 --port 8000 --reload
```
- Open your browser and navigate to: [http://127.0.0.1:8000](http://127.0.0.1:8000) 


2. Open `index.html` in a web browser to access the front-end interface.

3. Use the provided buttons to interact with the network simulation:
    - Add Device: Add a new device to the network.
    - Connect Devices: Connect two devices in the network.
    - Remove Device: Remove a device from the network.
    - Remove Connection: Remove the connection between two devices.
    - Plot Network: Visualize the current state of the network graph.

## Dependencies

- FastAPI: A modern, fast (high-performance), web framework for building APIs with Python.
- NetworkX: A Python package for the creation, manipulation, and study of complex networks.
- Matplotlib: A comprehensive library for creating static, animated, and interactive visualizations in Python.
- Uvicorn: An ASGI server implementation, which stands for Asynchronous Server Gateway Interface.

## Author

- Khadizatul Kobra


