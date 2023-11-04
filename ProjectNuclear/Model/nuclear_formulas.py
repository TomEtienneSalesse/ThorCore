import math
import numpy as np

class NuclearFormulas:

    #E = mc²
    #Einstein mass energy formula used to convert mass in energy in a nuclear reaction
    #m -> kg ; E -> J ; q -> J ; c -> m/s
    def einstein_mass_energy(m):
        c = 299792458.0
        E = m * (c)**2
        return E
    
    def einstein_energy_mass(E):
        c = 299792458.0
        m = E/(c)**2
        return m
    
    def einstein_nuclear_reaction(m1, m2):
        c = 299792458.0
        q = (m1 - m2) * (c)**2
        return q
    
    #N(t)=N0​e(−λt)
    #Radioactive decay formula, describes the decay rate of a radioactive sample over time
    #N0 -> number of nuclei at start ; Nt number of nuclei at t ; t -> s ; decay_constant -> s^-1

    def radioactive_consumption(N0, decay_constant , t):
        Nt = N0 * math.exp(-decay_constant  * (t*3600*24*365))
        return Nt
    
    #λ=​ln(2) / T1/2​
    #The half life is specific to each isotope and has to be entered manualy
    #half_life -> s

    def decay_constant_from_half_life(half_life):
        return math.log(2) / half_life
    
    #σ= k⋅Z1​⋅Z2​⋅e2​ / 4πε0​E
    #Calculate the cross section for scattering
    #Z1 -> atomic number of particle 1 ; Z2 -> atomic number of particle 2 ; energy -> energy of incident particle J
    #cross section -> m² ; k -> coulomb constant Nm²C^(-2) ; e -> elementary charge C ; epsilon_0 vacuum permittivity F/m ; pi

    def cross_section_for_scattering(Z1, Z2, energy):
        k = 8.9875517873681764e9
        e = 1.602176634e-19
        epsilon_0 = 8.854187817e-12
        pi = math.pi
        return (k * Z1 * Z2 * (e**2)) / (4 * pi * epsilon_0 * energy)
    
    #Calculate the number of nuclei
    #nuclei_mass -> kg : mass -> kg

    def nuclei_number(mass):
        nuclei_mass = 1.675e-27
        return mass / nuclei_mass
    
    #Calculate the number of transformed nuclei to another kind of nuclei
    #no units, conversion_rate is set by the transformation from a nuclei to another

    def convertion(initial_nuclei, conversion_rate):
        return initial_nuclei * conversion_rate
    
    def remaining_nuclei_mass(neutron_flux, mass, time):
        neutron_energy = NuclearFormulas.einstein_mass_energy(1.675e-27)
        cross_section = NuclearFormulas.cross_section_for_scattering(1, 90, neutron_energy)
        reactions_per_second = cross_section * neutron_flux
        consumption = 1 / reactions_per_second
        nuclei_to_transform = NuclearFormulas.nuclei_number(mass)
        remaining_nuclei = NuclearFormulas.radioactive_consumption(nuclei_to_transform, consumption , time)
        nuclei_mass = 1.675e-27  # kg (mass of a nucleus)
        remaining_mass = nuclei_mass * remaining_nuclei

        return remaining_nuclei, remaining_mass