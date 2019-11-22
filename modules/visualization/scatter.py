"""

Various functions for creating scatter plots

"""

import matplotlib.pyplot as plt
import matplotlib


def SimpleScatter(data, config={}, filepath=None, fileconfig={}, show=False):
	"""
	Simple Scatter
	
	data: <dict> a dictionary of shape
		x: [0.0, 1.0, 2.0], #the x coordinates of points
		y: [0.0, 1.0, 2.0], #the y coordinates of points,
		area: [1.0, 2.0, 3.0], #the area of points
		colors: [], #colors of points
		y_label: "", #label for y axis
		x_label: "", #label for x axis
		title: "", #title for plot

	config: <dict> a passable dictionary which can contain any other parameters
	eg: alpha:0.5

	filepath: <string> location to save the plot on disk

	fileconfig: <dict> any additional config parameters for saving the file

	show: <boolean> whether or not to render plot to screen

	

	"""

	plt.scatter(data["x"], data["y"], s=data["area"], c=data["colors"], **config)
	plt.xlabel(data["x_label"])
	plt.ylabel(data["y_label"])
	plt.title(data["title"])
	
	if filepath:
		plt.savefig(filepath, **fileconfig)
	if show:
		plt.show()


if __name__ == '__main__':
	matplotlib.style.use("seaborn")
	data = {
		"x": [0.0, 1.0, 2.0],
		"y": [1.0, 2.0, 3.0],
		"area":[50.0, 100.0, 200.0],
		"colors":["#ff0000", "#00ff00", "#0000ff"],
		"y_label": "y-scatter", 
		"x_label": "x-scatter", 
		"title": "Scatter Example"
	}

	config = {
		"alpha":0.8,
	}
	SimpleScatter(data, config, filepath="tmp/scatter.png", show=True)
