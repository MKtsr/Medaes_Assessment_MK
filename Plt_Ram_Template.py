# Import packages
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter1d
from scipy.signal import find_peaks

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
    px = p[1]['peak_heights']
    py = r[p[0]]
    return px,py

# Define function to import data
def dataimport(path)
    a = np.genfromtxt(path,delimiter='\t')
    r = a[:-50,0]
    i = a[:-50,1]
    y = gauss_sub(i)
    yy = second_gradient(i)

# Define function for raw plot 
def rawplot(r,i,title,filename,draft=None): # title format: 'SAMPLEID Raman Spectrum DATE', filename format: 'SAMPLEID_MapAvr_Raman_Spectrum_DATE.png'
    if draft:
        plt.scatter(r,i,c='Black',s=0.5) 
        plt.plot(r,i,c='Black',linewidth=0.5)
        plt.xlim(np.min(r),np.max(r))
        plt.xlabel('Raman Shift (cm-1)')
        plt.ylabel('Intensity')
        plt.title(title)        
    else:
        plt.scatter(r,i,c='Black',s=0.5) 
        plt.plot(r,i,c='Black',linewidth=0.5)
        plt.xlim(np.min(r),np.max(r))
        plt.xlabel('Raman Shift (cm-1)')
        plt.ylabel('Intensity')
        plt.title(title)
        plt.savefig(filename)

# Define gaussian subtracted plot
def gaussplot(r,y,h,ymin,ymax,title,filename,draft=None): # h is peak height, title format: 'SAMPLEID Gaussian Subtracted Raman Spectrum DATE', filename format: 'SAMPLEID_GS_MapAvr_Raman_Spectrum_DATE.png'
    if draft:
        pgx,pgy = peaks(r,y,h)
        plt.plot(r,y,c='Black',linewidth=1)
        plt.plot(pgx,pgy,"x")
        plt.xlim(np.min(r),np.max(r))
        plt.ylim(ymin,ymax) 
        plt.xlabel('Raman Shift (cm-1)')
        plt.ylabel('Intensity (Gaussian Filter Subtracted)')
        plt.title(title)     
    else:
        pgx,pgy = peaks(r,y,h)
        frame1 = plt.gca()
        plt.plot(r,y,c='Black',linewidth=1)
        plt.plot(pgx,pgy,"x")
        for i,j in zip(pgx,pgy):
            plt.annotate(np.round(,decimals=1),xy=(i,j),xytext=(-10,5),textcoords='offset points')
        plt.xlim(np.min(r),np.max(r))
        plt.ylim(ymin,ymax)
        frame1.axes.get_yaxis().set_ticks([])
        plt.xlabel('Raman Shift (cm-1)')
        plt.ylabel('Intensity (Gaussian Filter Subtracted)')
        plt.title(title)
        plt.savefig(filename)

# Define 2nd gradient plot
def gradplot(r,yy,h,ymin,ymax,title,filename,draft=None): # h is peak height, title format: 'SAMPLEID 2nd Gradient of Raman Spectrum DATE', filename format: 'SAMPLEID_2G_MapAvr_Raman_Spectrum_DATE.png'
    if draft:
        p2x,p2y = peaks(r,yy,h)
        plt.plot(r,yy,c='Black',linewidth=1)
        plt.plot(p2x,p2y,"x")
        plt.xlim(np.min(r),np.max(r))
        plt.ylim(ymin,ymax)
        plt.xlabel('Raman Shift (cm-1)')
        plt.ylabel('Inverse 2nd Gradient of Intensity')
        plt.title(title)
    else:
        p2x,p2y = peaks(r,yy,h)
        frame1 = plt.gca()
        plt.plot(r,yy,c='Black',linewidth=1)
        plt.plot(p2x,p2y,"x")
        for k,l in zip(p2x,p2y):
            plt.annotate(np.round(k,decimals=1),xy=(k,l),xytext=(-10,5),textcoords='offset points')
        plt.xlim(np.min(r),np.max(r))
        plt.ylim(ymin,ymax)
        frame1.axes.get_yaxis().set_ticks([])
        plt.xlabel('Raman Shift (cm-1)')
        plt.ylabel('Inverse 2nd Gradient of Intensity')
        plt.title(title)
        plt.savefig(filename)

# Set plot parameters
plt.rcParams['font.sans-serif'] = 'Noto Sans' # Set font
plt.rcParams['font.size'] = 9 # Set font size
plt.rcParams['figure.facecolor'] = 'White' # Set background colour
plt.rcParams['figure.dpi'] = 600 # Set figure resolution as DPI
