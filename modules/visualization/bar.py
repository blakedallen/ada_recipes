"""

Various functions for creating bar charts

"""

import matplotlib.pyplot as plt
import matplotlib


def simple_bar(data, config={}, filepath=None, fileconfig={}, show=False):
	"""
	Simple Bar, 
	creates a simple bar plot
	
	data: <dict> a dictionary of shape
		x_titles: ["foo", "bar", "baz"],
		x: [0.0, 1.0, 2.0], #the x coordinates of the bars
		heights: [1.0, 2.0, 3.0], #the height(s) of the bars,
		

	config: <dict> a passable dictionary which can contain any other parameters

	filepath: <string> location to save the plot on disk

	fileconfig: <dict> any additional config parameters for the bar chart

	show: <boolean> whether or not to render plot to screen

	returns: BarContainer
	#https://matplotlib.org/3.1.1/api/container_api.html#matplotlib.container.BarContainer

	"""
	p = plt.bar(data["x"],data["heights"], **config)
	plt.xticks(data["x"], data["x_titles"])
	plt.xlabel(config["x_label"])
	plt.ylabel(config["y_label"])
	plt.title(config["title"])
	
	if filepath:
		plt.savefig(filepath, **fileconfig)
	if show:
		plt.show()
	return p




if __name__ == '__main__':
	matplotlib.style.use("seaborn")
	data = {
		"x_titles":["foo", "bar", "baz"],
		"x": [0.0, 1.0, 2.0], #the x coordinates of the bars
		"heights": [1.0, 2.0, 3.0], #the height(s) of the bars,
		
	}

	config = {
		"color":["#008080", "teal", (0.2, 0.3, 0.4)],
		"y_label": "y-bar", #label for y axis
		"x_label": "x-bar", #label for x axis
		"title": "Bar Example"
	}
	simple_bar(data, config, filepath="tmp/bar.png", show=True)
