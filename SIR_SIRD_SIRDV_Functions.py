#-----------------------------------------------------------------------------------------------------------------------
# Name: Caspar Lu
# Date: 04/30/2025
#-----------------------------------------------------------------------------------------------------------------------
""" This module contains functions to simulate and visualize the spread of an infectious disease """
import turtledemo
from turtledemo import clock
import numpy as np
#====================================================================================================
# SIR Model differential equations Helper Function
#====================================================================================================
def sir_model(S_t, I_t, R_t, beta, gamma):
    """'
    This function takes in a specified infection rate (beta), recovery rate (gamma) and the
    current number of susceptible (S_t), infected (I_t) and recovered individuals (R_t) for a given day.
    It returns the rate of change in the number of susceptible individuals (dS/dt), change in the number
    of infected individuals (dI/dt), and change in the number of recovered individuals (dR/dt) for that day.
    """
    S_t = float(S_t)
    I_t = float(I_t)
    R_t = float(R_t)
    dS_dt = -beta*((S_t*I_t)/(S_t+I_t+R_t)) #Change in number of susceptible individuals at day t
    dI_dt = beta*((S_t*I_t)/(S_t+I_t+R_t)) - gamma*I_t #Change in number of infected people at day t
    dR_dt = gamma*I_t #Change in number of recovered individuals at day t
    return dS_dt, dI_dt, dR_dt

#Note: Instead of using a fixed N, you can use S+I+R because N=S+I+R. (When doing the sird_model, you have to do this
# because N will change since people die. So it's best not to feed in a fixed N and use S+I+R).

#====================================================================================================
# SIRD Model differential equations Helper Function (5 points)
#====================================================================================================
def sird_model(S_t, I_t, R_t, beta, gamma, mu):
    """'
   This function includes specific infection rate (beta), recovery rate (gamma) and the current number of susceptible (S_t), 
   infected (I_t), recovered individuals (R_t), and death rate (mu) for a given day. 
   It returns the rate of change in the number of susceptible individuals (dS/dt), change in the number
   of infected individuals (dI/dt), change in the number of recovered individuals (dR/dt), and change in the number of individuals deceased 
   for that day. 
    """
    S_t = float(S_t)
    I_t = float(I_t)
    R_t = float(R_t)
    dS_dt = -beta*((S_t*I_t)/(S_t+I_t+R_t)) #Change in number of susceptible individuals at day t
    dI_dt = beta*((S_t*I_t)/(S_t+I_t+R_t)) - gamma*I_t - mu*I_t #Change of number of infection individuals at day t 
    dR_dt = gamma*I_t #Change of number of recovered individuals at day t
    dD_dt = mu*I_t #Change of number of death individuals at day t
    return dS_dt, dI_dt, dR_dt, dD_dt

#Note: N = S_t + I_t + R_t

#====================================================================================================
# SIRDV Model differential equations Helper Function
#====================================================================================================
def sirdv_model(S_t, I_t, R_t,V_t, beta, gamma, mu, vac_rate):
    """'
   This function includes specific infection rate (beta), recovery rate (gamma) and the current number of susceptible (S_t), 
   infected (I_t), recovered individuals (R_t), death rate (mu), and vaccination rate (vac_rate) for a given day. 
   It returns the rate of change in the number of susceptible individuals (dS/dt), change in the number
   of infected individuals (dI/dt), change in the number of recovered individuals (dR/dt), and change in the number of individuals deceased 
   for that day. 
    """
    S_t = float(S_t)
    I_t = float(I_t)
    R_t = float(R_t)
    dS_dt = -beta*((S_t*I_t)/(S_t+I_t+R_t+V_t)) - vac_rate*S_t #Change in number of susceptible individuals at day t
    dI_dt = beta*((S_t*I_t)/(S_t+I_t+R_t+V_t)) - gamma*I_t - mu*I_t #Change of number of infection individuals at day t 
    dR_dt = gamma*I_t #Change of number of recovered individuals at day t
    dD_dt = mu*I_t #Change of number of death individuals at day t
    dV_dt = vac_rate*S_t #Change of number of vaccinated individuals at day t
    return dS_dt, dI_dt, dR_dt, dD_dt, dV_dt

#Note for this model: N = S_t + I_t + R_t + V_t
#====================================================================================================
# Function to Run the Whole Simulation based on the model ("SIR", "SIRD" or "SIRDV") the user specifies
#====================================================================================================

def run_sim(S_0 = 997, I_0 = 3, R_0 = 0, D_0 = 0, V_0 = 0, beta = .4, gamma = .035, mu = 0, vac_rate = 0, days = 100, model_choice = "SIR"):
    """'
   This function includes infection rate (beta), recovery rate (gamma) and the number of susceptible (S_0), 
   infected (I_0), recovered individuals (R_0), vaccinated individuals (V_0), death rate (mu), and vaccination rate (vac_rate) for day 0. 
   It returns the rate of change in the number of susceptible individuals (dS/dt), change in the number of infected individuals (dI/dt), 
   change in the number of recovered individuals (dR/dt), and change in the number of individuals deceased for that day. 
    """
    S = np.zeros(days)
    I = np.zeros(days)
    R = np.zeros(days)
    D = np.zeros(days)
    V = np.zeros(days)

    S[0] = S_0
    I[0] = I_0
    R[0] = R_0
    D[0] = D_0
    V[0] = V_0
    # -----------------------------------------------------------------------
    # Initialize arrays of zeroes with length "days" to keep track of the S, I, R, D and V individuals for each day

    # Set initial number of susceptible (S), infected (I), recovered (R) people on day 0 in the S, I, R arrays
    # based on the parameters S_0, I_0, R_0
    
    #-----------------------------------------------------------------------
    # Note: Deceased and vaccinated individuals day 0 will be 0, so no need to assign D[0] or V[0] to anything,
    # as the first element of your initialized array is already 0
    


    # -----------------------------------------------------------------------
    # Simulate the number of susceptible (S), infected (I), recovered (R) and if relevant,
    # the deceased (D) & vaccinated (V) people for the specified number of days
    # -----------------------------------------------------------------------
    for day in range(1, days): #For each day...
    #Get dS, dI, dR and if relevant, dD and dV to count up the number of S,I,R,D and V people for that day
        #Get rates of change (dS, dI, dR, & if needed, dD, dV)
        if model_choice == "SIR":
            dS, dI, dR = sir_model(S_t=S[day - 1], I_t=I[day - 1], R_t=R[day - 1], beta=beta, gamma=gamma)
            dV = dD = 0 #Vaccination and death rates not considered in SIR model so the "change" is 0
        elif model_choice == "SIRD":
            dS, dI, dR, dD = sird_model(S_t=S[day - 1], I_t=I[day - 1], R_t=R[day - 1], beta=beta, gamma=gamma, mu=mu)
            dV = 0
        else:
            dS, dI, dR, dD, dV = sirdv_model(S_t=S[day - 1], I_t=I[day - 1], R_t=R[day - 1], V_t=V[day-1], beta=beta, gamma=gamma, vac_rate=vac_rate, mu=mu)

        S[day] = S[day - 1] + dS
        I[day] = I[day - 1] + dI
        R[day] = R[day - 1] + dR
        D[day] = D[day - 1] + dD
        V[day] = V[day - 1] + dV
    
    return S, I, R, D, V

        #elif model_choice == ....else...

        #Fill in the arrays w/ # of indv for that day based on the calculated dS, dI, dR, dD, dV
       #and the # of indv from the day before (day -1).
       # Example: S[day] = S[day-1] + dS

    # -----------------------------------------------------------------------
    # Return the final arrays S, I, R, D, V
    # -----------------------------------------------------------------------



