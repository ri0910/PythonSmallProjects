import matplotlib.pyplot as plt

def graph_plot():
    x_plot = [3,5,6]
    y_plot = [1,2,3]
    plt.plot(x_plot, y_plot, 'red')
    plt.xlabel("X axis")
    plt.ylabel("Y axis")
    plt.title("Graph Plot")
    plt.show()

graph_plot()