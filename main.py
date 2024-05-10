# Import necessary modules and libraries
from fastapi import FastAPI, HTTPException
from network_simulation import NetworkSimulation
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

# Create FastAPI instance with title
app = FastAPI(title="Network Simulation")

# Enable CORS with whitelist domains
whitelist_website = ["*"]  # add whitelist domain
app.add_middleware(
    CORSMiddleware,
    allow_origins=whitelist_website,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize NetworkSimulation object
network = NetworkSimulation()

# Endpoint to add a device to the network
@app.post("/add_device/", tags=["Add device"])
def add_device(device_name: str):
    """
    Add a device to the network.

    Args:
        device_name (str): The name of the device to be added.
    
    Returns:
        dict: A message confirming the addition of the device.
    """
    network.add_device(device_name)
    return {"message": f"Device '{device_name}' added"}

# Endpoint to remove a device from the network
@app.delete("/remove_device/", tags=["Remove device"])
def remove_device(device_name: str):
    """
    Remove a device from the network.

    Args:
        device_name (str): The name of the device to be removed.
    
    Returns:
        dict: A message confirming the removal of the device.
    
    Raises:
        HTTPException: If the device to be removed is not found.
    """
    removed = network.remove_device(device_name)
    if removed:
        return {"message": f"Device '{device_name}' removed"}
    else:
        raise HTTPException(status_code=404, detail=f"Device '{device_name}' not found")

# Endpoint to connect two devices in the network
@app.post("/connect_device/", tags=["Connect device"])
def connect_device(device1: str, device2: str):
    """
    Connect two devices in the network.

    Args:
        device1 (str): The name of the first device.
        device2 (str): The name of the second device.
    
    Returns:
        dict: A message confirming the connection between the devices.
    
    Raises:
        HTTPException: If one of the devices is not found.
    """
    if not network.graph.has_node(device1) or not network.graph.has_node(device2):
        raise HTTPException(status_code=404, detail="One of the devices not found")
    network.connect_device(device1, device2)
    return {"message": f"Devices '{device1}' and '{device2}' connected"}

# Endpoint to remove the connection between two devices in the network
@app.delete("/remove_connect_device/", tags=["Remove connection"])
def remove_connect_device(device1: str, device2: str):
    """
    Remove the connection between two devices in the network.

    Args:
        device1 (str): The name of the first device.
        device2 (str): The name of the second device.
    
    Returns:
        dict: A message confirming the removal of the connection between the devices.
    
    Raises:
        HTTPException: If one of the devices or the connection is not found.
    """
    if not network.graph.has_node(device1) or not network.graph.has_node(device2):
        raise HTTPException(status_code=404, detail="One of the devices not found")
    if not network.graph.has_edge(device1, device2):
        raise HTTPException(status_code=404, detail="Connection between devices not found")
    network.remove_connect_device(device1, device2)
    return {"message": f"Connection between '{device1}' and '{device2}' removed"}

# Endpoint to plot the network graph
@app.get("/plot_network/", tags=["Plot network"])
def plot_network():
    """
    Plot the network graph and return the plot as a base64 encoded image.

    Returns:
        dict: Base64 encoded image of the network plot.
    """
    image = network.plot_network()
    return {"image": image}

# Run the FastAPI app using uvicorn server
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
