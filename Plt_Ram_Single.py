# Import packages and set plot parameters
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter1d
from scipy.signal import find_peaks
plt.rcParams['figure.dpi'] = 600

# Define gaussian filter subtraction and smoothing function
def gauss_sub(i):
    g = gaussian_filter1d(i,sigma=50)
    isub = i-g
    y = gaussian_filter1d(isub,sigma=2)
    return y

# Define second gradient function
def second_gradient(i):
    di = np.gradient(i)
    y = gaussian_filter1d(-np.gradient(di),sigma=2)
    return y
    
# Define function to get x and y position of peaks
def peaks(r,y,h):
    p = find_peaks(y,height=h,distance=20)
    ph = p[1]['peak_heights']
    pp = r[p[0]]
    return pp,ph

# Import data, remember to delete one of the tab spaces in header
a = np.genfromtxt('FILE.txt',delimiter='\t')
r = a[:-50,0]
i = a[:-50,1]
y = gauss_sub(i)
yy = second_gradient(i)

# Raw Plot 
plt.scatter(r,i,c='Black',s=0.5) 
plt.plot(r,i,c='Black',linewidth=0.5)
plt.xlim(np.min(r),np.max(r))
plt.xlabel('Raman Shift (cm-1)')
plt.ylabel('Intensity')
plt.title('SAMPLEID Raman Spectrum DATE')
# plt.savefig('SAMPLEID_MapAvr_Raman_Spectrum_DATE.png')

# Gaussian subtracted plot
# pgp,pgh = peaks(r,y,10) # Choose height based on plot
frame1 = plt.gca()
plt.plot(r,y,c='Black',linewidth=1)
# plt.plot(pgp,pgh,"x")
# for i,j in zip(pgp,pgh):
    # plt.annotate(np.round(r,decimals=1),xy=(i,j),xytext=(-10,5),textcoords='offset points')
plt.xlim(np.min(r),np.max(r))
# plt.ylim(0,50) # Choose based on plot
# frame1.axes.get_yaxis().set_ticks([])
plt.xlabel('Raman Shift (cm-1)')
plt.ylabel('Intensity (Gaussian Filter $\\sigma$=2, \nGaussian Filter $\\sigma$=50 Subtracted)')
plt.title('SAMPLEID Gaussian Subtracted Raman Spectrum DATE')
# plt.savefig('SAMPLEID_GS_MapAvr_Raman_Spectrum_DATE.png')

# 2nd gradient plot
# p2p,p2h = peaks(r,yy,10) # Choose height based on plot
frame2 = plt.gca()
plt.plot(r,yy,c='Black',linewidth=1)
# plt.plot(p2p,p2h,"x")
# for k,l in zip(p2p,p2h):
    # plt.annotate(np.round(k,decimals=1),xy=(k,l),xytext=(-10,5),textcoords='offset points')
plt.xlim(np.min(r),np.max(r))
# plt.ylim(0,10) # Choose based on plot
# frame2.axes.get_yaxis().set_ticks([])
plt.xlabel('Raman Shift (cm-1)')
plt.ylabel('Inverse 2nd Gradient of Intensity \n(Gaussian Filtered $\\sigma$=2)')
plt.title('SAMPLEID 2nd Gradient of Raman Spectrum DATE')
# plt.savefig('SAMPLEID_2G_MapAvr_Raman_Spectrum_DATE.png')
