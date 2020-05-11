import numpy as np

def create_laplacian(glon,glat,grid_cell):
    sz = np.size(glon)
    L = np.zeros((sz,sz))

    for i in np.arange(0,sz):

        ind = []
        find_val = (glat == glat[i] + grid_cell)*(glon == glon[i])
        ind.append(np.where(np.squeeze(find_val)))

        find_val = (glat == glat[i] + grid_cell)*(glon == glon[i] + grid_cell)
        ind.append(np.where(np.squeeze(find_val)))

        find_val = (glat == glat[i])*(glon == glon[i] + grid_cell)
        ind.append(np.where(np.squeeze(find_val)))

        find_val = (glat == glat[i] - grid_cell)*(glon == glon[i] + grid_cell)
        ind.append(np.where(np.squeeze(find_val)))

        find_val = (glat == glat[i] - grid_cell)*(glon == glon[i])
        ind.append(np.where(np.squeeze(find_val)))

        find_val = (glat == glat[i] - grid_cell)*(glon == glon[i] - grid_cell)
        ind.append(np.where(np.squeeze(find_val)))

        find_val = (glat == glat[i])*(glon == glon[i] - grid_cell)
        ind.append(np.where(np.squeeze(find_val)))

        find_val = (glat == glat[i] + grid_cell)*(glon == glon[i] - grid_cell)
        ind.append(np.where(np.squeeze(find_val)))

        n = [np.size(i) for i in ind]
        n = sum(n)

        if n > 0:
            L[i,ind[0]] = 4./n;
            L[i,ind[1]] = 1./n;
            L[i,ind[2]] = 4./n;
            L[i,ind[3]] = 1./n;
            L[i,ind[4]] = 4./n;
            L[i,ind[5]] = 1./n;
            L[i,ind[6]] = 4./n;
            L[i,ind[7]] = 1./n;

    L = L - np.diag(np.sum(L,1));

    return L
