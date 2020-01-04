
from ..modules.visualization.bar import simple_bar


def main():
    """ create a bar chart from some data """
    
    data = {
        "x_titles":["foo","bar","baz"],
        "x":[0.0,1.0,2.0],
        "heights":[1.0, 2.0, 3.0],
    }
    simple_bar(data, show=True)

if __name__ == "__main__":
    main()



