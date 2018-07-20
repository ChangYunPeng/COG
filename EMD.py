import numpy as np
from matplotlib import pyplot as plt
l = 10

P_r = np.array([12,7,4,1,19,14,9,6,3,2])
P_t = np.array([1,5,11,17,13,9,6,4,3,2])
P_r = P_r / np.sum(P_r)
P_t = P_t / np.sum(P_t)

plt.bar(range(l), P_r, 1, color='blue', alpha=1)
plt.axis('off')
plt.ylim(0, 0.5)
plt.savefig("discrete_p_r.svg")
print("P_r:")
plt.show()

plt.bar(range(l), P_t, 1, color='green', alpha=1)
plt.axis('off')
plt.ylim(0, 0.5)
plt.savefig("discrete_p_t.svg")
print("P_t:")
plt.show()