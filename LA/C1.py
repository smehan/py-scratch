# Copyright shawn dot mehan at shawn mehan dot com
#
# -*- : utf-8 -*-

from plotting import plot
import matplotlib.pyplot as plt

# define a picture in the complex plane
S = {2+2j, 3+2j, 1.75+1j, 2+1j, 2.25+1j, 2.5+1j, 2.75+1j, 3+1j, 3.25+1j}

# plotting.plot only writes a file if one debugs the plot method!
plot(S, 4)

#fig,ax = plt.subplots()
#ax.scatter([i.real for i in S], [j.imag for j in S])
plt.plot([i.real for i in S], [j.imag for j in S], 'ro')
plt.axis([-4,4,-4,4])
plt.grid(True)
plt.show()

# now translate picture z_0 by z
St = {1 + 2j + z for z in S}
plt.plot([i.real for i in St], [j.imag for j in St], 'ro')
plt.axis([-8,8,-8,8])
plt.grid(True)
plt.show()

# and now scale picture by s
Ss = {0.5 * z for z in S}
plt.plot([i.real for i in Ss], [j.imag for j in Ss], 'ro')
plt.axis([-4,4,-4,4])
plt.grid(True)
plt.show()

# and now rotate by i, scale by 1/2
Sr = {0.5j * z for z in S}
plt.plot([i.real for i in Sr], [j.imag for j in Sr], 'ro')
plt.axis([-4,4,-4,4])
plt.grid(True)
plt.show()

plot(Sr, 4)
