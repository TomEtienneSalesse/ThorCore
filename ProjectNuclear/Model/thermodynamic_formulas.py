import math

class ThermodynamicFormulas:

    #T = E / c*m
    #The temperature depends on the energy transmited divided by the product of thermic capacity and mass
    #E -> J, C -> J.kg-1, M -> kg

    def temperature_energy_mass(E, c, m):
        return E/ (c*m)
    
    def energy_temperature_mass(T, c, m):
        return T*c*m
    
    #Q is the transfer heat rate, the thinkness is in meters

    def transmit_energy_throught_contact_surface(liquid_1_temp, liquid_2_temp, surface, thinkness, material_conductivity):
        Q = material_conductivity/thinkness
        return Q * surface * (liquid_1_temp-liquid_2_temp)
