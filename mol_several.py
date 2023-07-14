from model_H2 import exec_calc_H2
from model_CH4 import exec_calc_CH4
import numpy as np


def calc_mol_several_H2(phi_min, phi_max, phi_step, pressure_list):

    phi_range = np.arange(phi_min, phi_max + phi_step, phi_step)

    x_h2o = np.zeros((len(pressure_list), len(phi_range)))
    x_o2 = np.zeros((len(pressure_list), len(phi_range)))
    x_h2 = np.zeros((len(pressure_list), len(phi_range)))
    x_oh = np.zeros((len(pressure_list), len(phi_range)))
    x_o = np.zeros((len(pressure_list), len(phi_range)))
    x_h = np.zeros((len(pressure_list), len(phi_range)))
    x_ho2 = np.zeros((len(pressure_list), len(phi_range)))
    x_h2o2 = np.zeros((len(pressure_list), len(phi_range)))

    index = 0
    index2 = 0
    for pressure in pressure_list:
        for phi in phi_range:
            data = exec_calc_H2(phi, pressure)[1]
            x_h2o[index][index2] = data[0]
            x_o2[index][index2] = data[1]
            x_h2[index][index2] = data[2]
            x_oh[index][index2] = data[3]
            x_o[index][index2] = data[4]
            x_h[index][index2] = data[5]
            x_ho2[index][index2] = data[6]
            x_h2o2[index][index2] = data[7]
            index2 += 1

        index += 1
        index2 = 0

    return x_h2o, x_o2, x_h2, x_oh, x_o, x_h, x_ho2, x_h2o2

def calc_mol_several_CH4(phi_min, phi_max, phi_step, pressure_list):

    phi_range = np.arange(phi_min, phi_max + phi_step, phi_step)

    x_h2o = np.zeros((len(pressure_list), len(phi_range)))
    x_co2 = np.zeros((len(pressure_list), len(phi_range)))
    x_o2 = np.zeros((len(pressure_list), len(phi_range)))
    x_co = np.zeros((len(pressure_list), len(phi_range)))
    x_o = np.zeros((len(pressure_list), len(phi_range)))
    x_h2 = np.zeros((len(pressure_list), len(phi_range)))
    x_oh = np.zeros((len(pressure_list), len(phi_range)))
    x_h = np.zeros((len(pressure_list), len(phi_range)))

    index = 0
    index2 = 0
    for pressure in pressure_list:
        for phi in phi_range:
            data = exec_calc_CH4(phi, pressure)[1]
            x_h2o[index][index2] = data[0]
            x_co2[index][index2] = data[1]
            x_o2[index][index2] = data[2]
            x_co[index][index2] = data[3]
            x_o[index][index2] = data[4]
            x_h2[index][index2] = data[5]
            x_oh[index][index2] = data[6]
            x_h[index][index2] = data[7]
            index2 += 1

        index += 1
        index2 = 0

    return x_h2o, x_co2, x_o2, x_co, x_o, x_h2, x_oh, x_h