import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

contour_levels = [-500,-100,-20,-5,1,5,10,20,40,60,100,500]
def plot_relative_difference(Frame):
    Coord = pd.read_csv('COOR_BFAF.csv', sep='\s+')
    U = pd.read_csv(f'{Frame}u.csv',sep='\s+',nrows=3838)
    # Load the CSV file into a pandas DataFrame, and formatic the data
    df_1 = pd.concat([Coord,U],axis=1)
    df_1 ['Z']=-df_1 ['Z']
    df_1['U3'] =1000* df_1['U3']
    df_1['X'] = df_1['X']/1.12
    df_1['Z'] = df_1['Z'] / 1.12
    # Creating a contour plot using the filtered DataFrame
    plt.figure(figsize=[4, 8])
    contour_plot = plt.tricontour(df_1['X'], df_1['Z'], df_1['U3'],
                                  linestyles='solid', levels=contour_levels, colors='black')
    contour_plot_0line = plt.tricontour(df_1['X'], df_1['Z'], df_1['U3'],
                                  linestyles='solid', levels=[0], colors='red')
    plt.clabel(contour_plot,fmt='%.1f', inline=True, fontsize=8, inline_spacing=1)
    plt.clabel(contour_plot_0line, fmt='%.1f', inline=True, fontsize=8, inline_spacing=1)
    # Adding a rectangle with the specified coordinates (without filling, only edge line)
    rect_x1=[0,0.5,0.5,0]
    rect_y1=[(-16.8+Frame*0.2)/1.12,(-16.8+Frame*0.2)/1.12,Frame*0.2/1.12,Frame*0.2/1.12]
    plt.fill(rect_x1,rect_y1,zorder=10,  fill=True, color='darkgrey', edgecolor='black', linewidth=1.0, alpha=1.0)
    plt.xlim([0, 10])
    plt.ylim([18,1])
    plt.xlabel('Normalised distance from the pile axis: $r/D$')
    plt.ylabel('Normalised depth: $z/D$')
    #plt.title('Contour Plot of Relative Difference in S11 with Rectangle Outline')
    plt.gca().set_aspect('equal', adjustable='box')
    #plt.gca().axes.get_xaxis().set_visible(False)  # Hide the stick numbers on x axis
    #plt.gca().axes.get_yaxis().set_visible(False)  # Hide the stick numbers on y axis
    #plt.show()
    plt.savefig(f'{Frame}.jpg',format='jpg',dpi=400)
    plt.close()
#plot_relative_difference( Frame=40)
for i in range(0,83):
    plot_relative_difference( Frame=i)

