import numpy as np
import re

class Species_coefficients:
    txt_file_content_list = []

    @classmethod
    def get_txt_file_content(cls):
        with open('nasa9.txt', mode='r') as file:
            cls.txt_file_content_list = [line.strip() for line in file.readlines()]
    
    def __init__(self, species_str):
        self.species_str = species_str
        self.molecular_mass = 0
        self.hf_298_15 = 0
        self.low_coeff_list = []
        self.high_coeff_list = []
    
    def get_coeff(self):
        rows_content = np.zeros(5, dtype='object')
        rows_number_array_defined = False
        index = 0
        row_number = 1
        for row in Species_coefficients.txt_file_content_list:
            if bool(re.search(f'^{self.species_str}\s\s\s\s\s\s', row)):
                rows_number_list = np.array([row_number + 1, row_number + 3, row_number + 4, row_number + 6, row_number + 7])
                rows_number_array_defined = True
            
            # This if block will store the content of the lines we want in an array
            if rows_number_array_defined:
                if row_number in rows_number_list:
                    rows_content[index] = row
                    index += 1

                    if index == 5:
                        break
            
            row_number += 1
        
        if (rows_number_array_defined):
            self.molecular_mass = float(rows_content[0][54:65])
            self.hf_298_15 = float(rows_content[0][67:80])
            
            coeff_list_low = re.findall(r"[-+]?\d*\.\d+(?:[Ee][-+]?\d+)?", rows_content[1])
            coeff_list_low.extend(re.findall(r"[-+]?\d*\.\d+(?:[Ee][-+]?\d+)?".strip(), rows_content[2]))

            coeff_list_high = re.findall(r"[-+]?\d*\.\d+(?:[Ee][-+]?\d+)?", rows_content[3])
            coeff_list_high.extend(re.findall(r"[-+]?\d*\.\d+(?:[Ee][-+]?\d+)?", rows_content[4]))

            self.low_coeff_list = list(map(float, coeff_list_low[0:7])) + list(map(float, coeff_list_low[-2:]))
            self.high_coeff_list = list(map(float, coeff_list_high[0:7])) + list(map(float, coeff_list_high[-2:]))

    def specific_heat_pressure(self, temperature):
        if 200 <= temperature <= 1000:
            return 8.3145*(self.low_coeff_list[0] * temperature**-2 +
                           self.low_coeff_list[1] * temperature**-1 +
                           self.low_coeff_list[2] +
                           self.low_coeff_list[3] * temperature +
                           self.low_coeff_list[4] * temperature**2 +
                           self.low_coeff_list[5] * temperature**3 +
                           self.low_coeff_list[6] * temperature**4)
        elif 1000 < temperature <= 6000:
            return 8.3145*(self.high_coeff_list[0] * temperature**-2 +
                           self.high_coeff_list[1] * temperature**-1 +
                           self.high_coeff_list[2] +
                           self.high_coeff_list[3] * temperature +
                           self.high_coeff_list[4] * temperature**2 +
                           self.high_coeff_list[5] * temperature**3 +
                           self.high_coeff_list[6] * temperature**4)
        else:
            raise Exception("Error: temperature out of bounds [200 K, 6000 K]")

    def enthalpy(self, temperature):
        if 200 <= temperature <= 1000:
            return 8.3145*temperature*(-self.low_coeff_list[0] * temperature**-2 +
                                       self.low_coeff_list[1] * np.log(temperature) * temperature**-1 +
                                       self.low_coeff_list[2] +
                                       self.low_coeff_list[3] * temperature / 2 +
                                       self.low_coeff_list[4] * temperature**2 / 3 +
                                       self.low_coeff_list[5] * temperature**3 / 4 +
                                       self.low_coeff_list[6] * temperature**4 / 5 +
                                       self.low_coeff_list[7] / temperature)
        elif 1000 < temperature <= 6000:
            return 8.3145*temperature*(-self.high_coeff_list[0] * temperature**-2 +
                                       self.high_coeff_list[1] * np.log(temperature) * temperature**-1 +
                                       self.high_coeff_list[2] +
                                       self.high_coeff_list[3] * temperature / 2 +
                                       self.high_coeff_list[4] * temperature**2 / 3 +
                                       self.high_coeff_list[5] * temperature**3 / 4 +
                                       self.high_coeff_list[6] * temperature**4 / 5 +
                                       self.high_coeff_list[7] / temperature)
        else:
            raise Exception("Error: temperature out of bounds [200 K, 6000 K]")        

    def entropy(self, temperature):
        if 200 <= temperature <= 1000:
            return 8.3145*(-self.low_coeff_list[0] * temperature**-2 / 2 -
                           self.low_coeff_list[1] * temperature**-1 +
                           self.low_coeff_list[2] * np.log(temperature) +
                           self.low_coeff_list[3] * temperature +
                           self.low_coeff_list[4] * temperature**2 / 2 +
                           self.low_coeff_list[5] * temperature**3 / 3 +
                           self.low_coeff_list[6] * temperature**4 / 4 +
                           self.low_coeff_list[8])
        elif 1000 < temperature <= 6000:
            return 8.3145*(-self.high_coeff_list[0] * temperature**-2 / 2 -
                           self.high_coeff_list[1] * temperature**-1 +
                           self.high_coeff_list[2] * np.log(temperature) +
                           self.high_coeff_list[3] * temperature +
                           self.high_coeff_list[4] * temperature**2 / 2 +
                           self.high_coeff_list[5] * temperature**3 / 3 +
                           self.high_coeff_list[6] * temperature**4 / 4 +
                           self.high_coeff_list[8])
        else:
            raise Exception("Error: temperature out of bounds [200 K, 6000 K]")




# if __name__ == "__main__":
    # Species_coefficients.get_txt_file_content()
    # H2O = Species_coefficients("H2O")
    # H2O.get_coeff()
    # print(H2O.specific_heat_pressure(2000))
    # print(H2O.enthalpy(2000))
    # print(H2O.entropy(2000))

    # species_str_list = ["H2O", "O2", "H2", "OH"]
    # Species_coefficients.get_txt_file_content()
    # species_obj_dict = {s: Species_coefficients(s) for s in species_str_list}
    # for values in species_obj_dict.values():
    #     values.get_coeff()
    # T = 2000
    # enthalpy_298_15_dict = {s: species_obj_dict[s].enthalpy(298.15) for s in species_str_list}
    # enthalpy_dict = {s: species_obj_dict[s].enthalpy(T) for s in species_str_list}
    # entropy_dict = {s: species_obj_dict[s].entropy(T) for s in species_str_list}
    # hs_dict, hf_dict, g_f_dict = thermo_calc_1(enthalpy_298_15_dict, enthalpy_dict, entropy_dict, species_str_list, T)
    # print(hs_dict)
    # print(hf_dict)
    # print(g_f_dict)