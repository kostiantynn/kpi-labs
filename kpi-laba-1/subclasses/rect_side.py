# in the subfunction I'm going to use matplotlib library to display grafic onto coordinate system

from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle
from . import rect_midle #importing second subfile

def rect_side(a,b,c,d):
    # defining a figure
    fig2 = plt.figure()
    ax2 = fig2.add_subplot(aspect='equal')

    # displaying rectangles
    ax2.add_patch(Rectangle((1,1), c, d, fill=None))
    ax2.add_patch(Rectangle((c/2-a/2,1), a, b, fill=None))
    ax2.add_patch(Rectangle((1,d/2-b/2), a, b, fill=None))
    ax2.add_patch(Rectangle((c-a+1,d/2-b/2), a, b, fill=None))
    ax2.add_patch(Rectangle((c/2-a/2,d-b+1), a, b, fill=None))

    plt.ylim((0,d+10))
    plt.xlim((0,c+10))

    # executing second subfil
    rect_midle.rect_midle(a,b,c,d)

    # executing current file
    plt.show()
