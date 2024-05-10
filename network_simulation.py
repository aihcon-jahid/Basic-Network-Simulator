# Import necessary modules and libraries
import networkx as nx
import matplotlib.pyplot as plt
import io
import base64
import random 

class NetworkSimulation:
    def __init__(self):
        """
        Initialize a NetworkSimulation object with an empty graph and positions dictionary.
        """
        self.graph = nx.Graph()
        self.positions = {}

    def add_device(self, device_name):
        """
        Add a device to the network graph.

        Args:
            device_name (str): The name of the device to be added.
        """
        self.graph.add_node(device_name)
        self.positions = nx.spring_layout(self.graph)

    def remove_device(self, device_name):
        """
        Remove a device from the network graph.

        Args:
            device_name (str): The name of the device to be removed.

        Returns:
            bool: True if the device was successfully removed, False otherwise.
        """
        if device_name in self.graph.nodes:
            self.graph.remove_node(device_name)
            self.positions = nx.spring_layout(self.graph)
            return True
        else:
            return False

    def connect_device(self, device1, device2):
        """
        Connect two devices in the network graph.

        Args:
            device1 (str): The name of the first device.
            device2 (str): The name of the second device.
        """
        self.graph.add_edge(device1, device2)
        self.positions = nx.spring_layout(self.graph)

    def remove_connect_device(self, device1, device2):
        """
        Remove the connection between two devices in the network graph.

        Args:
            device1 (str): The name of the first device.
            device2 (str): The name of the second device.
        """
        self.graph.remove_edge(device1, device2)
        self.positions = nx.spring_layout(self.graph)

    def plot_network(self):
        """
        Plot the network graph with random node colors and return the plot as a base64 encoded image.

        Returns:
            str: Base64 encoded image of the network plot.
        """
        plt.figure(figsize=(8, 6))
        
        # Generate a random color for each node (device)
        node_colors = [self.generate_random_color() for _ in self.graph.nodes]
        
        # Draw the network graph with random node colors
        nx.draw(self.graph, pos=self.positions, with_labels=True, 
                node_color=node_colors, edge_color='blue', 
                node_size=500, font_size=16)
        
        # Convert the plot to image and encode as base64
        img_buf = io.BytesIO()
        plt.savefig(img_buf, format='png')
        plt.close()
        img_buf.seek(0)
        image_base64 = base64.b64encode(img_buf.read()).decode('utf-8')
        return image_base64

    def generate_random_color(self):
        """
        Generate a random RGB color tuple.

        Returns:
            tuple: A tuple representing a random RGB color.
        """
        # Generate random RGB values for color
        r = random.random()
        g = random.random()
        b = random.random()
        return (r, g, b)
