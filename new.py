import numpy as np
import matplotlib.pyplot as plt

#  parameters
delta_m2 = 0.001      # in eV^2
sin2_2theta = 0.8      # sin^2(2θ)
E = 5              # Neutrino energy in MeV

# Distance from 0 to 1000 km
L = np.linspace(0, 1000, 1000)  # in km

# Oscillation phase with proper conversion factor
# factor 1270 is when we convert L from km to eV and E from MeV to eV
phase =  1270 * delta_m2 * L / E

# Oscillation and survival probabilities
P_emu = sin2_2theta * np.sin(phase)**2
P_ee = 1 - P_emu

# Plottin
plt.figure(figsize=(10, 6))
plt.plot(L, P_emu, label=r'$P(\nu_e \rightarrow \nu_\mu)$', color='red')
plt.plot(L, P_ee, label=r'$P(\nu_e \rightarrow \nu_e)$', color='blue')
plt.xlabel('L (km)')
plt.ylabel('Probability')
plt.title('Two-Flavor Neutrino Oscillation')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
