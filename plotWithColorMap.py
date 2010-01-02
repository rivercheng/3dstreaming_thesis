import matplotlib.pyplot as plt
import numpy as np
import Image

# Make plot with vertical (default) colorbar
buddha = Image.open('./buddha_heatmap.png')
fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.imshow(buddha, origin='lower', interpolation='nearest')
ax.set_axis_off()
ax.set_title('Number of Views for Faces (Happy Buddha)', size = 'x-large')

#ax2 = fig.add_subplot(122)
#cax = ax2.imshow(buddha_b, origin='lower', interpolation='nearest')
#ax2.set_axis_off()
#ax2.set_title('Happy Buddha Back')

# Add colorbar, make sure to specify tick locations to match desired ticklabels
ticks = []
labels = []
step = 255 / 0.61712  #maximum percentage for buddha is 0.61712
for i in range(13):
    ticks.append(i*0.05*step)
    labels.append(str(5 * i)+"%")

cbar = fig.colorbar(cax, ticks = ticks)
cbar.ax.set_yticklabels(labels)# vertically oriented colorbar
plt.savefig("heatmap_buddha.png")

# Make plot with vertical (default) colorbar
dragon = Image.open('./dragon_heatmap.png')
fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.imshow(dragon, origin='lower', interpolation='nearest')
ax.set_axis_off()
ax.set_title('Number of Views for Faces (Dragon)', size = 'x-large')

#ax2 = fig.add_subplot(122)
#cax = ax2.imshow(buddha_b, origin='lower', interpolation='nearest')
#ax2.set_axis_off()
#ax2.set_title('Happy Buddha Back')

# Add colorbar, make sure to specify tick locations to match desired ticklabels
ticks = []
labels = []
step = 255 / 0.4425  #maximum percentage for dragon is 0.4425
for i in range(13):
    ticks.append(i*0.05*step)
    labels.append(str(5 * i)+"%")

cbar = fig.colorbar(cax, ticks = ticks)
cbar.ax.set_yticklabels(labels)# vertically oriented colorbar
plt.savefig("heatmap_dragon.png")

# Make plot with vertical (default) colorbar
thai = Image.open('./thai_heatmap.png')
fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.imshow(thai, origin='lower', interpolation='nearest')
ax.set_axis_off()
ax.set_title('Number of Views for Faces (Thai Statue)', size = 'x-large')

#ax2 = fig.add_subplot(122)
#cax = ax2.imshow(buddha_b, origin='lower', interpolation='nearest')
#ax2.set_axis_off()
#ax2.set_title('Happy Buddha Back')

# Add colorbar, make sure to specify tick locations to match desired ticklabels
ticks = []
labels = []
step = 255 / 0.31794  #maximum percentage for thai is 0.31794
for i in range(13):
    ticks.append(i*0.05*step)
    labels.append(str(5 * i)+"%")

cbar = fig.colorbar(cax, ticks = ticks)
cbar.ax.set_yticklabels(labels)# vertically oriented colorbar
plt.savefig("heatmap_thai.png")
