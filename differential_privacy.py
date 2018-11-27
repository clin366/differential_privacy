import pandas as pd
import random
import numpy
import argparse
from matplotlib import pyplot

def plot_laplace(epsilon, original_count, fig_name, scalar):
    count_laplace = []
    # epsilon = 0.01
    loc, scale = 0., 1/epsilon
    for i in original_count:
        s = numpy.random.laplace(loc, scale, 1)

        new_count = i + s[0]
        count_laplace.append(int(max(new_count, 0)))

    pyplot.bar(scalar, original_count, width=5, alpha = 1, label = 'original', color = "white", edgecolor = "red",linestyle = '-')
    pyplot.bar(scalar, count_laplace, width=5, alpha = 0.5, label = 'laplace',color = "white", edgecolor = "grey",linestyle = '--' )
    pyplot.legend(loc='upper right')
    pyplot.savefig(fig_name)
    pyplot.show()


def diff_privacy(data_path, epsilon):

    data_pd = pd.read_csv(data_path)

    original_count = []
    scalar = []

    for i in range(0, 15):
        lower_bound = 15 + i*5
        upper_bound = 20 + i*5
        
        scalar.append(lower_bound + 2.5)
        
        number = data_pd[((data_pd['Age'] > lower_bound) & (data_pd['Age'] <= upper_bound))].shape[0]
        
        original_count.append(number)

    # epsilon = 0.01
    plot_laplace(epsilon, original_count, 'epsilon_'+str(epsilon).split('.')[1], scalar)

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--file_path", type = str, 
                    help="Path to the dataset")
parser.add_argument("-e", "--epsilon", type=float,
                    help="The epsilon value")

args = parser.parse_args()

Flag = True
if args.file_path != None: 
    if args.epsilon != None:
        diff_privacy(args.file_path, args.epsilon)
        Flag = False
if Flag:
    print("Missing necessary file path or epsilon, use --help or -h to see the detail")


