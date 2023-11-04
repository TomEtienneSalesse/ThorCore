import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def generate_plots(test_data, test_number, coef_NN, intercept_NN, coef_mass, intercept_mass, coef_energy, intercept_energy,ARIMA_model_NN,rmse_NN,ARIMA_model_mass,rmse_mass,ARIMA_model_energy,rmse_energy,test_NN,test_mass,test_energy):
    neutron_flux = round(test_data[1].values[0], 2)
    initial_mass = round(test_data[2].values[0], 2)
    time = test_data[3]
    NN = test_data[4]
    mass = test_data[5]
    energy = test_data[6]

    ARIMA_model_NN=pd.Series(ARIMA_model_NN)
    ARIMA_model_mass=pd.Series(ARIMA_model_mass)
    ARIMA_model_energy=pd.Series(ARIMA_model_energy)
    ARIMA_time = time.iloc[-len(ARIMA_model_NN):]
    test_NN = pd.Series(test_NN)
    test_mass = pd.Series(test_mass)
    test_energy = pd.Series(test_energy)

    plt.figure(figsize=(10, 5))
    plt.subplot(2, 1, 1)
    plt.plot(time, NN, 'o', label='Number of nuclei')
    plt.plot(time, coef_NN[0] * time + intercept_NN, color='red', label='Linear Regression')
    plt.xlabel('Time')
    plt.ylabel('Number of nuclei')
    plt.title(f'Number of nuclei on test number {test_number} : {neutron_flux}Neutron/s with {initial_mass}kg of thorium')
    plt.legend()
    plt.subplot(2, 1, 2)
    plt.plot(ARIMA_time, test_NN, label='real values')
    plt.plot(ARIMA_time, ARIMA_model_NN, color='red', label=f'ARIMA rmse {rmse_NN}')
    plt.xlabel('Time')
    plt.ylabel('Number of nuclei')
    plt.title(f'ARIMA prediction of the last 1/3 of the reaction')
    plt.legend()
    plt.savefig(f'C:/Users/Utilisateur/Desktop/Travail/Python/ThorCore/AnalysigData/Results/plots/test_{test_number}_ARIMA_NN.png')
    plt.close()

    plt.figure(figsize=(10, 5))
    plt.subplot(2, 1, 1)
    plt.plot(time, mass, 'o', label='Mass kg', color='orange')
    plt.plot(time, coef_mass[0] * time + intercept_mass, color='red', label='Linear Regression')
    plt.xlabel('Time')
    plt.ylabel('Mass kg')
    plt.title(f'Thorium mass on test number {test_number} : {neutron_flux}Neutron/s with {initial_mass}kg of thorium at start')
    plt.legend()
    plt.subplot(2, 1, 2)
    plt.plot(ARIMA_time, test_mass, label='real values')
    plt.plot(ARIMA_time, ARIMA_model_mass, color='red', label=f'ARIMA rmse {rmse_mass}')
    plt.xlabel('Time')
    plt.ylabel('Mass kg')
    plt.title(f'ARIMA prediction of the last 1/3 of the reaction')
    plt.legend()
    plt.savefig(f'/Users/Utilisateur/Desktop/Travail/Python/ThorCore/AnalysigData/Results/plots/test_{test_number}_ARIMA_mass.png')
    plt.close()

    plt.figure(figsize=(10, 5))
    plt.plot(time, energy, 'o', label='Energy J', color='green')
    plt.plot(time, coef_energy[0] * time + intercept_energy, color='red', label='Linear Regression')
    plt.xlabel('Time')
    plt.ylabel('Energy J')
    plt.title(f'Energy on test number {test_number} : {neutron_flux}Neutron/s with {initial_mass}kg of thorium')
    plt.legend()
    plt.subplot(2, 1, 2)
    plt.plot(ARIMA_time, test_energy, label='real values')
    plt.plot(ARIMA_time, ARIMA_model_energy, color='red', label=f'ARIMA rmse {rmse_energy}')
    plt.xlabel('Time')
    plt.ylabel('Energy J')
    plt.title(f'ARIMA prediction of the last 1/3 of the reaction')
    plt.legend()
    plt.savefig(f'/Users/Utilisateur/Desktop/Travail/Python/ThorCore/AnalysigData/Results/plots/test_{test_number}_ARIMA_energy.png')
    plt.close()