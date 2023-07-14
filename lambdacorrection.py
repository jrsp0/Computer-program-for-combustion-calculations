###############################################################################################
#
# -> Este script Aplica uma correção ao número de moles quanto este dá negativo
#
###############################################################################################

import numpy as np

# def dF_dlam(s, i, x, y, delta, c, x_bar, y_bar, delta_bar):
#     """
#     Equação 3.34 da dissertação
#       dF(lam)/dlam = sum_i delta_i[(g(T)/RT)_i + ln(P) +
#                                    ln(yi+lam*delta_i)/(y_bar+lam*delta_bar)]
#     """
#     return np.sum(delta[:i] * (c[:i] + np.log(y[:i] + s * delta[:i]) -
#                                np.log(y_bar + s * delta_bar)))

def fun(delta_slice, c_slice, y_slice, smart_range, y_bar, delta_bar):
    return sum(delta_slice * (c_slice + np.log(y_slice + smart_range * delta_slice) -
                        np.log(y_bar + smart_range * delta_bar)))


def lambdacorr(pressure, i, g_RT, y, x, delta, y_bar, x_bar, delta_bar, index_smart_range):
    '''
    Este módulo aplica o método de correção lambda . Quando os números moles de entrada são negativos,
    o código os corrige para valores positivos e passá-los para o próximo ciclo de iteração. Ele define um
    intervalo 'inteligente' para que possa explorar eficientemente os valores lambda de [0,1].
    Metade do intervalo é exponencial e a outra metade linear, totalizando 150 pontos. 
    O código recupera o último valor lambda antes do primeiro derivada torna-se positiva 
    (equação 3.e4) e corrige os números de moles negativos para positivos.

    '''

    # Ignorar NAN
    np.seterr(invalid='ignore')
    np.seterr(divide='ignore')

    # Equação 3.17
    # c_i = (g/RT)i + ln(P)
    c = g_RT + np.log(pressure)

    # Criar um intervalo de valores lambda para explorar. Para acelerar a localização do 
    # valor lambda correto a ser usado, o intervalo é dividido em duas partes em range_split:
    # o intervalo exponencial inferior e o intervalo linear superior. Isso ajuda o sistema a 
    # convergir mais rapidamente.
    range_split = 0.5

    # ======================= Intervalo exponencial =======================
    lower = -25

    # Numero de passos
    steps = 25

    # Intervalo exponencial
    low_range = np.exp(np.linspace(lower, 0, steps+1))

    # ======================= Intervalo linear =======================
    high_step = 0.1
    high_range = np.arange(0.5, 1 + high_step, high_step)



    # Combinar os dois intervalos
    smart_range = np.append(low_range[low_range <= range_split], high_range)
    # print(smart_range)
    # print("_---------------------------------------------_")

    # Variavel booleana para verificar
    lam_not_found = True

    # explorar o intervalo
    
    delta_slice = delta[:i]
    c_slice = c[:i]
    y_slice = y[:i]

    if index_smart_range == 0:
        for i in range(0, len(smart_range)):
            # val = sum(delta_slice * (c_slice + np.log(y_slice + smart_range[i] * delta_slice) -
            #             np.log(y_bar + smart_range[i] * delta_bar)))
            val = fun(delta_slice, c_slice, y_slice, smart_range[i], y_bar, delta_bar)

            # Verificar se o valor da equação 3.24
            if val > 0 or np.isnan(val):
                break

            # Se lambda for encontrado então:
            index_smart_range = i
            lam = val
            lam_not_found = False

    
    if index_smart_range != 0:
        for i in range(index_smart_range, len(smart_range)):
            val = fun(delta_slice, c_slice, y_slice, smart_range[i], y_bar, delta_bar)
        
            # Verificar se o valor da equação 3.24
            if val > 0 or np.isnan(val):
                break

            # Se lambda for encontrado então:
            index_smart_range = i
            lam = smart_range[i]
            lam_not_found = False       

    # Se não for encontrado
    if lam_not_found:
        x_corr = y
    else:
        x_corr = y + lam * delta       #Equação 3.30

    # Corrigir os outros parâmetros
    x_corr_bar = sum(x_corr)
    delta_corr = y - x_corr
    delta_corr_bar = x_corr_bar - y_bar

    return y, x_corr, delta_corr, y_bar, x_corr_bar, delta_corr_bar, index_smart_range