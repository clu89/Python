#-----------------------------------------------------------------------------------------------------------------------
# Name: Caspar Lu
# Date: 04/30/2025
# BIOS 584 Assignment 4 Application 2 (AI GUICode SIRModel)

#-----------------------------------------------------------------------------------------------------------------------
## Import packages
import matplotlib.pyplot as plt
import numpy as np
import LU_SIR_SIRD_SIRDV_Functions as sir

import ipywidgets as widgets ## Create sliders, text boxes, and dropdowns 
from IPython.display import display, clear_output ## Dynamically update plots based on user input
#-----------------------------------------------------------------------------------------------------------------------
## Parameter input
model_choice = widgets.Dropdown(
    options=['SIR', 'SIRD', 'SIRDV'],
    description='Model:',
    value='SIR'
)

# Common sliders
beta_slider = widgets.FloatSlider(value=0.3, min=0.0, max=1.0, step=0.01, description='Beta (Infection Rate):')
gamma_slider = widgets.FloatSlider(value=0.1, min=0.0, max=1.0, step=0.01, description='Gamma (Recovery Rate):')
days_slider = widgets.IntSlider(value=100, min=1, max=365, step=1, description='Days:')

# Day 0 population text
day0_text = widgets.Text(
    value='990,10,0',
    description='Day 0 (S,I,R):',
    placeholder='e.g., 990,10,0'
)

# Additional sliders (for SIRD and SIRDV)
mu_slider = widgets.FloatSlider(value=0.01, min=0.0, max=0.1, step=0.001, description='Mu (Death Rate):')
vac_slider = widgets.FloatSlider(value=0.0, min=0.0, max=1.0, step=0.01, description='Vaccination Rate:')

# Button to run simulation
run_button = widgets.Button(description="Run Simulation", button_style='success')

# Display widgets
display(model_choice, beta_slider, gamma_slider, days_slider, day0_text, mu_slider, vac_slider, run_button)
#-----------------------------------------------------------------------------------------------------------------------
## Simulation run and plotting block
def run_simulation(button):
    clear_output(wait=True)  # Clear previous outputs (clean plot refresh)
    
    # Re-display widgets after clear
    display(model_choice, beta_slider, gamma_slider, days_slider, day0_text, mu_slider, vac_slider, run_button)
    
    # Read model choice
    model = model_choice.value
    
    # Read sliders/texts
    beta = beta_slider.value
    gamma = gamma_slider.value
    days = days_slider.value
    day0_list = [float(x) for x in day0_text.value.split(',')]
    S_0, I_0, R_0 = day0_list
    
    mu = mu_slider.value
    vac_rate = vac_slider.value
    
    # Call appropriate function based on model
    if model == "SIR":
        Sim_S, Sim_I, Sim_R = sir.simulate_SIR(S_0, I_0, R_0, beta, gamma, days)
        t = np.arange(0, days)
        plt.figure(figsize=(10,6))
        plt.plot(t, Sim_S, label="Susceptible")
        plt.plot(t, Sim_I, label="Infected")
        plt.plot(t, Sim_R, label="Recovered")
        plt.xlabel(f"Days\nS={S_0}, I={I_0}, Beta={beta}, Gamma={gamma}")
        plt.ylabel("Number of People")
        plt.title(f"SIR Model (N={S_0+I_0+R_0}, {days} Days)")
        plt.legend()
        plt.grid(True)
        plt.show()

    elif model == "SIRD":
        Sim_S, Sim_I, Sim_R, Sim_D = sir.simulate_SIRD(S_0, I_0, R_0, beta, gamma, mu, days)
        t = np.arange(0, days)
        plt.figure(figsize=(10,6))
        plt.plot(t, Sim_S, label="Susceptible")
        plt.plot(t, Sim_I, label="Infected")
        plt.plot(t, Sim_R, label="Recovered")
        plt.plot(t, Sim_D, label="Dead")
        plt.xlabel(f"Days\nS={S_0}, I={I_0}, Beta={beta}, Gamma={gamma}, Mu={mu}")
        plt.ylabel("Number of People")
        plt.title(f"SIRD Model (N={S_0+I_0+R_0}, {days} Days)")
        plt.legend()
        plt.grid(True)
        plt.show()

    else:  # SIRDV
        Sim_S, Sim_I, Sim_R, Sim_D, Sim_V = sir.simulate_SIRDV(S_0, I_0, R_0, beta, gamma, mu, vac_rate, days)
        t = np.arange(0, days)
        plt.figure(figsize=(10,6))
        plt.plot(t, Sim_S, label="Susceptible")
        plt.plot(t, Sim_I, label="Infected")
        plt.plot(t, Sim_R, label="Recovered")
        plt.plot(t, Sim_D, label="Dead")
        plt.plot(t, Sim_V, label="Vaccinated")
        plt.xlabel(f"Days\nS={S_0}, I={I_0}, Beta={beta}, Gamma={gamma}, Mu={mu}, Vac Rate={vac_rate}")
        plt.ylabel("Number of People")
        plt.title(f"SIRDV Model (N={S_0+I_0+R_0}, {days} Days)")
        plt.legend()
        plt.grid(True)
        plt.show()

# Connect button click to function
run_button.on_click(run_simulation)
#-----------------------------------------------------------------------------------------------------------------------
## Final widget-connected version
def run_simulation(button):
    clear_output(wait=True)  # Clear previous outputs (clean plot refresh)
    
    # Re-display widgets after clear
    display(model_choice, beta_slider, gamma_slider, days_slider, day0_text, mu_slider, vac_slider, run_button)
    
    # Read inputs
    MODEL_CHOICE = model_choice.value
    BETA = beta_slider.value
    GAMMA = gamma_slider.value
    DAYS = days_slider.value
    day0_list = [float(x) for x in day0_text.value.split(',')]
    S_0, I_0, R_0 = day0_list
    MU = mu_slider.value
    VAC_RATE = vac_slider.value

    # Call your existing run_sim function
    Sim_S, Sim_I, Sim_R, Sim_D, Sim_V = sir.run_sim(
        S_0=S_0, I_0=I_0, R_0=R_0, beta=BETA, gamma=GAMMA, mu=MU,
        vac_rate=VAC_RATE, days=DAYS, model_choice=MODEL_CHOICE
    )

    # Time axis
    t = np.arange(0, DAYS)

    # Plot
    plt.figure(figsize=(10,6))
    plt.plot(t, Sim_S, label="Susceptible")
    plt.plot(t, Sim_I, label="Infected")
    plt.plot(t, Sim_R, label="Recovered")
    if MODEL_CHOICE in ['SIRD', 'SIRDV']:
        plt.plot(t, Sim_D, label="Deceased")
    if MODEL_CHOICE == 'SIRDV':
        plt.plot(t, Sim_V, label="Vaccinated")

    plt.xlabel(f"Days\nS={S_0}, I={I_0}, Beta={BETA}, Gamma={GAMMA}, Mu={MU}, Vac Rate={VAC_RATE}")
    plt.ylabel("Number of People")
    plt.title(f"{MODEL_CHOICE} Model (N={S_0+I_0+R_0}, {DAYS} Days)")
    plt.legend()
    plt.grid(True)
    
    # Optional: save file (you can comment this out if not desired)
    plt.savefig(f"{MODEL_CHOICE}_N{int(S_0+I_0+R_0)}_{DAYS}Days_{BETA},{GAMMA},{MU},{VAC_RATE}.png")
    plt.show()

# Connect button click
run_button.on_click(run_simulation)
#-----------------------------------------------------------------------------------------------------------------------
