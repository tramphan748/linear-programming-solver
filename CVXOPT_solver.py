from cvxopt import matrix, solvers
import numpy as np

def input_matrix():
  # input matrix c
  print("Input matrix c: ")
  row_c = int(input("Enter the number of rows of matrix/vector c:"))
  print("Enter the entries in a single column (separated by space): ")
  c = list(map(float, input().split()))
  matrix_c = matrix(c, (row_c, 1)) # Directly create cvxopt matrix
  print(f'matrix c_T is:\n{matrix_c}\n')

  # input matrix G
  print("Input matrix G: ")
  row_G = int(input("Enter the number of rows of matrix G:"))
  col_G = int(input("Enter the number of columns of matrix G:"))
  print("Enter the entries in a single column (separated by space): ")
  G = list(map(float, input().split()))
  matrix_G = matrix(G, (row_G, col_G)) # Directly create cvxopt matrix
  print(f'matrix G is:\n{matrix_G}\n')

  # input matrix h
  print("Input matrix h: ")
  row_h = int(input("Enter the number of rows of matrix h:"))
  print("Enter the entries in a single column (separated by space): ")
  h = list(map(float, input().split()))
  matrix_h = matrix(h, (row_h, 1)) # Directly create cvxopt matrix
  print(f'matrix h is:\n{matrix_h}\n')

  return matrix_c, matrix_G, matrix_h

matrix_c, matrix_G, matrix_h = input_matrix()

def solver():
  show_progress = input("Do you want to show process? [Y/N] ")
  if show_progress == 'Y' or show_progress == "Yes" or show_progress == "YES" or show_progress == "yes" or show_progress == "y":
    solvers.options['show_progress'] = True
    solution = solvers.lp(matrix_c, matrix_G, matrix_h)
    print('Optimal solution:\n', solution['x'].T)
    print('Optimal value:\n',solution['primal objective'])
    print('Number of iterations:\n', solution['iterations'])
  else:
    solvers.options['show_progress'] = False
    solution = solvers.lp(matrix_c, matrix_G, matrix_h)
    print('Optimal solution:\n', solution['x'].T)
    print('Optimal value:\n', solution['primal objective'])
    print('Number of iterations:\n', solution['iterations'])
  return solution

result = solver()
print(result)
