import numpy as np

def initialGuess_H2_O2(phi, a_coef):

    if 0.6 <= phi <= 1.1:

        y1 = 7.42223223e-01
        y4 = 1.26023391e-01
        y5 = 2.90419341e-02
        y6 = 6.39074945e-02
        y7 = 1.29541193e-04
        y8 = 1.44878765e-05

    elif 0.1 <= phi < 0.6:

        y1 = 8.45652758e-01
        y4 = 1.68457092e-01
        y5 = 5.08241496e-02
        y6 = 2.82555795e-02
        y7 = 3.93636018e-04
        y8 = 2.97825404e-05

    elif 1.1 < phi <= 1.72:
        y1 = 5.55677761e-01
        y4 = 2.79079153e-02
        y5 = 2.23483254e-03
        y6 = 5.38865125e-02
        y7 = 4.96083266e-06
        y8 = 1.32659683e-06

    else:
        raise Exception("Equivalence Ratio out of bounds [0.1, 1.7]")

    A = np.array([[1,0],
                  [0,1]])

    B = np.array([[a_coef-0.5*y1-0.5*y4-0.5*y5-y7-y8],[1-y1-0.5*y4-0.5*y6-0.5*y7-y8]])

    X = np.linalg.solve(A, B)

    if (X[0] > 0 and X[1] > 0):
        return [y1, X.item(0), X.item(1), y4, y5, y6, y7, y8]
    else:
        raise Exception('No initial guess was found')

def initialGuess_CH4_O2(phi, a_coef):

    if 0.5 <= phi <= 1.1:

        y2 = 0.45482881
        y5 = 0.10688137
        y6 = 0.22909534
        y7 = 0.34347079
        y8 = 0.12105655

    elif 0.1 <= phi < 0.5:

        y2 = 0.89783866
        y5 = 0.11598922
        y6 = 0.02833698
        y7 = 0.32458843
        y8 = 0.01640948

    elif 1.1 < phi <= 1.72:

        y2 = 0.16115216
        y5 = 0.00310029
        y6 = 0.79200659
        y7 = 0.04470864
        y8 = 0.09035537

    else:
        raise Exception("Equivalence Ratio out of bounds [0.1, 1.7]")

    A = np.array([[1,0,0],
                  [0,1,0],
                  [0,0,1]])

    B = np.array([[2-y6-0.5*y7-0.5*y8],[a_coef-1.5-0.5*y2-0.5*y5+0.5*y6-0.25*y7+0.25*y8],[1-y2]])

    X = np.linalg.solve(A, B)

    if (X[0] > 0 and X[1] > 0 and X[2] > 0):
        return [X.item(0), y2, X.item(1), X.item(2), y5, y6, y7, y8]
    else:
        raise Exception('No initial guess was found')

def initialGuess_H2_Air(phi, a_coef):
# H2O CO2 NO O2 Ar
# y1  y10 y7 y2 y11

    y3  = 0.01120*2.8741411
    y4  = 0.00565*2.8741411
    y5  = 0.00025*2.8741411
    y6  = 0.00084*2.8741411
    y8  = 0.63932*2.8741411
    y9  = 0.00005*2.8741411

    A = np.array([[1, 0, 0, 0, 0],
                  [0, 1, 0, 0, 0],
                  [0, 0, 1, 0, 0],
                  [0, 0, 0, 1, 0],
                  [0, 0, 0, 0, 1]])
    
    B = np.array([[1-y3-0.5*y4-0.5*y6],
                  [-0.5-2.779*a_coef+0.5*y3-0.25*y4-0.5*y5+0.25*y6+y8+0.5*y9],
                  [7.46*a_coef-2*y8],
                  [0.04*a_coef],
                  [0.002*a_coef-y9]])
    
    X = np.linalg.solve(A,B)
    print(X)
    if (X[0] > 0 and X[1] > 0 and X[2] > 0 and X[3] > 0 and X[4] > 0):
        return [X.item(0), X.item(1), y3, y4, y5, y6, X.item(2), y8, y9, X.item(3), X.item(4)]
    else:
        raise Exception('No initial guess was found')

def initialGuess_CH4_Air(phi, a_coef):
# H2O CO2 NO O2 Ar
# y1  y10 y7 y2 y11

    y3  = 0.02666*9.226986
    y4  = 0.00021*9.226986
    y5  = 0.0001*9.226986
    y6  = 0.00021*9.226986
    y8  = 0.66859*9.226986
    y9  = 0.04514*9.226986

    A = np.array([[1, 0, 0, 0, 0],
                  [0, 1, 0, 0, 0],
                  [0, 0, 1, 0, 0],
                  [0, 0, 0, 1, 0],
                  [0, 0, 0, 0, 1]])
    
    B = np.array([[4-y3-0.5*y4-0.5*y6],
                  [-2.994-2.779*a_coef+0.5*y3-0.25*y4-0.5*y5+0.25*y6+y8+0.5*y9],
                  [7.46*a_coef-2*y8],
                  [0.04*a_coef],
                  [1+0.002*a_coef-y9]])
    
    X = np.linalg.solve(A,B)
    print(X)
    if (X[0] > 0 and X[1] > 0 and X[2] > 0 and X[3] > 0 and X[4] > 0):
        return [X.item(0), X.item(1), y3, y4, y5, y6, X.item(2), y8, y9, X.item(3), X.item(4)]
    else:
        raise Exception('No initial guess was found')


if __name__ == "__main__":
    phi = 1.2
    a_coef = (12+4*1) / (2*16+2*14*3.76+0.04*40+0.002*(12+2*16)) * 17.23852 / phi
    print(a_coef)
    asd = initialGuess_H2_Air(phi, a_coef)
    print(asd)