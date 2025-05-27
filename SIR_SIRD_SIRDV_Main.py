#-----------------------------------------------------------------------------------------------------------------------
# Name: Caspar Lu
# Date: 04/30/2025
#-----------------------------------------------------------------------------------------------------------------------
import matplotlib.pyplot as plt
import numpy as np
import LU_SIR_SIRD_SIRDV_Functions as sir
#import functions module

#=========================================================================================
# Get user input
#=========================================================================================
#Ask user "Do you want to simulate the SIR, SIRD or SIRDV model?" & assign their input to the variable MODEL_CHOICE

MODEL_CHOICE = input("Do you want to simulate the SIR, SIRD or SIRDV model?").strip().upper()

if MODEL_CHOICE == "SIR":
    BETA = float(input("What is the infection rate you want to simulate?"))
    GAMMA = float(input("What is the recovery rate you want to simulate?"))
    DAYS = int(input("How many days do you want to simulate the disease outbreak?"))
    DAY0_INDV = input("Give me a list of 3 numbers (Susceptible, Infected, Recovered at day 0)):").split(",")
    S_0 = float(DAY0_INDV[0])
    I_0 = float(DAY0_INDV[1])
    R_0 = float(DAY0_INDV[2])

elif MODEL_CHOICE == "SIRD":
    BETA = float(input("What is the infection rate you want to simulate?"))
    GAMMA = float(input("What is the recovery rate you want to simulate?"))
    DAYS = int(input("How many days do you want to simulate the disease outbreak?"))
    DAY0_INDV = input("Give me a list of 3 numbers (Susceptible, Infected, Recovered at day 0)):").split(",")
    S_0 = float(DAY0_INDV[0])
    I_0 = float(DAY0_INDV[1])
    R_0 = float(DAY0_INDV[2])
    MU = float(input("What is the death rate from the disease that you want to simulate?"))

else:
    BETA = float(input("What is the infection rate you want to simulate?"))
    GAMMA = float(input("What is the recovery rate you want to simulate?"))
    DAYS = int(input("How many days do you want to simulate the disease outbreak?"))
    DAY0_INDV = input("Give me a list of 3 numbers (Susceptible, Infected, Recovered at day 0)):").split(",")
    S_0 = float(DAY0_INDV[0])
    I_0 = float(DAY0_INDV[1])
    R_0 = float(DAY0_INDV[2])
    MU = float(input("What is the death rate from the disease that you want to simulate?"))
    VAC_RATE = float(input("What is the vaccination rate you want to simulate?"))

#Ask user relevant questions based on the model they chose and store the information in variables.

    # If the user requested a SIR model, ask them 4 questions:
        #"What is the infection rate you want to simulate?" Assign this user input to the variable BETA
        #"What is the recovery rate you want to simulate?" Assign this user input to the variable GAMMA
        #"How many days do you want to simulate the disease outbreak?" Assign this user input to the variable DAYS
        #"Give me a list of 3 numbers: the # of susceptible, # of infected and # of recovered individuals at day 0."
        # Assign the list the user inputted to the variable DAY0_INDV

    # If the user requested a SIRD model, ask the same questions as above but also:
        #"What is the death rate from the disease that you want to simulate?" Assign this user input to the variable MU

    #If the user requested a SIRDV model, ask the same questions as above but also:
        #"What is the vaccination rate you want to simulate?" Assign this user input to the variable VAC_RATE

# Note: Make sure you convert all the user input numbers to floats!

#=========================================================================================
# Run default simulation and generate plot. Save the plot as png file called
# DefaultSIR_N1000_100Days_.4,.035.png. The .4, .035 are the default infection and recovery rates
#=========================================================================================
#Call the run_sim function to run the default SIR Model simulation, save the arrays returned by the function
# as Sim_S, Sim_I, Sim_R, Sim_D, Sim_V
Sim_S, Sim_I, Sim_R, Sim_D, Sim_V = sir.run_sim()

# Create a plot for this default simulation (SIR Model) and make sure it matches the sample output
# I've given you the code below. If you'd like, you can use Seaborn and tweak the plot the way you'd like.
t = np.arange(0, 100) #array of time points (0 to 100 days)
plt.figure(figsize=(10,6))
plt.plot(t, Sim_S, label="Susceptible")
plt.plot(t, Sim_I, label="Infected")
plt.plot(t, Sim_R, label="Recovered")
plt.xlabel("Days \n Simulation Parameters: S=997, I=3, Beta = .4, Gamma = .035., Mu = 0.005, Vac Rate = 0.05")
plt.ylabel("Number of People")
plt.title("Default SIR Model (N=1000, 100 Days)")
plt.legend()
plt.grid(True)
plt.savefig("DefaultSIR_N1000_100Days_.4,.035.png")
plt.show() #Make sure to do plt.savefig before you type plt.show() otherwise, the plot will be empty

#=========================================================================================
# Run the simulation the user wants and generate plot. Save the plot as a png file with a name that includes the
# name of the model the user specified, the population N (this is S+I+R or S+I+R+V) and
# the rates (infection, recovery, and if relevant, vaccination and/or death rate)

#Example: SIRD_N1000_100Days_Rates.4,.035,.005.png
#(if the user requested a SIRD model of 100 days for 1000 people with infection,recovery & death rates of .4,.035,.005)
#Hint: use f-strings!
#=========================================================================================
#Call the run_sim function to run the user's requested simulation & save the arrays returned by the function
# as Sim_S, Sim_I, Sim_R, Sim_D, Sim_V
Sim_S, Sim_I, Sim_R, Sim_D, Sim_V = sir.run_sim(S_0 = S_0, I_0 = I_0, R_0 = R_0, beta = BETA, gamma = GAMMA, mu = MU, 
                                                vac_rate = VAC_RATE, days = DAYS, model_choice = MODEL_CHOICE)

t = np.arange(0, 100) #array of time points (0 to 100 days)
plt.figure(figsize=(10,6))
plt.plot(t, Sim_S, label="Susceptible")
plt.plot(t, Sim_I, label="Infected")
plt.plot(t, Sim_R, label="Recovered")
plt.plot(t, Sim_D, label="Deceased")
plt.plot(t, Sim_V, label="Vaccinated")
plt.xlabel("Days \n Simulation Parameters: S=997, I=3, Beta = .4, Gamma = .035., Mu = 0.005, Vac Rate = 0.05")
plt.ylabel("Number of People")
plt.title("SIRDV Model (N=1000, 100 Days)")
plt.legend()
plt.grid(True)
plt.savefig(f"{MODEL_CHOICE}_N{S_0+I_0+R_0}_{DAYS}Days_{BETA},{GAMMA},{MU},{VAC_RATE}.png")
plt.show() #Make sure to do plt.savefig before you type plt.show() otherwise, the plot will be empty

#=========================================================================================


