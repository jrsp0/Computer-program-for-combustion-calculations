###############################################################################################
# Este script:
#
# -> Resolve os sistema de equações (equação 3.27 da dissertação)
#    
###############################################################################################

import numpy as np
# from GaussianElimination import Gauss
import time

def solveLagrange(pressure,j,a,b,g_RT,y, info=False):

    """
    Variables:

    m       : number of elements
    n       : number of chemical species
    a_ij    : number of atoms of element j in species i
    b_j     : number of moles of element j on the reactants side
    x_i     : number of moles x of the species i
    y_i     : initial mol number

    """

    y_bar = sum(y)

    # Equação 3.18 da dissertação
    # ci = (g/RT)_i + ln(P)
    c = g_RT + np.log(pressure)

    # Equação 3.19 da dissertação
    # fi = y_i * [ci + ln(y_i/y_bar)]
    fi_y = y * (c + np.log(y / y_bar))


    # ========================== Sistema de Equações ========================== #

    # Número total de equações j + 1 = 2 + 1 = 3 equações

    # Duas primeiras equações do sistema de equações (da equação 3.27 da dissertação):
    # r_1j*pi_1 + r_2j*pi_2 + ... + r_jj*pi_j + b_j*u = sum_i[a_ij * fi(Y)]
    system = np.zeros((j+1,j+2))

    # Inserir os valores r_ij dados pela equação 3.26 da dissertação
    # rjk = rkj = sum_i(a_ij * a_ik) * y_i
    # for l in np.arange(j):
    #     for m in np.arange(j):
    #         system[m, l] = np.sum(a[:,m] * a[:,l] * y)
    system[:j, :j] = np.dot(a[:, :j].T * y, a[:, :j])

    # Última coluna, b_j*u:
    system[:j,j] = b

    # Soma sum_i[a_ij * fi(Y)] da equação 3.27
    system[:j,j+1] = np.sum(a.T*fi_y, axis=1)

    # Última equação do sistema de equações 3.27
    # b_1*pi_1 + b_2*pi_2 + ... + b_m*pi_m  = sum_i[fi(Y)]
    system[j,:j] = b
    system[j, j+1] = sum(fi_y)

    # O método de eliminação de Gauss é da forma A*X = B
    a_arr = system[:j+1,:j+1]
    # b_arr = system[:,3].reshape(3,1)
    b_arr = system[:, j+1:j+2]

    # Chamar GaussElimination.py e calcular a solução do sistema de equações (sol)
    # sol = Gauss(a_arr, b_arr, 3, 1)
    sol = np.linalg.solve(a_arr, b_arr)

    # pi_f = np.array([sol[0], sol[1]]).reshape(1,2)
    pi_f = np.array([sol[index] for index in range(0,j)]).reshape(1,j)

    # ============ Calculo de x_i para a iteração ============ #
    # Calcular x_bar da equação 3.28
    # u = -1. + (x_bar/y_bar); u é o terceiro elemento da solução (sol[2])
    x_bar = (sol[-1] + 1.0) * y_bar

    # Equação 3.23
    # x_i = -fi(Y) + (y_i/y_bar) * x_bar + [sum_j(pi_j * a_ij)] * y_i
    sum_pi_aij = np.sum(pi_f*a, axis=1)
    x = np.array(-fi_y + (y/y_bar)*x_bar + sum_pi_aij*y)

    # Cálculo de outras variáveis
    x_bar = sum(x)
    delta = x - y
    delta_bar = x_bar - y_bar

    return y, x, delta, y_bar, x_bar, delta_bar

if __name__ == '__main__':
    pressure = 10
    a_coef = 0.5
    j        = 2
    a        = np.array([[2,1],
                        [0,2],
                        [2,0],
                        [1,1],
                        [0,1],
                        [1,0],
                        [1,2],
                        [2,2]])
    b        = [2, 2*a_coef]
    g_RT = np.array([1,2,3,4,5,6,7,8])
    y = np.array([11,12,13,14,15,16,17,18])

    asd = solveLagrange(pressure,j,a,b,g_RT,y)

    print(asd[1])