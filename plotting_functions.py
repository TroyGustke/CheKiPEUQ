import sys
sys.path.insert(0, '/mumpce/')
import mumpce.Project as mumpceProject
import mumpce.solution as mumpceSolution
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import cm #EAW 2020/01/07
import copy

class plotting_functions_class():
    def __init__(self, UserInput, samples = False): # The plots require samples.  Other plot settings are probably plotting-package specific.
        self.UserInput = UserInput
        if not samples:
            print("Warning: Pass in the 'samples' keyword argument containing a numpy array of samples to plot.")
    
    def mu_and_cov_from_samples(self):
        mu = np.mean(self.samples, axis = 0)
        cov = np.cov(self.samples,rowvar=False)
        return mu, cov

    def mumpce_plots(self, model_parameter_info = {}, active_parameters = [], pairs_of_parameter_indices = [], posterior_mu_vector = 0, posterior_cov_matrix = 0, prior_mu_vector = 0, prior_cov_matrix = 0, contour_settings_custom = {'figure_name','fontsize','num_y_ticks','num_x_ticks','colormap_posterior_customized','colormap_prior_customized','contours_normalized','colorbars'}): # Pass empty keyword arguments for important parameters.  That way, warnings may be issued if they are not set.  There is not really a good default for these keyword arguments.  They depend entirely on the nature of the data being plotted.
        mumpceProjectObject = mumpceProject.Project() # A mumpce project object must be created.
        if len(model_parameter_info) == 0:
            print("Pass the 'model_parameter_info' argument to the mumpce_plots function.")
            model_parameter_info = np.array([{'parameter_number': 0, 'parameter_name': 'Parameter 0'},{'parameter_number': 1, 'parameter_name': 'Parameter 1'}])
        if len(active_parameters) == 0:
            print("Pass the 'active_parameters' argument to the mumpce_plots function.")
            active_parameters = np.array([0, 1]) 
        mumpceProjectObject.active_parameters = active_parameters
        #if len(pairs_of_parameter_indices) == 0:
        #    print("Pass the 'pairs_of_parameter_indices' argument to the mumpce_plots function.")
        #    mumpceProjectObject.pairsOfParameterIndices = [[0, 1]]
        #else:
        mumpceProjectObject.pairsOfParameterIndices = pairs_of_parameter_indices
        #if not posterior_mu_vector == 0:
        #    print("Pass the 'posterior_mu_vector' argument to the mumpce_plots function.")
        #    posterior_mu_vector = np.array([-0.58888733,1.1200355])
        #if not posterior_cov_matrix == 0:
        #    print("Pass the 'posterior_cov_matrix' argument to the mumpce_plots function.")
        #    posterior_cov_matrix = np.array([[ 0.0148872,-0.01894579],[-0.01894579,0.04284732]])
        #if not prior_mu_vector == 0:
        #    print("Pass the 'prior_mu_vector' argument to the mumpce_plots functions.")
        #    prior_cov_matrix = np.array([-0.98888733,0.8200355])
        #if not prior_cov_matrix == 0:
        #    prior_cov_matrix = 10*posterior_cov_matrix
        #    print("Pass the 'prior_cov_matrix' argument to the mumpce_plots functions.")
        mumpceProjectObject.model_parameter_info = model_parameter_info
        mumpceSolutionsObject = mumpceSolution.Solution(posterior_mu_vector, posterior_cov_matrix, initial_x=prior_mu_vector, initial_covariance=prior_cov_matrix)
        mumpceProjectObject.solution = mumpceSolutionsObject
        #if hasattr(UserInput,'figure_name'):
        #    contour_settings_custom['figure_name']=UserInput.figure_name
        #else:
        #    contour_settings_custom['figure_name']='mumpce_plots_04'
        #if hasattr(UserInput,'fontsize'):
        #    contour_settings_custom['fontsize'] = UserInput.fontsize        
        #else:
        #    contour_settings_custom['fontsize'] = 'auto'
        #if hasattr(UserInput,'num_y_ticks'):
        #    contour_settings_custom['num_y_ticks'] = UserInput.num_y_ticks
        #else:
        #    contour_settings_custom['num_y_ticks'] = 'auto'
        #if hasattr(UserInput,'num_x_ticks'):
        #    contour_settings_custom['num_x_ticks'] = UserInput.num_x_ticks
        #else:
        #    contour_settings_custom['num_x_ticks'] = 'auto'
        #if hasattr(UserInput,'colormap_posterior_customized'):
        #    contour_settings_custom['colormap_posterior_customized'] = UserInput.colormap_posterior_customized
        #else:
        #    contour_settings_custom['colormap_posterior_customized'] = "Oranges"
        #if hasattr(UserInput,'colormap_prior_customized'):
        #    contour_settings_custom['colormap_prior_customized'] = UserInput.colormap_prior_customized
        #else:
        #    contour_settings_custom['colormap_prior_customized'] = "Greens"
        #if hasattr(UserInput,'contours_normalized'):
        #    contour_settings_custom['contours_normalized'] = UserInput.contours_normalized
        #else:
        #    contour_settings_custom['contours_normalized'] = False
        #if hasattr(UserInput,'center_on'):
        #    contour_settings_custom['center_on'] = UserInput.center_on
        #else:
        #    contour_settings_custom['center_on'] = 'prior'
        #if hasattr(UserInput,'colorbars'):
        #    contour_settings_custom['colorbars'] = UserInput.colorbars
        #else:
        #    contour_settings_custom['colorbars'] = True
        mumpceProjectObject.plot_pdfs(mumpceProjectObject.pairsOfParameterIndices, contour_settings_custom = contour_settings_custom)


    def seaborn_scatterplot_matrix(self):
        #fig0, ax0 = plt.subplots()
        #if UserInput.verbose:
        #    print(np.mean(rate_tot_array,axis = 0))
        #ax0.plot(np.array(experiments_df['AcH - T']),np.mean(rate_tot_array,axis = 0), 'r')
        #ax0.plot(np.array(experiments_df['AcH - T']),np.array(experiments_df['AcHBackgroundSubtracted'])/2000,'g')
        #ax0.set_ylim([0.00, 0.025])
        #ax0.set_xlabel('T (K)')
        #ax0.set_ylabel(r'$rate (s^{-1})$')
        #ax0.legend(['model posterior', 'experiments'])
        #fig0.tight_layout()
        #fig0.savefig('tprposterior.png', dpi=220)
        #posterior_df = pd.DataFrame(samples,columns=[UserInput.parameterNamesAndMathTypeExpressionsDict[x] for x in UserInput.parameterNamesList])
        #pd.plotting.scatter_matrix(posterior_df)
        #plt.savefig('scatter_matrix_posterior.png',dpi=220)
        return

    def rate_tot_plot(self):
        return

def sampledParameterHistogramMaker(parameterSamples, parameterName,parameterNamesAndMathTypeExpressionsDict, sampledParameterFiguresDictionary, sampledParameterAxesDictionary):
        parameterIndex = list(parameterNamesAndMathTypeExpressionsDict).index(parameterName)
        sampledParameterFiguresDictionary['parameterName'], sampledParameterAxesDictionary['parameterName'] = plt.subplots()   #making plt objects    
        sampledParameterAxesDictionary['parameterName'].hist(parameterSamples[:,parameterIndex]) #filling the object with data
        #setting the labels etc. and then exporting.
        sampledParameterAxesDictionary['parameterName'].set_ylabel('frequency')
        sampledParameterAxesDictionary['parameterName'].set_xlabel(parameterNamesAndMathTypeExpressionsDict[parameterName])
        sampledParameterFiguresDictionary['parameterName'].tight_layout()
        sampledParameterFiguresDictionary['parameterName'].savefig(parameterName+'.png', dpi=220)
        #The above block makes code kind of like this in a dynamic fashion. Since we know how many we will need, a dictionary is used to avoid the need for 'exec' statements when making new parameters.
        # fig2, ax2 = plt.subplots()
        # ax2.hist(samples[:,1])
        # ax2.set_ylabel('frequency')
        # ax2.set_xlabel(r'$E_{a2}$')
        # fig2.tight_layout()
        # fig2.savefig('Ea2.png', dpi=220)

    #Make histograms for each parameter. Need to make some dictionaries where relevant objects will be stored.
def makeHistogramsForEachParameter(parameterSamples,parameterNamesAndMathTypeExpressionsDict):
    sampledParameterFiguresDictionary = copy.deepcopy(parameterNamesAndMathTypeExpressionsDict) #This must be a deep copy to perserve original.
    sampledParameterAxesDictionary = copy.deepcopy(parameterNamesAndMathTypeExpressionsDict) #This must be a deep copy to preserve original.
    for key in parameterNamesAndMathTypeExpressionsDict:
        parameterName = key
        sampledParameterHistogramMaker(parameterSamples, parameterName,parameterNamesAndMathTypeExpressionsDict, sampledParameterFiguresDictionary, sampledParameterAxesDictionary)        

def createSimulatedResponsesPlot(x_values, listOfYArrays, plot_settings=[]):
    #First put some defaults in if not already defined.
    if 'x_label' not in plot_settings: plot_settings['x_label'] = ''
    if 'y_label' not in plot_settings: plot_settings['y_label'] = ''
    if 'legendLabels' not in plot_settings: plot_settings['legendLabels'] = ''
    if 'figure_name' not in plot_settings: plot_settings['figure_name'] = 'simulatedResponsesPlot'
    if 'dpi' not in plot_settings: plot_settings['dpi']=220          
    fig0, ax0 = plt.subplots()
    ax0.set_xlabel(plot_settings['x_label'])
    ax0.set_ylabel(plot_settings['y_label']) #TODO: THis is not yet generalized (will be a function)
    if 'y_range' in plot_settings: ax0.set_ylim(plot_settings['y_range'] )
    if len(listOfYArrays) == 3:
        for seriesIndex in range(len(listOfYArrays)):
            ax0.plot(x_values,listOfYArrays[0],'g')
            ax0.plot(x_values,listOfYArrays[1], 'b')
            ax0.plot(x_values,listOfYArrays[2], 'r') 
    elif len(listOfYArrays) == 4:
        for seriesIndex in range(len(listOfYArrays)):
            ax0.plot(x_values,listOfYArrays[0],'green')
            ax0.plot(x_values,listOfYArrays[1], 'b')
            ax0.plot(x_values,listOfYArrays[2], 'red') 
            ax0.plot(x_values,listOfYArrays[3], 'black') 
    else:
        for seriesIndex in range(len(listOfYArrays)):
            ax0.plot(x_values,listOfYArrays[seriesIndex])
    ax0.legend(plot_settings['legendLabels']) #legends must be after plots are made.
    fig0.tight_layout()
    fig0.savefig(plot_settings['figure_name'] + '.png', dpi=plot_settings['dpi'])
    return fig0
