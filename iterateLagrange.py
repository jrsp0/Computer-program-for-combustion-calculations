###############################################################################################
# 
# -> Este script faz as iterações para o problema de equilibrio quimico da minimização da energia
#    livre de Gibbs até que a tolerância de erro seja satisfeita ou o número max de 
#    iterações seja alcançado
#
###############################################################################################


from solveLagrange import solveLagrange
import numpy as np
from lambdacorrection import lambdacorr

def iterateLagrange(pressure,g_RT,i,j,a,b,y,max_it):

    index_smart_range = 0

    it_num     = 0

    # print("y que entra no iterateLagrange:\n")
    # print(y)

    while it_num <= max_it:
        # print(f"it_num {it_num}")
        # Resolver o sistema de equações:

        y, x, delta, y_bar, x_bar, delta_bar = solveLagrange(pressure,j,a,b,g_RT,y)

        # print(f"x depois de solveLagrange {x}")
        # Verificar se todos os nº d emol os elementos são positivos
        # Se não forem chamar lambdacorr para corrigir
        
        if not all(i > 0 for i in x):
        # if not np.all(x > 0):
            # start = time.time()
            y, x, delta, y_bar, x_bar, delta_bar, index_smart_range = lambdacorr(pressure, i, g_RT, y, x, delta, y_bar, x_bar, delta_bar, index_smart_range)
        
            # end = time.time()
            # print(end - start)
            # print("x depois de lambdacorr\n")
            # print(x)
        # Verificar se a tolerância de erro é satisfeita (delta = x - y)
        # Se não é, então y = x e repetir os cáculos com o novo y
        # print(index_smart_range)
        # if np.all(abs(delta) < 10e-4):
        if np.all(np.absolute(delta) < 10e-4):
            return x
        else:
            y = x
            it_num += 1

if __name__ == '__main__':
    pressure = 10
    j        = 2
    a_coef   = 0.5
    i        = 8
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
    y        = np.array([0.5, 0.175, 0.43, 0.01, 0.1, 0.1, 0.01, 0.01])
    g_RT     = np.array([-39.09426432585993, -30.28623343919619, -20.84439788297744,
                         -25.72272378153731,-12.964098024733945, -8.577989536426179,
                         -34.51842668594744, -43.28208448687616])
    
    sol = iterateLagrange(pressure, g_RT, i, j, a, b, y, 50)

    print(sol)