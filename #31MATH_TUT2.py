#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Create Labels for a Plot

import matplotlib.pyplot as plt
import numpy as np

x = np.array([0, 1, 2, 3, 4])
y = np.array([2, 4, 6, 8, 10])

plt.plot(x, y)

plt.xlabel("x-axis")
plt.ylabel("y-axis")

plt.show()


# In[3]:


#using title

import matplotlib.pyplot as plt # importing a library
import numpy as np

x = np.array([0, 1, 2, 3, 4])
y = np.array([2, 4, 6, 8, 10])

plt.plot(x, y)

plt.title('plots')
plt.xlabel("x-axis")
plt.ylabel("y-axis")

plt.show()


# In[1]:


#Font Properties for Title and Labels

#We can use the fontdict parameter in xlabel(), ylabel(), and title() to set font properties.

import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

#f1 = {'family':'serif','color':'green','size':30}
#f2 = {'family':'serif','color':'darkred','size':20}

f1 = {'color':'green','size':30}
f2 = {'color':'darkred','size':20}

plt.title("plot", fontdict = f1)
plt.xlabel("x-axis", fontdict = f2)
plt.ylabel("y-axis", fontdict = f2)

plt.plot(x, y)
plt.show()


# In[6]:


#Position the Title

#we can use the loc parameter in title() to position the title.

#Legal values are: 'left', 'right', and 'center'. Default value is 'center'.

import matplotlib.pyplot as plt
import numpy as np

x = np.array([0, 1, 2, 3, 4])
y = np.array([2, 4, 6, 8, 10])

plt.plot(x, y)

plt.title('plots',loc='left')
plt.xlabel("x-axis")
plt.ylabel("y-axis")

plt.show()


# In[7]:


#add Grid lines to the plot

import matplotlib.pyplot as plt
import numpy as np

x = np.array([0, 1, 2, 3, 4])
y = np.array([2, 4, 6, 8, 10])

plt.plot(x, y)

plt.title('plots',loc='left')
plt.xlabel("x-axis")
plt.ylabel("y-axis")

plt.grid()

plt.show()


# In[9]:


# we can show ONLY 1 axis grid at a time

import matplotlib.pyplot as plt
import numpy as np

x = np.array([0, 1, 2, 3, 4])
y = np.array([2, 4, 6, 8, 10])

plt.plot(x, y)

plt.title('plots',loc='left')
plt.xlabel("x-axis")
plt.ylabel("y-axis")

#plt.grid(axis='x')
plt.grid(axis='y')

plt.show()


# In[14]:


#we can add color, linesize, line width for grid as well.

import matplotlib.pyplot as plt
import numpy as np

x = np.array([0, 1, 2, 3, 4])
y = np.array([2, 4, 6, 8, 10])

plt.plot(x, y)

plt.title('plots',loc='left')
plt.xlabel("x-axis")
plt.ylabel("y-axis")

plt.grid(color='g',ls='-.',lw='1.5')

plt.show()


# In[15]:


#mutiple plots --> subplot()

import matplotlib.pyplot as plt
import numpy as np

#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([2, 4, 6, 8])

plt.subplot(1, 2, 1) # 1 row 2 colums
plt.plot(x,y)

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([3, 5, 7, 9])

plt.subplot(1, 2, 2)
plt.plot(x,y)

plt.show()


# In[3]:


#mutiple plots --> subplot()

import matplotlib.pyplot as plt
import numpy as np

#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([2, 4, 6, 8])

plt.subplot(2, 1, 1)
plt.plot(x,y)

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([3, 5, 7, 9])

plt.subplot(2, 1,2)
plt.plot(x,y)

plt.show()


# In[17]:


#we can draw mutiple plots in plot

import matplotlib.pyplot as plt
import numpy as np

x = np.array([0, 1, 2, 3])
y = np.array([2, 4, 5, 7])

plt.subplot(2, 3, 1)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([3, 5, 7, 9])

plt.subplot(2, 3, 2)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([2, 7, 8, 10])

plt.subplot(2, 3, 3)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([7, 5, 9, 10])

plt.subplot(2, 3, 4)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 5)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([7, 9, 1, 5])

plt.subplot(2, 3, 6)
plt.plot(x,y)

plt.show()


# In[19]:


import matplotlib.pyplot as plt
import numpy as np

#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([2, 4, 6, 8])

plt.subplot(1, 2, 1)
plt.plot(x,y)
plt.title('plot1')

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([3, 5, 7, 9])

plt.subplot(1, 2, 2)
plt.plot(x,y)
plt.title('plot2')

plt.show()


# In[20]:


#suptitle is used for main title

import matplotlib.pyplot as plt
import numpy as np

#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([2, 4, 6, 8])

plt.subplot(1, 2, 1)
plt.plot(x,y)
plt.title('plot1')

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([3, 5, 7, 9])

plt.subplot(1, 2, 2)
plt.plot(x,y)
plt.title('plot2')

plt.suptitle('plots')
plt.show()


# In[ ]:




