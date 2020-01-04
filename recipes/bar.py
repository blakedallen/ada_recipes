
import matplotlib.pyplot as plt
import matplotlib

def main(d, path=None, show=True):
    """ create a bar chart from some data """
    
    p = plt.bar(d["x"],d["y"])
    plt.xticks(d["x"], d["x_titles"])
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
        "x":[0.0,1.0,2.0,3.0], #x coordinates of the bars
        "y":[1.2, 2.3, 1.7, 0.5], #heights of the bars
        "x_titles":["bacon","eggs","toast","bagels"], #titles for the bars
        "x_label":"Provisions",
        "y_label":"Amount",
        "title":"Breakfast",
    }
    return d

if __name__ == "__main__":
    dataset = define_data()
    main(dataset)



