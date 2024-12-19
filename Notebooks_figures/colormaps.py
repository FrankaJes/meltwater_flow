import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.colors
import cmocean as cmo

# IMAU-ICE variables

# BMB colormap and normalization
vmax = 100
vmin = -10
linthresh = 0.3
linscale = 0.25
fracpos = (np.log10(vmax / linthresh) + linscale) / (np.log10(vmax / linthresh) + np.log10(-(vmin / linthresh)) + 2 * linscale)
nneg = int((1 - fracpos) * 256)
colors1 = plt.get_cmap('cmo.ice_r')(np.linspace(0, 1.0, nneg + 1))
colors2 = plt.get_cmap('inferno')(np.linspace(0.0, 1, 256 - nneg - 1))
colors = np.vstack((colors1, colors2))
cmap_BMB = mpl.colors.LinearSegmentedColormap.from_list('my_colormap', colors)
norm_BMB = mpl.colors.SymLogNorm(linthresh, vmin=vmin, vmax=vmax, linscale=linscale)

# Hi colormap and normalization
cmap_Hi = plt.get_cmap('gist_stern')
norm_Hi = mpl.colors.Normalize(vmin=0, vmax=700)

# Hs colormap and normalization
cmap_Hs = plt.get_cmap('Blues')
norm_Hs = mpl.colors.Normalize(vmin=0, vmax=300)

# Hb colormap and normalization
cmap_Hb = plt.get_cmap('cmo.dense')
norm_Hb = mpl.colors.Normalize(vmin=-800, vmax=0)

# u_surf colormap and normalization
cmap_u_surf = plt.get_cmap('turbo')
norm_u_surf = mpl.colors.Normalize(vmin=0, vmax=2000)

# mask grounded colormap and normalization
cmap_ground = mpl.colors.LinearSegmentedColormap.from_list("", ["gainsboro", (0.7019607843137254, 0.803921568627451, 0.8901960784313725, 1.0)])
norm_ground = mpl.colors.Normalize(vmin=3, vmax=4)

# mask ocean colormap and normalization
cmap_ocean = plt.get_cmap('Greys')
norm_ocean = mpl.colors.Normalize(vmin=0, vmax=1.7)

# mask GL colormap and normalization
cmap_GL = plt.get_cmap('Greens')
norm_GL = mpl.colors.Normalize(vmin=1, vmax=2)

# draft colormap and normalization
cmap_draft = 'cmo.deep_r'
norm_draft = mpl.colors.Normalize(vmin=-700, vmax=0)

# LADDIE vars
# u_lad colormap and normalization
cmap_u_lad = plt.get_cmap('Greens')
norm_u_lad = mpl.colors.Normalize(vmin=0, vmax=0.2)

# D colormap and normalization
cmap_D = plt.get_cmap('Blues')
norm_D = mpl.colors.Normalize(vmin=0, vmax=150)

# T colormap and normalization
cmap_T = plt.get_cmap('Reds')
norm_T = mpl.colors.Normalize(vmin=-2.5, vmax=-1)

# S colormap and normalization
cmap_S = plt.get_cmap('cmo.haline')
norm_S = mpl.colors.Normalize(vmin=33.8, vmax=34.2)