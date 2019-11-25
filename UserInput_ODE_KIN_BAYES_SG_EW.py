import numpy as np

#####Temperature Programmed Reaction Settings#####
TPR = True #Set to false if doing an isothermal experiment.

#Need to define beta directly, or define dt and dT.
dT = 0.77 #Set this to 0 for an isothermal experiment.
dt = 0.385
beta_dTdt = dt/dT #This beta is heating rate. This will be set to 0 if somebody sets TPR to false. Not to be confused with 1/(T*k_b) which is often also called beta. User can put beta in manually.

T_0 = 152.96 #this is the starting temperature.

#####Experimental Data Input Files#####
Filename = 'ExperimentalDataAcetaldehydeTPDCeO2111MullinsTruncatedLargerErrors.csv'

#####Chemical Kinetic Model Input Files#####
parameterNamesAndMathTypeExpressionsDict = {'Ea_1':r'$E_{a1}$','Ea_2':r'$E_{a2}$','log_A1':r'$log(A_{1})$','log_A2':r'$log(A_{2})$','gamma1':r'$\gamma_{1}$','gamma2':r'$\gamma_{2}$'}

#####Chemical Kinetic Model Initial Concentrations#####
initial_concentrations_dict = {}
initial_concentrations_array = [0.5, 0.5]


#####Bayesian Probability Parameters#####
verbose = True
mu_prior = np.array([41.5, 41.5, 13.0, 13.0, 0.1, 0.1]) # Ea1_mean, Ea2_mean, log_A1_mean, log_A2_mean, gamma_1_mean, gamma_2_mean
cov_prior = np.array([[20.0, 0., 0., 0., 0., 0.],
                          [0., 20.0, 0., 0., 0., 0.],
                          [0., 0., 13.0, 0., 0., 0.],
                          [0., 0., 0., 13.0, 0., 0.],
                          [0., 0., 0., 0., 0.1, 0.],
                          [0., 0., 0., 0., 0., 0.1]])


						  
######MCMC settings:#####
mcmc = True 
mcmc_length = 1000
mcmc_burn_in = 100 

######gridSamplingSettings#####
gridSampling = False


    