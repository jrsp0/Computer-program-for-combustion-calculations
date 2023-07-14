from model_H2 import exec_calc_H2
from model_CH4 import exec_calc_CH4
import numpy as np

def calc_Tad_several_H2(phi_min, phi_max, phi_step, pressure_list):

    phi_range = np.arange(phi_min, phi_max + phi_step, phi_step)

    Tad_array = np.zeros((len(phi_range), 3))

    index2 = 0
    for pressure in pressure_list:
        index = 0
        for phi in phi_range:
            Tad_array[index, index2] = exec_calc_H2(phi, pressure)[0]
            index += 1
        index2 += 1

    return Tad_array

def calc_Tad_several_CH4(phi_min, phi_max, phi_step, pressure_list):

    phi_range = np.arange(phi_min, phi_max + phi_step, phi_step)

    Tad_array = np.zeros((len(phi_range), 3))

    index2 = 0
    for pressure in pressure_list:
        index = 0
        for phi in phi_range:
            Tad_array[index, index2] = exec_calc_CH4(phi, pressure)[0]
            index += 1
        index2 += 1

    return Tad_array