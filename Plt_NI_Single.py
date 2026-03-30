# Import packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter1d
from scipy.signal import find_peaks
plt.rcParams['figure.dpi'] = 600

# Define second gradient function
def second_gradient(y):
    dy = np.gradient(y)
    yy = gaussian_filter1d(-np.gradient(dy),sigma=2)
    return yy

# Define smoothing function
def smooth(y):
    ys = gaussian_filter1d(y,sigma=2)
    return ys

# Define function to get x and y position of peaks 
def peaks(w,y,h):
    p = find_peaks(y,height=h,distance=20)
    ph = p[1]['peak_heights']
    pp = w[p[0]]
    return pp,ph

# Import data and define variables
a = pd.read_csv('FILE',sep=',',names=['wave','ref'])
b = pd.read_csv('FILE',sep=',',names=['bwave','bref'])
w = np.asarray(a.wave)
r = np.asarray(a.ref)
rb = np.asarray(b.bref)
y = r-rb
ys = smooth(y)
yy = second_gradient(y)

# Raw plot
ss = 0.5 
cc = 'Black' 
plt.scatter(w,y,c=cc,s=ss) 
plt.plot(w,y,c=cc,linewidth=ss) 
plt.xlim(np.min(w),np.max(w)) 
plt.xlabel('Wavelength')
plt.ylabel('Reflectance (Background Subtracted)')
plt.title('SAMPLEID Near Infrared Spectrum DATE')
# plt.savefig('SAMPLEID_Near_Infrared_Spectrum_DATE.png')

# Shape plot
frame1 = plt.gca()
plt.plot(w,ys,c='Black',linewidth=1) 
plt.xlim(np.min(w),np.max(w))
frame1.axes.get_yaxis().set_ticks([])
plt.xlabel('Wavelength')
plt.ylabel('Reflectance (Background Subtracted, \nGaussian Filtered $\\sigma$=2)')
plt.title('AMPLEID Near Infrared Spectrum DATE')
# plt.savefig('SAMPLEID_Sh_Near_Infrared_Spectrum_DATE.png')

# 2nd gradient plot 
# pp,ph = peaks(w,yy,10) # Choose height based on plot
frame2 = plt.gca()
plt.plot(w,yy,c='Black',linewidth=1)
# plt.plot(pp,ph,"x")
# for i,j in zip(pp,ph):
    # plt.annotate(np.round(i,decimals=1),xy=(i,j),xytext=(5,0),textcoords='offset points')
plt.xlim(np.min(w),np.max(w))
# plt.ylim(,) # Choose based on plot
# frame2.axes.get_yaxis().set_ticks([])
plt.xlabel('Wavelength')
plt.ylabel('2nd Gradient of Reflectance (Background \nSubtracted & Gaussian Filtered $\\sigma$=5)')
plt.title('SAMPLEID 2nd Gradient of Near Infrared Spectrum DATE')
# plt.savefig('SAMPLEID_2G_Near_Infrared_DATE.png')