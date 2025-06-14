import cv2
import numpy as np
import matplotlib.pyplot as plt

def save_video_from_images(filename, images, fps):
    _image = images[0]
    image_shape = {'height': _image.shape[0],
                   'width': _image.shape[1],
                   'layers': _image.shape[2]}

    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    video = cv2.VideoWriter(filename, fourcc, fps,
                            (image_shape['width'], image_shape['height']))
    for image in images:
        video.write(image)
    video.release()

def moving_average(array, moving_window):
    N = len(array)
    try :
        array  = np.array(array, dtype=np.float64)
    except:
        print(type(array),"-----------------",array)
    moving_avg = np.empty(N)
    for t in range(N):
        moving_avg[t] = np.mean(array[max(0, t-moving_window):(t+1)])
    return moving_avg
    
def save_episode_plot(x_array, y_array, moving_window, xlabel, ylabel, vertical_line, filename):
    plt.rcParams.update({'font.size': 14})
    fig = plt.figure()
    running_avg = moving_average(array=y_array, moving_window=moving_window)
    
    plt.plot(x_array, running_avg)
    plt.xlabel(f"{xlabel}",fontsize=14)
    plt.ylabel(f"{ylabel} Moving Average (n={moving_window})",fontsize=14)
    
    if vertical_line != None:
        plt.axvline(x=int(vertical_line), color='g')
        plt.legend([f'{ylabel}','model saved'])
    else:
        plt.legend([f'{ylabel}'])

    #plt.legend(fontsize=14) 
    #plt.savefig(filename)
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    plt.close(fig)
    
