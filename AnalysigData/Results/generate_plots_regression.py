import matplotlib.pyplot as plt

def generate_plots(test_data, test_number, coef_NN, intercept_NN, coef_mass, intercept_mass, coef_energy, intercept_energy):
    neutron_flux = round(test_data[1].values[0], 2)
    initial_mass = round(test_data[2].values[0], 2)
    time = test_data[3]
    NN = test_data[4]
    mass = test_data[5]
    energy = test_data[6]

    plt.figure(figsize=(10, 5))
    plt.plot(time, NN, 'o', label='Number of nuclei')
    plt.plot(time, coef_NN[0] * time + intercept_NN, color='red', label='Linear Regression')
    plt.xlabel('Time')
    plt.ylabel('Number of nuclei')
    plt.title(f'Number of nuclei on test number {test_number} : {neutron_flux}Neutron/s with {initial_mass}kg of thorium')
    plt.legend()
    plt.savefig(f'C:/Users/Utilisateur/Desktop/Travail/Python/ThorCore/AnalysigData/Results/plots/test_{test_number}_NN.png')
    plt.close()

    plt.figure(figsize=(10, 5))
    plt.plot(time, mass, 'o', label='Mass kg', color='orange')
    plt.plot(time, coef_mass[0] * time + intercept_mass, color='red', label='Linear Regression')
    plt.xlabel('Time')
    plt.ylabel('Mass kg')
    plt.title(f'Thorium mass on test number {test_number} : {neutron_flux}Neutron/s with {initial_mass}kg of thorium at start')
    plt.legend()
    plt.savefig(f'/Users/Utilisateur/Desktop/Travail/Python/ThorCore/AnalysigData/Results/plots/test_{test_number}_mass.png')
    plt.close()

    plt.figure(figsize=(10, 5))
    plt.plot(time, energy, 'o', label='Energy J', color='green')
    plt.plot(time, coef_energy[0] * time + intercept_energy, color='red', label='Linear Regression')
    plt.xlabel('Time')
    plt.ylabel('Energy J')
    plt.title(f'Energy on test number {test_number} : {neutron_flux}Neutron/s with {initial_mass}kg of thorium')
    plt.legend()
    plt.savefig(f'/Users/Utilisateur/Desktop/Travail/Python/ThorCore/AnalysigData/Results/plots/test_{test_number}_energy.png')
    plt.close()