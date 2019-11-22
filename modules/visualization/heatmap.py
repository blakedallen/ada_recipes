"""

Various functions for creating Heatmap plots

"""
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib


def SimpleHeatmap(data, config={}, plot_info={}, filepath=None, fileconfig={}, show=False):
	"""
	Simple Heatmap
	
	data: <dict> a dictionary of shape
		x: [0.0, 1.0, 2.0], #the x coordinates of points
		y: [0.0, 1.0, 2.0], #the y coordinates of points,
		area: [1.0, 2.0, 3.0], #the area of points
		colors: [], #colors of points
		y_label: "", #label for y axis
		x_label: "", #label for x axis
		title: "", #title for plot

	config: <dict> a passable dictionary which can contain any other parameters
	eg: linewidth:0.5

	plot_info: information that corressponds to the plot
		- xlabel
		- ylabel
		- title

	filepath: <string> location to save the plot on disk

	fileconfig: <dict> any additional config parameters for saving the file

	show: <boolean> whether or not to render plot to screen

	

	"""	

	sns.heatmap(data, **config)
	plt.xlabel(plot_info["x_label"])
	plt.ylabel(plot_info["y_label"])
	plt.title(plot_info["title"])
	
	if filepath:
		plt.savefig(filepath, **fileconfig)
	if show:
		plt.show()


if __name__ == '__main__':
	matplotlib.style.use("seaborn")
	flights = sns.load_dataset("flights")
	flights = flights.pivot("month", "year", "passengers")
	
	config = {
		"linewidth":0.5,
	}

	plot_info = {
		"y_label": "y-heatmap", 
		"x_label": "x-heatmap", 
		"title": "Heatmap Example"
	}

	SimpleHeatmap(flights, config=config, plot_info=plot_info, filepath="tmp/heatmap.png", show=True)
