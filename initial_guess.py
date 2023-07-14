###############################################################################################
# Este script:

# -> Dá uma estimativa inicial razoável para a composição de equilibrio inicial
#    para iniciar o algoritmo
#
#
# H2 + a_coef O2 ---> n1 H2O + n2 O2 + n3 H2 + n4 OH + n5 O + n6 H + n7 HO2 + n8 H2O2
#
# H: 2 n1 + 2 n3 + n4 + n6 + n7 + 2 n8 = 2
# O: n1 + 2 n2 + n4 + n5 + 2 n7 + 2 n8 = a_coef
#
###############################################################################################

import numpy as np


def initialGuess(model, a_coef):
    """
    This function solves the mass balance to give an initial estimate of the mol number (y)
    Some y_i variables must remain as free parameters. The number of free variables is the
    number of elements (j)

    A explicação está na secção 3.7 da dissertação
    
    """

    A = np.array([[0,2],[2,0]])

    if model == 1:
        y1 = 0.5
        y4 = 0.01
        B = np.array([[2-2*y1-y4],[2*a_coef-y1-y4]])
        X = np.linalg.solve(A, B)
        if (X[0] > 0 and X[1] > 0):
            return [y1, X.item(0), X.item(1), y4]
        else:
            raise Exception('No initial guess was found')

    elif model == 2:
        y1 = 0.5
        y4 = 0.01
        y5 = 0.01
        y6 = 0.01
        B = np.array([[2-2*y1-y4-y6],[2*a_coef-y1-y4-y5]])
        X = np.linalg.solve(A, B)
        if (X[0] > 0 and X[1] > 0):
            return [y1, X.item(0), X.item(1), y4, y5, y6]
        else:
            raise Exception('No initial guess was found')

    elif model == 3:
        y1 = 0.5
        y4 = 0.01
        y5 = 0.01
        y6 = 0.01
        y7 = 0.01
        y8 = 0.01
        B = np.array([[2-2*y1-y4-y6-y7-2*y8],[2*a_coef-y1-y4-y5-2*y7-2*y8]])
        X = np.linalg.solve(A, B)
        if (X[0] > 0 and X[1] > 0):
            return [y1, X.item(0), X.item(1), y4, y5, y6, y7, y8] 
        else:
            raise Exception('No initial guess was found')
                
    else:
        raise Exception('Invalid model number')

def initialGuess2(a_coef):
    """
    This function solves the mass balance to give an initial estimate of the mol number (y)
    Some y_i variables must remain as free parameters. The number of free variables is the
    number of elements (j)

    A explicação está na secção 3.7 da dissertação
    
    """

    A = np.array([[1,0,0],[0,1,0],[0,0,1]])

    if (a_coef >= 2.0):
        y2 = 0.46471903
        y5 = 0.11298964
        y6 = 0.23910202
        y7 = 0.3065884
        y8 = 0.14415641
        B = np.array([[2-y6-0.5*y7-0.5*y8],[a_coef-1.5-0.5*y2-0.5*y5+0.5*y6-0.25*y7+0.25*y8],[1-y2]])
        X = np.linalg.solve(A, B)
        if (X[0] > 0 and X[1] > 0 and X[2] > 0):
            return [X.item(0), y2, X.item(1), X.item(2), y5, y6, y7, y8]
        else:
            raise Exception('No initial guess was found')
    else:
        y2 = 0.46471903
        y3 = 0.28694797
        y5 = 0.11298964
        y7 = 0.3065884
        y8 = 0.14415641
        B = np.array([[2*a_coef-1-y2-2*y3-y5-y7],[1-y2],[3-2*a_coef+y2+2*y3+y5+0.5*y7-0.5*y8]])
        X = np.linalg.solve(A, B)
        if (X[0] > 0 and X[1] > 0 and X[2] > 0):
            return [X.item(0), y2, y3, X.item(1), y5, X.item(2), y7, y8]
        else:
            raise Exception('No initial guess was found')        

if __name__ == '__main__':
    asd = initialGuess(3, 0.5)
    print(asd)