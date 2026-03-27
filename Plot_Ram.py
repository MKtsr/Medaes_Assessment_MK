import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter1d
plt.rcParams['figure.dpi'] = 600

def gauss_sub(i):
    g = gaussian_filter1d(i,sigma=50)
    isub = i-g
    y = gaussian_filter1d(isub,sigma=2)
    return y

def second_gradient(i):
    di = np.gradient(i)
    y = gaussian_filter1d(-np.gradient(di),sigma=2)
    return y

# Remember to delete one of the tab spaces in header
a = np.genfromtxt('FILE.txt',delimiter='\t')
r = a[:-50,0]
i = a[:-50,1]
y = gaussian_filter1d(i,sigma=50)
yy = second_gradient(i)

# Raw Plot
ss = 0.5
cc = 'Black'
plt.scatter(r,i,c=cc,s=ss) 
plt.plot(r,i,c=cc,linewidth=ss) 
plt.xlim(np.min(r),np.max(r))
plt.xlabel('Raman Shift (cm-1)')
plt.ylabel('Intensity')
plt.title('SAMPLEID Raman Spectrum DATE')
plt.savefig('SAMPLEID_MapAvr_Raman_Spectrum_DATE.png')

# Gaussian Subtracted Plot
frame1 = plt.gca()
plt.plot(r,y,c='Black',linewidth=1)
plt.xlim(np.min(r),np.max(r))
frame1.axes.get_yaxis().set_ticks([])
plt.xlabel('Raman Shift (cm-1)')
plt.ylabel('Intensity (Gaussian Filter $\\sigma$=2, \nGaussian Filter $\\sigma$=50 Subtracted)')
plt.title('SAMPLEID Gaussian Subtracted Raman Spectrum DATE')
plt.savefig('SAMPLEID_GS_MapAvr_Raman_Spectrum_DATE.png')

# 2nd Gradient Plot
frame2 = plt.gca()
plt.plot(r,yy,c='Black',linewidth=1) 
plt.xlim(np.min(r),np.max(r))
frame2.axes.get_yaxis().set_ticks([])
plt.xlabel('Raman Shift (cm-1)')
plt.ylabel('Inverse 2nd Gradient of Intensity \n(Gaussian Filtered $\\sigma$=2)')
plt.title('SAMPLEID 2nd Gradient of Raman Spectrum DATE')
plt.savefig('SAMPLEID_2G_MapAvr_Raman_Spectrum_DATE.png')
