# coding: utf-8
import numpy as np
a =np.array([
 np.linspace(1, 3, 3),
 np.linspace(4, 6, 3),
 np.linspace(7, 9, 3)
])
print(a)
a[0:2, 1:]
a[, 1:]
a[:, 1:]
a[:2, 1:]
a
a[a % 2 == 0]
a[a % 2 == 1]
get_ipython().run_line_magic('pinfo', 'np.where')
np.where(a > 2)
a
arr = np.array([
 [1,2],
 [3,4],
 [5,6]
])
print(arr)
np.where(arr > 2)
zip(np.where(arr > 2))
np.array(zip(np.where(arr > 2)))
np.array(list(zip(np.where(arr > 2))))
np.where(arr >)[0]
np.where(arr >2)[0]
arr.tolist()
(2, 3) * 2
list((2, 3))
list((2, 3), (1,2))
np.array(np.where(a > 2))
list(np.where(a > 2))
np.array(np.where(a > 2)).tolist()
zip(np.array(np.where(a > 2)).tolist())
list(zip(np.array(np.where(a > 2)).tolist()))
list(zip(np.array(np.where(a > 2)).tolist()[0]))
np.array(np.where(a > 2))
np.array(np.where(a > 2)).tolist()
np.array(np.where(a > 2)).tolist()[0]
_a, _b = np.array(np.where(a > 2)).tolist()
_a, _b
list(zip(_a, _b))
arr
arr[arr > 2]
np.where(arr > 2)
list(zip(_a, _b))
arr[[1, 2]]
arr[[0, 2]]
arr[:, [0, 2]]
arr[:, [0, 1]]
arr[:, [0]]
arr[np.where(arr > 2)]
arr
arr ** 2
np.pow(arr, 1.2)
np.power(arr, 1.2)
np.exp(arr)
get_ipython().run_line_magic('pinfo', 'np.exp')
np.e
arr
4 ** 2
2 ** 4
2 ** arr
3 ** arr
arr.reshape(None)
arr.reshape((6))
3 ** arr.reshape((6))
v1 = np.arange(0, 5)
v1
v2 = np.arange(5, 10)
v2
v1 @ v2
np.sum(v1 * v2)
v1 * v2
A = np.array([[n+m*10 for n in range(5)] for m in range(5)])
A
A.T
A @ A
a
arr
a[:1]
a[:, :1]
a[:, :2]
a[:, :2] @ arr
a[:2]
a[:2] @ arr
A_mat = np.matrix(a[:2])
A_mat
A_mat * 2
A_mat * A_mat
A_mat * arr
A_mat.sum()
A.sum(axis=1)
A_mat.sum(axis=1)
A_mat.sum(axis=0)
# seems that reshapes hold the reference
A_mat
A_mat.reshape(3, 2)
B_mat = A_mat.reshape(3, 2)
B[0, :] = 2
B_mat[0, :] = 2

A_mat
