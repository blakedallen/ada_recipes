
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
sns.set()


def main(d, path=None, show=True):
    """ create a timeseries chart from some data
        
        note: The optional parameter fmt is a convenient way for defining basic formatting like color, marker and linestyle. It's a shortcut string notation described in the Notes section below
        '.'	point marker
        ','	pixel marker
        'o'	circle marker
        'v'	triangle_down marker
        '^'	triangle_up marker
        '<'	triangle_left marker
        '>'	triangle_right marker
        '1'	tri_down marker
        '2'	tri_up marker
        '3'	tri_left marker
        '4'	tri_right marker
        's'	square marker
        'p'	pentagon marker
        '*'	star marker
        'h'	hexagon1 marker
        'H'	hexagon2 marker
        '+'	plus marker
        'x'	x marker
        'D'	diamond marker
        'd'	thin_diamond marker
        '|'	vline marker
        '_'	hline marker
        Line Styles

        character	description
        '-'	solid line style
        '--'	dashed line style
        '-.'	dash-dot line style
        ':'	dotted line style
        Example format strings:

        'b'    # blue markers with default shape
        'or'   # red circles
        '-g'   # green solid line
        '--'   # dashed line with default color
        '^k:'  # black triangle_up markers connected by a dotted line
        Copy to clipboard
        Colors

        The supported color abbreviations are the single letter codes

        character	color
        'b'	blue
        'g'	green
        'r'	red
        'c'	cyan
        'm'	magenta
        'y'	yellow
        'k'	black
        'w'	white.
    
    """
    
    p = plt.plot_date(d["x"],d["y"], fmt="g-.")
    plt.xticks(d["x"], d["x"])
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
        "x":["Jan 1st","Jan 2nd","Jan 3rd","Jan 4th", "Jan 5th", "Jan 6th", "Jan 7th"], #x coordinates equate to dates
        "y":[14.0, 13.2, 12.3, 9.9, 8.1, 9.9, 13.5], #y coordinates of the values
        "x_titles":["bacon","eggs","toast","bagels"], #titles for the bars
        "x_label":"Provisions",
        "y_label":"Amount",
        "title":"Breakfast Provisions by Day",
    }
    return d

if __name__ == "__main__":
    dataset = define_data()
    main(dataset)



