# Import packages
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter1d
from scipy.signal import find_peaks

# Define second gradient function
def second_gradient(r):
    dr = np.gradient(r)
    yy = gaussian_filter1d(np.gradient(dr),sigma=2)
    return yy

# Define smoothing function
def smooth(r):
    ys = gaussian_filter1d(r,sigma=2)
    return ys
    
# Define function to get x and y position of peaks
def peaks(r,y,h):
    p = find_peaks(y,height=h,distance=20) # The Numpy find peaks function gives the intensity of the peaks
    py = p[1]['peak_heights'] # Get the y value of peak position
    px = r[p[0]] # Get the x value of peak position
    return px,py

# Define function to import data
def dataimport(pathd,pathb): # Set path to the data file and background data file
    a = pd.read_csv(pathd,sep=',',names=['wave','ref']) # Read file of sample measurement
    b = pd.read_csv(pathb,sep=',',names=['bwave','bref']) # Read file of background measurement
    w = np.asarray(a.wave)
    r = np.asarray(a.ref)
    rb = np.asarray(b.bref)
    y = r-rb # Subtract background measurement
    ys = smooth(y) 
    yy = second_gradient(y) # Return second gradient of background subtracted reflectance
    return w,y,ys,yy

# Define raw plot
def rawplot(w,y,title,filename,draft=None): # title format: 'SAMPLEID Near Infrared Spectrum DATE', filename format: 'SAMPLEID_Near_Infrared_Spectrum_DATE.png'
    if draft:
        plt.scatter(w,y,c='Black',s=0.5) 
        plt.plot(w,y,c=cc,linewidth=0.5) 
        plt.xlim(np.min(w),np.max(w)) 
        plt.xlabel('Wavelength')
        plt.ylabel('Reflectance (Background Subtracted)')
        plt.title(title)
    else:
        plt.scatter(w,y,c='Black',s=0.5) 
        plt.plot(w,y,c=cc,linewidth=0.5) 
        plt.xlim(np.min(w),np.max(w)) 
        plt.xlabel('Wavelength')
        plt.ylabel('Reflectance (Background Subtracted)')
        plt.title(title)
        plt.savefig(filename)

# Define shape plot
def shapeplot(w,ys,title,filename,draft=None): # title format: 'SAMPLEID Near Infrared Spectrum DATE', filename format: 'SAMPLEID_Sh_Near_Infrared_Spectrum_DATE.png'
    if draft:
        plt.plot(w,ys,c='Black',linewidth=1) 
        plt.xlim(np.min(w),np.max(w))
        plt.xlabel('Wavelength')
        plt.ylabel('Reflectance (Background Subtracted)')
        plt.title(title)
    else:
        frame1 = plt.gca()
        plt.plot(w,ys,c='Black',linewidth=1) 
        plt.xlim(np.min(w),np.max(w))
        frame1.axes.get_yaxis().set_ticks([])
        plt.xlabel('Wavelength')
        plt.ylabel('Reflectance (Background Subtracted)')
        plt.title(title)
        plt.savefig(filename)

# Define 2nd gradient plot 
def gradplot(w,yy,h,ymin,ymax,title,filename,draft=None): # h is peak height, title format: 'SAMPLEID 2nd Gradient of Near Infrared Spectrum DATE, filename format: 'SAMPLEID_2G_Near_Infrared_DATE.png'
    if draft:
        px,py = peaks(w,yy,h)
        plt.plot(w,yy,c='Black',linewidth=1)
        plt.plot(px,py,"x")
        plt.xlim(np.min(w),np.max(w))
        plt.ylim(ymin,ymax)
        plt.xlabel('Wavelength')
        plt.ylabel('2nd Gradient of Reflectance')
        plt.title(title)
    else:
        px,py = peaks(w,yy,h)
        frame1 = plt.gca()
        plt.plot(w,yy,c='Black',linewidth=1)
        plt.plot(px,py,"x")
        for i,j in zip(px,py):
            if i == 1003:
                pass
            else:
                plt.annotate(np.round(i,decimals=1),xy=(i,j),xytext=(5,0),textcoords='offset points')
        plt.xlim(np.min(w),np.max(w))
        plt.ylim(ymin,ymax)
        frame1.axes.get_yaxis().set_ticks([])
        plt.xlabel('Wavelength')
        plt.ylabel('2nd Gradient of Reflectance')
        plt.title(title)
        plt.savefig(filename)

# Set plot parameters
plt.rcParams['font.sans-serif'] = 'Noto Sans' # Set font
plt.rcParams['font.size'] = 9 # Set font size
plt.rcParams['figure.facecolor'] = 'White' # Set background colour
plt.rcParams['figure.dpi'] = 600 # Set figure resolution as DPI
