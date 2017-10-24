#!/usr/bin/env python3

import numpy as np
import pandas as pd


def init_grid(N):
    """
        INITIALIZES GRID FOR FFT
        INPUT :
            N(int) size of the grid
        OUTPUT :
            grid(pandas dataframe) 4 columns (x,y,z, resloc)
    """
    x = []
    y = []
    z = []
    for i in range(0,N+1):
        for j in range(0,N+1):
            for k in range(0,N+1):
                x.append(i)
                y.append(j)
                z.append(k)

    resloc = [0] * len(x)
    grid = np.array((x, y, z, resloc), dtype=int)
    grid = pd.DataFrame(grid.transpose())
    return(grid)

def dist_cal(x1, y1, z1, x2, y2, z2):
    """
        CALCULATES DISTANCE BETWEEN TWO POINTS IN 3D
        INPUT :
            x1(float)
            y1(float)
            z1(float)
            x2(float)
            y2(float)
            z2(float)
        OUTPUT :
            dist(float)
    """
    dist = sqrt((x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2)
    return(dist)

def fill_grid(grid, coords, thresh):
    """
        FILL GRID FOR FFT ACCORDING TO RESIDUE POSITION AND DEPTH
        INPUT :
            grid(pandas dataframe) empty grid generated by init_grid() function
            coords(pandas dataframe) residue coordinates (x,y,z) and depth from read scale_coords() function
            thresh(float) threshold for distance cuttof
        OUTPUT :
            grid(pandas dataframe) grid for FFT with 1 for points at surface, -1 for points in the core, 0 for points outside
    """
    for i in range(0,len(grid.index)):
        flag = False
        for j in range(0, len(coords.index)):
            dist = dist_cal(x1 = grid.iloc[i,0], y1 = grid.iloc[i,1], z1 = grid.iloc[i,2], x2 = coords.iloc[j,0], y2 = coords.iloc[j,1], z2 = coords.iloc[j,2])
            if dist < thresh:
                if coords.iloc[j,3] == 1:#surface
                    grid.iloc[i,3] = 1
                    continue
                elif coords.iloc[j,3] == -1:# inside prot
                    grid.iloc[i,3] = -1
                    flag = True
            elif flag == False:
                grid.iloc[i,3] = 0 # outside

    return(grid)

if __name__ == "__main__":
    mygrid = init_grid(65)