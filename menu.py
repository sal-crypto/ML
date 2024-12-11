# import pandas as pd
# my_index =[ 'UAE' , 'UK ', 'USA','INDIA']
# pdata= [1234,4567,1999,2004]
# my_ser= pd.Series(data=pdata,index=my_index)
# print(my_ser['USA'])
# pd.Series( )
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 10, 100)
y = x ** 2
plt.plot(y, x ,'r')
plt.subplot( 1, 2, 1)
plt.show()