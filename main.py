import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from model_H2 import exec_calc_H2
from model_CH4 import exec_calc_CH4
from Tad_several import calc_Tad_several_H2, calc_Tad_several_CH4
from mol_several import calc_mol_several_H2, calc_mol_several_CH4

class AppGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("App")

        self.equivalence_ratio_H2 = tk.DoubleVar()
        self.pressure_H2 = tk.DoubleVar()

        self.equivalence_ratio_CH4 = tk.DoubleVar()
        self.pressure_CH4 = tk.DoubleVar()

        self.min_equivalence_ratio_H2 = tk.DoubleVar()
        self.max_equivalence_ratio_H2 = tk.DoubleVar()
        self.step_equivalence_ratio_H2 = tk.DoubleVar()

        self.min_equivalence_ratio_CH4 = tk.DoubleVar()
        self.max_equivalence_ratio_CH4 = tk.DoubleVar()
        self.step_equivalence_ratio_CH4 = tk.DoubleVar()

        self.pressure_values_H2 = tk.StringVar()
        self.pressure_values_CH4 = tk.StringVar()

        self.display_mode_H2 = tk.StringVar()
        self.display_mode_H2.set("Molar Fraction")

        self.display_mode_CH4 = tk.StringVar()
        self.display_mode_CH4.set("Molar Fraction")

        self.create_widgets()

    def create_widgets(self):
        # Option H2
        H2_frame = tk.Frame(self.window)
        H2_frame.pack(side=tk.LEFT, padx=10, pady=10)

        H2_label = tk.Label(H2_frame, text="H2")
        H2_label.pack()

        equivalence_ratio_H2_label = tk.Label(H2_frame, text="Equivalence Ratio")
        equivalence_ratio_H2_label.pack()

        equivalence_ratio_H2_entry = tk.Entry(H2_frame, textvariable=self.equivalence_ratio_H2)
        equivalence_ratio_H2_entry.pack()

        pressure_H2_label = tk.Label(H2_frame, text="Pressure (bar)")
        pressure_H2_label.pack()

        pressure_H2_entry = tk.Entry(H2_frame, textvariable=self.pressure_H2)
        pressure_H2_entry.pack()

        H2_button = tk.Button(H2_frame, text="Calculate H2", command=self.calculate_H2)
        H2_button.pack(pady=10)

        # Chemical equation button for H2
        H2_reaction_button = tk.Button(H2_frame, text="Show Reaction Equation", command=self.show_reaction_H2)
        H2_reaction_button.pack(pady=10)

        display_mode_H2_label = tk.Label(H2_frame, text="Display Mode")
        display_mode_H2_label.pack()

        display_mode_H2_option1 = tk.Radiobutton(H2_frame, text="Molar Fraction", variable=self.display_mode_H2, value="Molar Fraction")
        display_mode_H2_option1.pack()

        display_mode_H2_option2 = tk.Radiobutton(H2_frame, text="Mole Number", variable=self.display_mode_H2, value="Mole Number")
        display_mode_H2_option2.pack()

        # Result and Export for H2
        result_frame_H2 = tk.Frame(self.window)
        result_frame_H2.pack(side=tk.LEFT, padx=10, pady=10)

        self.result_label_H2 = tk.Label(result_frame_H2, text="H2 results will be shown here.")
        self.result_label_H2.pack(pady=10)

        self.export_button_H2 = tk.Button(result_frame_H2, text="Export H2 Results", command=self.export_results_H2)
        self.export_button_H2.pack(pady=10)

        # Additional computations for H2
        min_equivalence_ratio_H2_label = tk.Label(H2_frame, text="Lowest equivalence ratio value")
        min_equivalence_ratio_H2_label.pack(pady=1)

        min_equivalence_ratio_H2_entry = tk.Entry(H2_frame, textvariable=self.min_equivalence_ratio_H2)
        min_equivalence_ratio_H2_entry.pack(pady=10)

        max_equivalence_ratio_H2_label = tk.Label(H2_frame, text="Highest equivalence ratio value")
        max_equivalence_ratio_H2_label.pack(pady=1)

        max_equivalence_ratio_H2_entry = tk.Entry(H2_frame, textvariable=self.max_equivalence_ratio_H2)
        max_equivalence_ratio_H2_entry.pack(pady=10)

        step_equivalence_ratio_H2_label = tk.Label(H2_frame, text="Step size for equivalence ratio")
        step_equivalence_ratio_H2_label.pack(pady=1)

        step_equivalence_ratio_H2_entry = tk.Entry(H2_frame, textvariable=self.step_equivalence_ratio_H2)
        step_equivalence_ratio_H2_entry.pack(pady=10)

        pressure_values_H2_label = tk.Label(H2_frame, text="Pressure values in bar (separated by comma)")
        pressure_values_H2_label.pack(pady=1)

        pressure_values_H2_entry = tk.Entry(H2_frame, textvariable=self.pressure_values_H2)
        pressure_values_H2_entry.pack(pady=10)

        compute_temp_button_H2 = tk.Button(H2_frame, text="Compute Adiabatic Flame Temp", command=self.compute_adiabatic_flame_temp_H2)
        compute_temp_button_H2.pack(pady=10)

        compute_composition_button_H2 = tk.Button(H2_frame, text="Compute Species Composition", command=self.compute_species_composition_H2)
        compute_composition_button_H2.pack(pady=10)

        # Option CH4
        CH4_frame = tk.Frame(self.window)
        CH4_frame.pack(side=tk.LEFT, padx=10, pady=10)

        CH4_label = tk.Label(CH4_frame, text="CH4")
        CH4_label.pack()

        equivalence_ratio_CH4_label = tk.Label(CH4_frame, text="Equivalence Ratio")
        equivalence_ratio_CH4_label.pack()

        equivalence_ratio_CH4_entry = tk.Entry(CH4_frame, textvariable=self.equivalence_ratio_CH4)
        equivalence_ratio_CH4_entry.pack()

        pressure_CH4_label = tk.Label(CH4_frame, text="Pressure (bar)")
        pressure_CH4_label.pack()

        pressure_CH4_entry = tk.Entry(CH4_frame, textvariable=self.pressure_CH4)
        pressure_CH4_entry.pack()

        CH4_button = tk.Button(CH4_frame, text="Calculate CH4", command=self.calculate_CH4)
        CH4_button.pack(pady=10)

        # Chemical equation button for CH4
        CH4_reaction_button = tk.Button(CH4_frame, text="Show Reaction Equation", command=self.show_reaction_equation_CH4)
        CH4_reaction_button.pack(pady=10)

        display_mode_CH4_label = tk.Label(CH4_frame, text="Display Mode")
        display_mode_CH4_label.pack()

        display_mode_CH4_option1 = tk.Radiobutton(CH4_frame, text="Molar Fraction", variable=self.display_mode_CH4, value="Molar Fraction")
        display_mode_CH4_option1.pack()

        display_mode_CH4_option2 = tk.Radiobutton(CH4_frame, text="Mole Number", variable=self.display_mode_CH4, value="Mole Number")
        display_mode_CH4_option2.pack()

        # Result and Export for CH4
        result_frame_CH4 = tk.Frame(self.window)
        result_frame_CH4.pack(side=tk.LEFT, padx=10, pady=10)

        self.result_label_CH4 = tk.Label(result_frame_CH4, text="CH4 results will be shown here.")
        self.result_label_CH4.pack(pady=10)

        self.export_button_CH4 = tk.Button(result_frame_CH4, text="Export CH4 Results", command=self.export_results_CH4)
        self.export_button_CH4.pack(pady=10)

        # Additional computations for CH4
        min_equivalence_ratio_CH4_label = tk.Label(CH4_frame, text="Lowest equivalence ratio value")
        min_equivalence_ratio_CH4_label.pack(pady=1)

        min_equivalence_ratio_CH4_entry = tk.Entry(CH4_frame, textvariable=self.min_equivalence_ratio_CH4)
        min_equivalence_ratio_CH4_entry.pack(pady=10)

        max_equivalence_ratio_CH4_label = tk.Label(CH4_frame, text="Highest equivalence ratio value")
        max_equivalence_ratio_CH4_label.pack(pady=1)

        max_equivalence_ratio_CH4_entry = tk.Entry(CH4_frame, textvariable=self.max_equivalence_ratio_CH4)
        max_equivalence_ratio_CH4_entry.pack(pady=10)

        step_equivalence_ratio_CH4_label = tk.Label(CH4_frame, text="Step size for equivalence ratio")
        step_equivalence_ratio_CH4_label.pack(pady=1)

        step_equivalence_ratio_CH4_entry = tk.Entry(CH4_frame, textvariable=self.step_equivalence_ratio_CH4)
        step_equivalence_ratio_CH4_entry.pack(pady=10)

        pressure_values_CH4_label = tk.Label(CH4_frame, text="Pressure values in bar (separated by comma)")
        pressure_values_CH4_label.pack(pady=1)

        pressure_values_CH4_entry = tk.Entry(CH4_frame, textvariable=self.pressure_values_CH4)
        pressure_values_CH4_entry.pack(pady=10)

        compute_temp_button_CH4 = tk.Button(CH4_frame, text="Compute Adiabatic Flame Temp", command=self.compute_adiabatic_flame_temp_CH4)
        compute_temp_button_CH4.pack(pady=10)

        compute_composition_button_CH4 = tk.Button(CH4_frame, text="Compute Species Composition", command=self.compute_species_composition_CH4)
        compute_composition_button_CH4.pack(pady=10)

    @staticmethod
    def check_display_mode(display_mode):
        if display_mode == "Molar Fraction":
            return 1
        elif display_mode == "Mole Number":
            return 4
        else:
            raise Exception("Display Mode error")

    @staticmethod
    def calculate_single_H2(display_mode, equivalence_ratio, pressure):
        index = AppGUI.check_display_mode(display_mode)
        calc_results = exec_calc_H2(equivalence_ratio, pressure)

        adiabatic_flame_temp = calc_results[0]
        species_compositions = {
            "H2O": calc_results[index][0],
            "O2": calc_results[index][1],
            "H2": calc_results[index][2],
            "OH": calc_results[index][3],
            "O": calc_results[index][4],
            "H": calc_results[index][5],
            "HO2": calc_results[index][6],
            "H2O2": calc_results[index][7]
        }
        return adiabatic_flame_temp, species_compositions        

    @staticmethod
    def calculate_single_CH4(display_mode, equivalence_ratio, pressure):
        index = AppGUI.check_display_mode(display_mode)
        calc_results = exec_calc_CH4(equivalence_ratio, pressure)

        adiabatic_flame_temp = calc_results[0]
        species_compositions = {
            "H2O": calc_results[index][0],
            "CO2": calc_results[index][1],
            "O2": calc_results[index][2],
            "CO": calc_results[index][3],
            "O": calc_results[index][4],
            "H2": calc_results[index][5],
            "OH": calc_results[index][6],
            "H": calc_results[index][7]
        }
        return adiabatic_flame_temp, species_compositions

    def calculate_H2(self):
        display_mode = self.display_mode_H2.get()
        adiabatic_flame_temp, species_compositions = self.calculate_single_H2(display_mode,
                                                                              self.equivalence_ratio_H2.get(),
                                                                              self.pressure_H2.get())

        self.display_results("H2", adiabatic_flame_temp, species_compositions, display_mode)

    def calculate_CH4(self):
        display_mode = self.display_mode_CH4.get()
        adiabatic_flame_temp, species_compositions = self.calculate_single_CH4(display_mode,
                                                                               self.equivalence_ratio_CH4.get(),
                                                                               self.pressure_CH4.get())

        self.display_results("CH4", adiabatic_flame_temp, species_compositions, display_mode)

    def compute_adiabatic_flame_temp_H2(self):
        min_ratio = self.min_equivalence_ratio_H2.get()
        max_ratio = self.max_equivalence_ratio_H2.get()
        step_ratio = self.step_equivalence_ratio_H2.get()
        pressure_values = [float(value) for value in self.pressure_values_H2.get().split(",")]

        Tad_results = calc_Tad_several_H2(min_ratio, max_ratio, step_ratio, pressure_values)

        file_path = self.export_Tad_results(Tad_results,
                                            "Adiabatic Flame Temperature H2 Combustion Reaction",
                                            min_ratio,
                                            max_ratio,
                                            step_ratio,
                                            pressure_values)
        
        messagebox.showinfo("Export H2 Results", f"H2 results exported to:\n{file_path}")

    def compute_adiabatic_flame_temp_CH4(self):
        min_ratio = self.min_equivalence_ratio_CH4.get()
        max_ratio = self.max_equivalence_ratio_CH4.get()
        step_ratio = self.step_equivalence_ratio_CH4.get()
        pressure_values = [float(value) for value in self.pressure_values_CH4.get().split(",")]

        Tad_results = calc_Tad_several_CH4(min_ratio, max_ratio, step_ratio, pressure_values)

        file_path = self.export_Tad_results(Tad_results,
                                            "Adiabatic Flame Temperature CH4 Combustion Reaction",
                                            min_ratio,
                                            max_ratio,
                                            step_ratio,
                                            pressure_values)

        messagebox.showinfo("Export CH4 Results", f"CH4 results exported to:\n{file_path}")

    def compute_species_composition_H2(self):
        min_ratio = self.min_equivalence_ratio_H2.get()
        max_ratio = self.max_equivalence_ratio_H2.get()
        step_ratio = self.step_equivalence_ratio_H2.get()
        pressure_values = [float(value) for value in self.pressure_values_H2.get().split(",")]

        result = calc_mol_several_H2(min_ratio, max_ratio, step_ratio, pressure_values)
        file_path = self.export_mol_results(result,
                                            "Species Molar Fraction (H2)",
                                            min_ratio,
                                            max_ratio,
                                            step_ratio,
                                            pressure_values,
                                            ["H2O", "O2", "H2", "OH", "O", "H", "HO2", "H2O2"])
        
        messagebox.showinfo("Export H2 Results", f"H2 results exported to:\n{file_path}")

    def compute_species_composition_CH4(self):
        min_ratio = self.min_equivalence_ratio_CH4.get()
        max_ratio = self.max_equivalence_ratio_CH4.get()
        step_ratio = self.step_equivalence_ratio_CH4.get()
        pressure_values = [float(value) for value in self.pressure_values_CH4.get().split(",")]

        result = calc_mol_several_CH4(min_ratio, max_ratio, step_ratio, pressure_values)
        file_path = self.export_mol_results(result,
                                            "Species Molar Fraction (CH4)",
                                            min_ratio,
                                            max_ratio,
                                            step_ratio,
                                            pressure_values,
                                            ["H2O", "CO2", "O2", "CO", "O", "H2", "OH", "H"])
        
        messagebox.showinfo("Export CH4 Results", f"CH4 results exported to:\n{file_path}")

    def show_reaction_H2(self):
        reaction_equation = "H2 + a O2 -> n1 H2O + n2 O2 + n3 H2 + n4 OH + n5 O + n6 H + n7 HO2 + n8 H2O2"
        messagebox.showinfo("Reaction Equation - H2", reaction_equation)

    def show_reaction_equation_CH4(self):
        reaction_equation = "CH4 + a O2 -> n1 H2O + n2 CO2 + n3 O2 + n4 CO + n5 O + n6 H2 + n7 OH + n8 H"
        messagebox.showinfo("Reaction Equation - CH4", reaction_equation)

    def export_single_results(self, title, equivalence_ratio, temperature, species_composition, display_mode):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt")
        with open(file_path, "w") as file:
            file.write(f"{title}\n")
            file.write(f"Equivalence Ratio: {equivalence_ratio:.2f}\n")
            file.write(f"Adiabatic Flame Temperature: {temperature:.2f} K\n")
            file.write(display_mode)
            file.write("\n")
            for species, value in species_composition.items():
                file.write(f"{species}: {value:.2f}\n")
        return file_path
    
    def export_Tad_results(self, results, title, min_ratio, max_ratio, step_ratio, pressure_list):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt")
        index = 0
        str1 = "                        "
        for pressure in pressure_list:
            str1 += "{:<25}".format(f"Pressure = {pressure} bar")
        with open(file_path, "w") as file:
            file.write(f"{title}\n")
            file.write("{:<23} {:<35}".format("Equivalence Ratio", "Adiabatic Flame Temperature"))
            file.write("\n")
            file.write(str1)
            file.write("\n")
            for ratio in self.range_generator(min_ratio, max_ratio + step_ratio, step_ratio):
                file.write(f"{ratio:<24.2f}")
                for i in range(0,3):
                    print(results)
                    file.write(f"{results[index][i]:<25.2f}")
                file.write("\n")
                index += 1
        return file_path

    def export_mol_results(self, results, title, min_ratio, max_ratio, step_ratio, pressure_list, species_list):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt")
        str1 = "{:<20}".format("Equivalence Ratio")
        species_index = 0
        pressure_index = 0
        ratio_index = 0
        for species in species_list:
            str1 += "{:<12}".format(species)
        with open(file_path, "w") as file:
            file.write(f"{title}\n")
            for pressure in pressure_list:
                file.write(f"Pressure = {pressure} bar\n")
                file.write(str1)
                file.write("\n")
                for ratio in self.range_generator(min_ratio, max_ratio + step_ratio, step_ratio):
                    file.write("{:<20.2f}".format(ratio))
                    for species in species_list:
                        file.write("{:<12.7f}".format(results[species_index][pressure_index][ratio_index]))
                        species_index += 1
                    file.write("\n")
                    species_index = 0
                    ratio_index += 1
                file.write("\n")
                ratio_index = 0
                pressure_index += 1

        return file_path

    # Perform export for H2 results
    def export_results_H2(self):
        display_mode = self.display_mode_H2.get()
        adiabatic_flame_temp, species_compositions = self.calculate_single_H2(display_mode,
                                                                              self.equivalence_ratio_H2.get(),
                                                                              self.pressure_H2.get())

        file_path = self.export_single_results("H2 Combustion Reaction",
                                               self.equivalence_ratio_H2.get(),
                                               adiabatic_flame_temp,
                                               species_compositions,
                                               self.display_mode_H2.get())
        
        messagebox.showinfo("Export H2 Results", f"H2 results exported to:\n{file_path}")

    # Perform export for CH4 results
    def export_results_CH4(self):
        display_mode = self.display_mode_CH4.get()
        adiabatic_flame_temp, species_compositions = self.calculate_single_CH4(display_mode,
                                                                               self.equivalence_ratio_CH4.get(),
                                                                               self.pressure_CH4.get())

        file_path = self.export_single_results("CH4 Combustion Reaction",
                                               self.equivalence_ratio_CH4.get(),
                                               adiabatic_flame_temp,
                                               species_compositions,
                                               display_mode)
        
        messagebox.showinfo("Export CH4 Results", f"CH4 results exported to:\n{file_path}")

    def range_generator(self, start, end, step):
        current = start
        while current <= end:
            yield current
            current += step

    def display_results(self, option, adiabatic_flame_temp, species_compositions, display_mode):
        # display_mode = self.display_mode.get()
        result_text = f"{option} Results:\n\n"
        result_text += f"Adiabatic Flame Temperature: {adiabatic_flame_temp:.2f} K\n\n"
        result_text += "Species Compositions:\n"
        for species, value in species_compositions.items():
            if display_mode == "Molar Fraction":
                result_text += f"{species}: {value:.2f}\n"
            elif display_mode == "Mole Number":
                result_text += f"{species}: {value:.2f} moles\n"
        if option == "H2":
            self.result_label_H2.config(text=result_text)
        elif option == "CH4":
            self.result_label_CH4.config(text=result_text)

    def run(self):
        self.window.mainloop()

calculator = AppGUI()
calculator.run()
