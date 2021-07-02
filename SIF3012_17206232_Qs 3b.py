#QS 3b

import numpy as np

#matrix
a = np.array([[1.5, 0, 1], 
              [-0.5, 0.5, -0.5],
              [-0.5, 0, 0]])

#initial eigenvector approximation
x = np.array([1, 1, 1])

tolerance = 0.01
max_iteration = 5 #can be adjusted accordingly

#power method

lambda_old = 1.0
condition =  True
step = 1

while condition:
    # Multiplying a and x
    x = np.dot(a,x)
    
    # Finding eigenvalues and eigenvectors
    lambda_new = max(abs(x))
    
    x = x/lambda_new
    
    # Displaying eigenvalue and eigenvectors
    print('Step', (step))
    print('')
    print('Eigenvalue =' ,(lambda_new))
    print('Eigenvectors = ')
    for i in range(3):
        print((x[i]))

    # Checking maximum iteration
    step = step + 1
    if step > max_iteration :
        break

    # Calculating error
    error = abs(lambda_new - lambda_old)
    print('error =', (error))
    print('')
    lambda_old = lambda_new
    condition = error > tolerance
    