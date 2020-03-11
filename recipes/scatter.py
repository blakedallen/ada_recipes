import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib

sns.set()

def main(d, path=None, show=True):
    """ create a scatterplot 
        path: optional file location to save data
        show: boolean, whether to render plot to screen
    """
    
    p = plt.scatter(d["x"],d["y"])
    plt.xlabel(d["x_label"])
    plt.ylabel(d["y_label"])
    plt.title(d["title"])
    if path:
        plt.savefig(path)
    if show:
        plt.show()

def define_data():
    """ function to create our mock dataset """
    d = {
        "x":[0.0,1.0,2.0,3.0], #x coordinates of the points
        "y":[1.2, 2.3, 1.7, 0.5], #y coordinates of the points
        "x_label":"Provisions",
        "y_label":"Amount",
        "title":"Breakfast",
    }
    return d

if __name__ == "__main__":
    dataset = define_data()
    main(dataset)



