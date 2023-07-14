def thermo_calc_1(enthalpy_298_15_dict, enthalpy_dict, entropy_dict, species_str_list, T):

    # A entalpia e a entropia vão ser necessários para os cálculos da entalpia sensivel,
    # entalpia de formação e função de Gibbs.
    # Por isso, é necessário calcular h e s através dos polinómios do ficheiro thermo.py

    # thermo.py --> return --> [molecular_mass, hf_298_15, c_p, h, s]

    # ====================================== sensible enthalpy for T ======================================

    hs_dict = {s: enthalpy_dict[s] - enthalpy_298_15_dict[s] for s in species_str_list}

    # ====================================== enthalpy of formation for T ======================================

    # Equação 3.51 da dissertação

    hf_o2 = 0
    hf_h2 = 0

    # H2 + 0.5 O2 ---> H2O

    hf_h2o = enthalpy_dict["H2O"] - (enthalpy_dict["H2"] + 0.5 * enthalpy_dict["O2"])

    # 0.5 H2 + 0.5 O2 ---> OH

    hf_oh = enthalpy_dict["OH"] - (0.5 * enthalpy_dict["H2"] + 0.5 * enthalpy_dict["O2"])

    hf_dict = {species_str_list[0]: hf_h2o,
               species_str_list[1]: hf_o2,
               species_str_list[2]: hf_h2,
               species_str_list[3]: hf_oh}

    # ====================================== Gibbs Function ======================================

    # Equação 3.50 da dissertação

    # H2O

    g_f_h2o = -entropy_dict["H2O"] + (enthalpy_dict["H2O"] - enthalpy_298_15_dict["H2O"]) / T

    # O2
    
    g_f_o2 = -entropy_dict["O2"] + (enthalpy_dict["O2"] - enthalpy_298_15_dict["O2"]) / T

    # H2

    g_f_h2 = -entropy_dict["H2"] + (enthalpy_dict["H2"] - enthalpy_298_15_dict["H2"]) / T

    # OH
    
    g_f_oh = -entropy_dict["OH"] + (enthalpy_dict["OH"] - enthalpy_298_15_dict["OH"]) / T 

    g_f_dict = {species_str_list[0]: g_f_h2o,
               species_str_list[1]: g_f_o2,
               species_str_list[2]: g_f_h2,
               species_str_list[3]: g_f_oh}

    return [hs_dict, hf_dict, g_f_dict]

def thermo_calc_2(enthalpy_298_15_dict, enthalpy_dict, entropy_dict, species_str_list, T):

    # A entalpia e a entropia vão ser necessários para os cálculos da entalpia sensivel,
    # entalpia de formação e função de Gibbs.
    # Por isso, é necessário calcular h e s através dos polinómios do ficheiro thermo.py

    # thermo.py --> return --> [molecular_mass, hf_298_15, c_p, h, s]

    # ====================================== sensible enthalpy for T ======================================

    hs_dict = {s: enthalpy_dict[s] - enthalpy_298_15_dict[s] for s in species_str_list}

    # ====================================== enthalpy of formation for T ======================================

    # Equação 3.51 da dissertação

    hf_o2 = 0
    hf_h2 = 0

    # H2 + 0.5 O2 ---> H2O

    hf_h2o = enthalpy_dict["H2O"] - (enthalpy_dict["H2"] + 0.5 * enthalpy_dict["O2"])

    # 0.5 H2 + 0.5 O2 ---> OH

    hf_oh = enthalpy_dict["OH"] - (0.5 * enthalpy_dict["H2"] + 0.5 * enthalpy_dict["O2"])

    # 0.5 O2 ---> O

    hf_o = enthalpy_dict["O"] - 0.5 * enthalpy_dict["O2"]

    # 0.5 H2 ---> H

    hf_h = enthalpy_dict["H"] - 0.5 * enthalpy_dict["H2"] 

    hf_dict = {species_str_list[0]: hf_h2o,
               species_str_list[1]: hf_o2,
               species_str_list[2]: hf_h2,
               species_str_list[3]: hf_oh,
               species_str_list[4]: hf_o,
               species_str_list[5]: hf_h}

    # ====================================== Gibbs Function ======================================

    # Equação 3.50 da dissertação

    # H2O

    g_f_h2o = -entropy_dict["H2O"] + (enthalpy_dict["H2O"] - enthalpy_298_15_dict["H2O"]) / T

    # O2
    
    g_f_o2 = -entropy_dict["O2"] + (enthalpy_dict["O2"] - enthalpy_298_15_dict["O2"]) / T

    # H2

    g_f_h2 = -entropy_dict["H2"] + (enthalpy_dict["H2"] - enthalpy_298_15_dict["H2"]) / T

    # OH
    
    g_f_oh = -entropy_dict["OH"] + (enthalpy_dict["OH"] - enthalpy_298_15_dict["OH"]) / T

    # O
    
    g_f_o = -entropy_dict["O"] + (enthalpy_dict["O"] - enthalpy_298_15_dict["O"]) / T

    # H
    
    g_f_h = -entropy_dict["H"] + (enthalpy_dict["H"] - enthalpy_298_15_dict["H"]) / T    

    g_f_dict = {species_str_list[0]: g_f_h2o,
               species_str_list[1]: g_f_o2,
               species_str_list[2]: g_f_h2,
               species_str_list[3]: g_f_oh,
               species_str_list[4]: g_f_o,
               species_str_list[5]: g_f_h}

    return [hs_dict, hf_dict, g_f_dict]

def thermo_calc_3(enthalpy_298_15_dict, enthalpy_dict, entropy_dict, species_str_list, T):

    # A entalpia e a entropia vão ser necessários para os cálculos da entalpia sensivel,
    # entalpia de formação e função de Gibbs.
    # Por isso, é necessário calcular h e s através dos polinómios do ficheiro thermo.py

    # thermo.py --> return --> [molecular_mass, hf_298_15, c_p, h, s]

    # ====================================== sensible enthalpy for T ======================================

    hs_dict = {s: enthalpy_dict[s] - enthalpy_298_15_dict[s] for s in species_str_list}

    # ====================================== enthalpy of formation for T ======================================

    # Equação 3.51 da dissertação

    hf_o2 = 0
    hf_h2 = 0

    # H2 + 0.5 O2 ---> H2O

    hf_h2o = enthalpy_dict["H2O"] - (enthalpy_dict["H2"] + 0.5 * enthalpy_dict["O2"])

    # 0.5 H2 + 0.5 O2 ---> OH

    hf_oh = enthalpy_dict["OH"] - (0.5 * enthalpy_dict["H2"] + 0.5 * enthalpy_dict["O2"])

    # 0.5 O2 ---> O

    hf_o = enthalpy_dict["O"] - 0.5 * enthalpy_dict["O2"]

    # 0.5 H2 ---> H

    hf_h = enthalpy_dict["H"] - 0.5 * enthalpy_dict["H2"] 

    # 0.5 H2 + O2 ---> HO2

    hf_ho2 = enthalpy_dict["HO2"] - (0.5 * enthalpy_dict["H2"] + enthalpy_dict["O2"])

    # H2 + O2 ---> H2O2

    hf_h2o2 = enthalpy_dict["H2O2"] - (enthalpy_dict["H2"] + enthalpy_dict["O2"])

    hf_dict = {species_str_list[0]: hf_h2o,
               species_str_list[1]: hf_o2,
               species_str_list[2]: hf_h2,
               species_str_list[3]: hf_oh,
               species_str_list[4]: hf_o,
               species_str_list[5]: hf_h,
               species_str_list[6]: hf_ho2,
               species_str_list[7]: hf_h2o2}

    # ====================================== Gibbs Function ======================================

    # Equação 3.50 da dissertação

    # H2O

    g_f_h2o = -entropy_dict["H2O"] + (enthalpy_dict["H2O"] - enthalpy_298_15_dict["H2O"]) / T

    # O2
    
    g_f_o2 = -entropy_dict["O2"] + (enthalpy_dict["O2"] - enthalpy_298_15_dict["O2"]) / T

    # H2

    g_f_h2 = -entropy_dict["H2"] + (enthalpy_dict["H2"] - enthalpy_298_15_dict["H2"]) / T

    # OH
    
    g_f_oh = -entropy_dict["OH"] + (enthalpy_dict["OH"] - enthalpy_298_15_dict["OH"]) / T

    # O
    
    g_f_o = -entropy_dict["O"] + (enthalpy_dict["O"] - enthalpy_298_15_dict["O"]) / T

    # H
    
    g_f_h = -entropy_dict["H"] + (enthalpy_dict["H"] - enthalpy_298_15_dict["H"]) / T    

    # HO2

    g_f_ho2 = -entropy_dict["HO2"] + (enthalpy_dict["HO2"] - enthalpy_298_15_dict["HO2"]) / T

    # H2O2

    g_f_h2o2 = -entropy_dict["H2O2"] + (enthalpy_dict["H2O2"] - enthalpy_298_15_dict["H2O2"]) / T

    g_f_dict = {species_str_list[0]: g_f_h2o,
               species_str_list[1]: g_f_o2,
               species_str_list[2]: g_f_h2,
               species_str_list[3]: g_f_oh,
               species_str_list[4]: g_f_o,
               species_str_list[5]: g_f_h,
               species_str_list[6]: g_f_ho2,
               species_str_list[7]: g_f_h2o2}

    return [hs_dict, hf_dict, g_f_dict]

def thermo_calc_4(enthalpy_298_15_dict, enthalpy_dict, entropy_dict, species_str_list, T):

    # A entalpia e a entropia vão ser necessários para os cálculos da entalpia sensivel,
    # entalpia de formação e função de Gibbs.
    # Por isso, é necessário calcular h e s através dos polinómios do ficheiro thermo.py

    # thermo.py --> return --> [molecular_mass, hf_298_15, c_p, h, s]

    # ====================================== sensible enthalpy for T ======================================

    hs_dict = {s: enthalpy_dict[s] - enthalpy_298_15_dict[s] for s in species_str_list}

    # ====================================== Gibbs Function ======================================

    # Equação 3.50 da dissertação

    # H2O

    g_f_h2o = -entropy_dict["H2O"] + (enthalpy_dict["H2O"] - enthalpy_298_15_dict["H2O"]) / T

    # CO2

    g_f_co2 = -entropy_dict["CO2"] + (enthalpy_dict["CO2"] - enthalpy_298_15_dict["CO2"]) / T

    # O2
    
    g_f_o2 = -entropy_dict["O2"] + (enthalpy_dict["O2"] - enthalpy_298_15_dict["O2"]) / T

    # CO

    g_f_co = -entropy_dict["CO"] + (enthalpy_dict["CO"] - enthalpy_298_15_dict["CO"]) / T

    # O

    g_f_o = -entropy_dict["O"] + (enthalpy_dict["O"] - enthalpy_298_15_dict["O"]) / T

    # H2

    g_f_h2 = -entropy_dict["H2"] + (enthalpy_dict["H2"] - enthalpy_298_15_dict["H2"]) / T

    # OH

    g_f_oh = -entropy_dict["OH"] + (enthalpy_dict["OH"] - enthalpy_298_15_dict["OH"]) / T

    # H

    g_f_h = -entropy_dict["H"] + (enthalpy_dict["H"] - enthalpy_298_15_dict["H"]) / T

    g_f_dict = {species_str_list[0]: g_f_h2o,
               species_str_list[1]: g_f_co2,
               species_str_list[2]: g_f_o2,
               species_str_list[3]: g_f_co,
               species_str_list[4]: g_f_o,
               species_str_list[5]: g_f_h2,
               species_str_list[6]: g_f_oh,
               species_str_list[7]: g_f_h}

    return [hs_dict, 0, g_f_dict]

def thermo_calc_5(enthalpy_298_15_dict, enthalpy_dict, entropy_dict, species_str_list, T):

    # A entalpia e a entropia vão ser necessários para os cálculos da entalpia sensivel,
    # entalpia de formação e função de Gibbs.
    # Por isso, é necessário calcular h e s através dos polinómios do ficheiro thermo.py

    # thermo.py --> return --> [molecular_mass, hf_298_15, c_p, h, s]

    # ====================================== sensible enthalpy for T ======================================

    hs_dict = {s: enthalpy_dict[s] - enthalpy_298_15_dict[s] for s in species_str_list}

    # ====================================== Gibbs Function ======================================

    # Equação 3.50 da dissertação

    # H2O

    g_f_h2o = -entropy_dict["H2O"] + (enthalpy_dict["H2O"] - enthalpy_298_15_dict["H2O"]) / T

    # CO2

    g_f_co2 = -entropy_dict["CO2"] + (enthalpy_dict["CO2"] - enthalpy_298_15_dict["CO2"]) / T

    # O2
    
    g_f_o2 = -entropy_dict["O2"] + (enthalpy_dict["O2"] - enthalpy_298_15_dict["O2"]) / T

    # CO

    g_f_co = -entropy_dict["CO"] + (enthalpy_dict["CO"] - enthalpy_298_15_dict["CO"]) / T

    # O

    g_f_o = -entropy_dict["O"] + (enthalpy_dict["O"] - enthalpy_298_15_dict["O"]) / T

    # H2

    g_f_h2 = -entropy_dict["H2"] + (enthalpy_dict["H2"] - enthalpy_298_15_dict["H2"]) / T

    # OH

    g_f_oh = -entropy_dict["OH"] + (enthalpy_dict["OH"] - enthalpy_298_15_dict["OH"]) / T

    # H

    g_f_h = -entropy_dict["H"] + (enthalpy_dict["H"] - enthalpy_298_15_dict["H"]) / T

    # N2

    g_f_n2 = -entropy_dict["N2"] + (enthalpy_dict["N2"] - enthalpy_298_15_dict["N2"]) / T

    # NO

    g_f_no = -entropy_dict["NO"] + (enthalpy_dict["NO"] - enthalpy_298_15_dict["NO"]) / T

    # Ar

    g_f_ar = -entropy_dict["Ar"] + (enthalpy_dict["Ar"] - enthalpy_298_15_dict["Ar"]) / T

    g_f_dict = {species_str_list[0]: g_f_h2o,
               species_str_list[1]: g_f_o2,
               species_str_list[2]: g_f_h2,
               species_str_list[3]: g_f_oh,
               species_str_list[4]: g_f_o,
               species_str_list[5]: g_f_h,
               species_str_list[6]: g_f_no,
               species_str_list[7]: g_f_n2,
               species_str_list[8]: g_f_co,
               species_str_list[9]: g_f_co2,
               species_str_list[10]: g_f_ar}

    return [hs_dict, 0, g_f_dict]