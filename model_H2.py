###############################################################################################
#
# -> Este script faz o cálculo da temperatura adiabática chama para o modelo 3 para uma dada razão de
#    equivalência e pressão (em bar)
#
###############################################################################################

from iterateLagrange import iterateLagrange
# from initial_guess import initialGuess
from initialGuess import initialGuess_H2_O2
from Species_coefficients import Species_coefficients
from thermo_calc import thermo_calc_3
import numpy as np
import time

def exec_calc_H2(phi, pressure, max_it=50):
    """
    Função que faz o cálculo da temperatura adiabática de chama
    (e consequentemente da composição de equilibrio química)

    """

    R = 8.3145

    species_str_list = ["H2O", "O2", "H2", "OH", "O", "H", "HO2", "H2O2"]
    Species_coefficients.get_txt_file_content()
    species_obj_dict = {s: Species_coefficients(s) for s in species_str_list}
    for values in species_obj_dict.values():
        values.get_coeff()
    enthalpy_298_15_dict = {s: species_obj_dict[s].enthalpy(298.15) for s in species_str_list}

    # m_ox / m_fuel
    mass_ratio = 16 / (2 * phi)
    
    a_coef = mass_ratio * (2 / 32)

    #***********************************************************************************************
    # Parâmetros do modelo 1

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

    y        = np.array(initialGuess_H2_O2(phi, a_coef))
    #***********************************************************************************************

    # T1 < Tad    
    T1 = 2000
    # T2 > Tad
    T2 = 3900

    for k in range(1, max_it):
        
        iterations = k

        # Para o Método da Bisseção:
        Tad = (T1 + T2) / 2

        # ============================== chemical equilibrium for T1 ==============================

        T = T1

        enthalpy_dict = {s: species_obj_dict[s].enthalpy(T) for s in species_str_list}
        entropy_dict = {s: species_obj_dict[s].entropy(T) for s in species_str_list}

        hs_dict, hf_dict, g_f_dict = thermo_calc_3(enthalpy_298_15_dict,
                                                   enthalpy_dict,
                                                   entropy_dict,
                                                   species_str_list,
                                                   T)

        g_RT = [1/R * g_f_dict[s] + np.array(enthalpy_298_15_dict[s] / (R * T)) for s in species_str_list]

        sol = iterateLagrange(pressure,g_RT,i,j,a,b,y,max_it)

        deltaH_R1 = np.dot(sol, [hs_dict[s] for s in species_str_list]) + \
            sol[0] * species_obj_dict["H2O"].hf_298_15 + sol[3] * species_obj_dict["OH"].hf_298_15 + \
            sol[4] * species_obj_dict["O"].hf_298_15 + sol[5] * species_obj_dict["H"].hf_298_15 + \
            sol[6] * species_obj_dict["HO2"].hf_298_15 + sol[7] * species_obj_dict["H2O2"].hf_298_15

        # ============================== chemical equilibrium Tad ==============================

        T = Tad

        enthalpy_dict = {s: species_obj_dict[s].enthalpy(T) for s in species_str_list}
        entropy_dict = {s: species_obj_dict[s].entropy(T) for s in species_str_list}

        hs_dict, hf_dict, g_f_dict = thermo_calc_3(enthalpy_298_15_dict,
                                                   enthalpy_dict,
                                                   entropy_dict,
                                                   species_str_list,
                                                   T)

        g_RT = [1/R * g_f_dict[s] + np.array(enthalpy_298_15_dict[s] / (R * T)) for s in species_str_list]

        sol = iterateLagrange(pressure,g_RT,i,j,a,b,y,max_it)

        deltaH_Rad = np.dot(sol, [hs_dict[s] for s in species_str_list]) + \
            sol[0] * species_obj_dict["H2O"].hf_298_15 + sol[3] * species_obj_dict["OH"].hf_298_15 + \
            sol[4] * species_obj_dict["O"].hf_298_15 + sol[5] * species_obj_dict["H"].hf_298_15 + \
            sol[6] * species_obj_dict["HO2"].hf_298_15 + sol[7] * species_obj_dict["H2O2"].hf_298_15

        # Método da Bisseção
        if deltaH_R1 * deltaH_Rad < 0:
            T2 = Tad
        else:
            T1 = Tad

        # Verificação do erro
        if 0 < abs(deltaH_Rad) < 100:
            break
        else:
            continue

    mol_fraction = sol/sum(sol)

    return [Tad, mol_fraction, deltaH_Rad, iterations, sol]

if __name__ == '__main__':
    start = time.time()
    results = exec_calc_H2(1.6, 10)
    end = time.time()
    print(f"Adiabatic flame temperature {results[0]}")
    print(f"Chemical equilibrium composition {results[1]}")
    print("Mol Number:")
    print(results[-1])
    print(end - start)
