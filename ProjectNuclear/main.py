from Model.constants import Elements
from Model.constants import Values
import numpy as np
import random
import pandas as pd
from Model.nuclear_formulas import NuclearFormulas

def variation_gauss(number):
    max_dispersion = 0.05
    dispersion = number * random.uniform(0, max_dispersion)
    variation = random.gauss(0, dispersion)
    return number + variation

def simulate_nuclear_reaction_over_time(neutron_flux, initial_mass):
    results = []
    min_mass = 0.00001  # Set the minimum mass threshold
    max_time = 1000

    for t in range(max_time):
        remaining_nuclei, remaining_mass = NuclearFormulas.remaining_nuclei_mass(neutron_flux, initial_mass, t)
        remaining_energy = NuclearFormulas.einstein_nuclear_reaction(initial_mass, remaining_mass)
        results.append((t,variation_gauss(remaining_nuclei), variation_gauss(remaining_mass), variation_gauss(remaining_energy)))

        if remaining_mass < min_mass:
            break

    return results

neutron_flux = 10e14  # Neutrons per second 1e14
initial_mass = 1  # kg

reaction_results = simulate_nuclear_reaction_over_time(neutron_flux, initial_mass)

def create_values(neutron_flux_min, neutron_flux_max, neutron_flux_number_of_step, mass_min, mass_max, mass__number_of_step):
    max_tests = 1000
    results = []

    neutron_flux_step = (neutron_flux_max - neutron_flux_min)/neutron_flux_number_of_step
    mass_step = (mass_max - mass_min)/mass__number_of_step

    neutron_flux_values = [neutron_flux_min]
    mass_values = [mass_min]

    for i in range(1,neutron_flux_number_of_step):
        neutron_flux_values.append(i * neutron_flux_step + neutron_flux_min)
    neutron_flux_values.append(neutron_flux_max)
    
    for i in range (1,mass__number_of_step):
        mass_values.append(i * mass_step + mass_min)
    mass_values.append(mass_max)

    num_tests = min(neutron_flux_number_of_step * mass__number_of_step, max_tests)
    tests = num_tests

    for flux in neutron_flux_values:
        for mass in mass_values:
            result=[]
            if num_tests <= 0:
                break

            result_nuclear_reaction = list(simulate_nuclear_reaction_over_time(flux, mass))
            for i in range(0, len(result_nuclear_reaction)):
                result.append(list(tuple([tests-num_tests+1])+tuple([flux])+tuple([mass])+result_nuclear_reaction[i]))
            results.append(result)
            num_tests -= 1

    return results

def write_data(data, file_name):
    lines = []

    for sub_list in data:
        for sous_liste in sub_list:
            lines.append(sous_liste)

    df = pd.DataFrame(lines)

    df.to_excel(file_name, index=False, header=False)

data = create_values(1, 10e14, 5, 1, 60, 5)
write_data(data, "data.xlsx")
