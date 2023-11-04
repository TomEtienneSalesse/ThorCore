from Model.thermodynamic_formulas import ThermodynamicFormulas
import math

class PostReactorThermodynamics:

    #This function is used to represent the heat that goes from the reactor the the liquid around it

    def temperature_liquid_1(energy_per_second, t, thermic_capacity_liquid_1, mass_liquid_1, energy_loss_containing_liquid_1, liquid_1_temp):
        energy = energy_per_second * t
        total_energy_loss = energy_loss_containing_liquid_1 * t

        final_liquid_1_temp = liquid_1_temp + ThermodynamicFormulas.temperature_energy_mass(energy, thermic_capacity_liquid_1, mass_liquid_1) - ThermodynamicFormulas.temperature_energy_mass(total_energy_loss, thermic_capacity_liquid_1, mass_liquid_1)

        return final_liquid_1_temp

    #This function is used to represent where the heat is transmited : to the containing and to the 2 circuit with the 2nd liquid

    def transmitted_energies(liquid_1_temp, liquid_2_temp, ext_temp, thermic_capacity_containing, containing_mass, containing_surface, containing_conductivity, thermic_capacity_liquid_2, mass_liquid_2, contact_surface_liquid_1_2, thinkness, material_conductivity):
        temp_diff_containing = liquid_1_temp - ext_temp
        energy_loss_containing = ThermodynamicFormulas.energy_temperature_mass(temp_diff_containing, thermic_capacity_containing, containing_mass) + containing_conductivity * containing_surface * temp_diff_containing

        transmited_energy_liquid_2 = ThermodynamicFormulas.transmit_energy_throught_contact_surface(liquid_1_temp, liquid_2_temp, contact_surface_liquid_1_2, thinkness, material_conductivity)

        return energy_loss_containing, transmited_energy_liquid_2