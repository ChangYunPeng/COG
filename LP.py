import numpy as np
from scipy.optimize import linprog

# We construct our A matrix by creating two 3-way tensors,
# and then reshaping and concatenating them
A_r = np.zeros((l, l, l))
A_t = np.zeros((l, l, l))

for i in range(l):
	for j in range(l):
		A_r[i, i, j] = 1
		A_t[i, j, i] = 1

A = np.concatenate((A_r.reshape((l, l**2)), A_t.reshape((l, l**2))), axis=0)
b = np.concatenate((P_r, P_t), axis=0)
c = D.reshape((l**2))

opt_res = linprog(c, A_eq=A, b_eq=b)
emd = opt_res.fun
gamma = opt_res.x.reshape((l, l))