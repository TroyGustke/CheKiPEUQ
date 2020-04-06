import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import sys; sys.path.append('../../');  import CheKiPEUQ as CKPQ
import CheKiPEUQ.UserInput as UserInput

if __name__ == "__main__":
    
    observed_data_Filename = 'ExperimentalDataAcetaldehydeTPDCeO2111MullinsTruncatedConstantErrors.csv'
    
    import processing_function_chem_rxn as fun

    UserInput.responses['responses_observed'] = -3.912
    UserInput.responses['responses_observed_uncertainties'] = 1.0
    
    UserInput.simulated_response_plot_settings['x_label'] = r'$Temperature (K)$'
    UserInput.simulated_response_plot_settings['y_label'] = r'$ln(C_A)$'
    #UserInput.simulated_response_plot_settings['y_range'] = [0.00, 0.025] #optional.
    UserInput.simulated_response_plot_settings['figure_name'] = 'Posterior_Example11' #This creates the filename, also.

    UserInput.model['parameterNamesAndMathTypeExpressionsDict'] = {'delta_G':r'$\deltaG (eV)$'}
    UserInput.model['InputParameterPriorValues'] = [-0.15] # eV
    UserInput.model['InputParametersPriorValuesUncertainties'] = [0.1] #If user wants to use a prior with covariance, then this must be a 2D array/ list. To assume no covariance, a 1D  This is a standard deviation!
    UserInput.model['InputParameterInitialGuess'] = [-0.15] #This is where the mcmc chain will start.
    #InputParameterInitialValues = [41.5, 41.5, 13.0, 13.0, 0.1, 0.1] # Ea1_mean, Ea2_mean, log_A1_mean, log_A2_mean, gamma_1_mean, gamma_2_mean 
    
    #InputParametersInitialValuesUncertainties = [200, 200, 13, 13, 0.1, 0.1] #If user wants to use a prior with covariance, then this must be a 2D array/ list. To assume no covariance, a 1D array can be used.
    UserInput.model['simulateByInputParametersOnlyFunction'] = fun.delta_G_T_to_ln_CA #This must simulate with *only* the parameters listed above, and no other arguments.
    #UserInput.model['simulationOutputProcessingFunction'] = processing_functions_tpd_odeint.no_log_wrapper_func #Optional: a function to process what comes out of the simulation Function and then return an observable vector.
    
    UserInput.parameter_estimation_settings['verbose'] = False 
    UserInput.parameter_estimation_settings['checkPointFrequency'] = 100
    UserInput.parameter_estimation_settings['mcmc'] = True 
    UserInput.parameter_estimation_settings['mcmc_mode'] = 'unbiased'
    UserInput.parameter_estimation_settings['mcmc_random_seed'] = None #Normally set to None so that mcmc is set to be random. To get the same results repeatedly, such as for testing purposes, set the random seed to 0 or another integer for testing purposes.
    UserInput.parameter_estimation_settings['mcmc_burn_in'] = 100
    UserInput.parameter_estimation_settings['mcmc_length'] = 80100
    UserInput.parameter_estimation_settings['mcmc_relative_step_length'] = 0.05
    UserInput.parameter_estimation_settings['mcmc_modulate_accept_probability']  = 0 #Default value of 0. Changing this value sharpens or flattens the posterior. A value greater than 1 flattens the posterior by accepting low values more often. It can be useful when greater sampling is more important than accuracy. One way of using this feature is to try with a value of 0, then with the value equal to the number of priors for comparison, and then to gradually decrease this number as low as is useful (to minimize distortion of the result). A downside of changing changing this variable to greater than 1 is that it slows the the ascent to the maximum of the prior, so there is a balance in using it. In contrast, numbers increasingly less than one (such as 0.90 or 0.10) will speed up the ascent to the maximum of the posterior, but will also result in fewer points being retained.
    
    UserInput.parameter_pairs_for_contour_plots = [[0, 0]]
    UserInput.contour_settings_custom['contours_normalized'] = False
    UserInput.contour_settings_custom['figure_name'] = 'Mumpce_contour_plot_chem_rxn'
    #After making the UserInput, now we make a 'parameter_estimation' object from it.
    global T
    T = 298.15
    PE_object = CKPQ.parameter_estimation(UserInput)
    
    #Now we do parameter estimation.
    #PE_object.doGridSearch('getLogP', verbose = False)
    PE_object.doMetropolisHastings()
    #PE_object.doOptimizeNegLogP(method="BFGS", printOptimum=True, verbose=True)
    #[map_parameter_set, muap_parameter_set, stdap_parameter_set, evidence, info_gain, samples, samples_simulatedOutputs, logP] = PE_object.doMetropolisHastings()
    
    PE_object.createAllPlots() #This function calls each of the below functions.
#    PE_object.makeHistogramsForEachParameter()    
#    PE_object.makeSamplingScatterMatrixPlot()
#    PE_object.createSimulatedResponsesPlot()
    #TODO: call the mum_pce plotting objects, which will be PE_object.createContourGraphs() or something like that.
    fig, ax = plt.subplots()
    prior = np.random.normal(-0.15,0.1,80000)
    (density0,bins0,pathces0)=ax.hist([prior,PE_object.post_burn_in_samples.flatten()],bins=100,label=['prior','posterior'],density=True)
    ax.legend()
    ax.set_xlabel(r'$\Delta G (eV)$')
    ax.set_ylabel('Probability density')
    ax.set_title('Prior and Posterior Density Plot at T= 298 K')
    fig.savefig('prior_and_posterior_G_histogram.png', dpi=300)