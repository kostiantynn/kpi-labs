# in the subfunction I'm going to use matplotlib library to display grafic onto coordinate system

from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle

def rect_midle(a,b,c,d):
    # defining a figure
    fig1 = plt.figure()
    ax1 = fig1.add_subplot(aspect='equal')

    # displaying rectangles
    ax1.add_patch(Rectangle((1,1), c, d, fill=None))
    ax1.add_patch(Rectangle((c/2-a/2,d/2-b/2), a, b, fill=None))

    plt.ylim((0,d+10))
    plt.xlim((0,c+10))

    # executing current file
    plt.show()
