import matplotlib.pyplot as plt
import numpy as np

g = 9.81

#dry_weight_initial = 1000
prop_mass = 2200
engine_mass = 100 # Estimate of base weight of engine without pump drive, if applicable

# this analysis assumes that electric motors and turbopumps have similar power density values (W/kg)
# this seems to be a reasonable assumption when including additional combustion devices such as gas generators/preburners

burn_time_s = 120
m_dot_tot = prop_mass / burn_time_s
m_dot_f = m_dot_tot / 3
m_dot_o = m_dot_tot * (2/3)

# Pc vs. Isp (other factors normalized)

Pc = np.arange(3e3, 35e3, 10)
At = 0.035 # throat area, square meters
c_star = Pc * At / m_dot_tot
T = 3500
M_LOX = 0.372
M_kero = 0.172
M_CO2 = 0.044
M_H2O = 0.018
#M_weighted = ((2 * M_LOX) + (M_kero)) / 3
M_weighted = (24 * M_CO2 + 26 * M_H2O) / 50 # Carbon dioxide and water are the products of oxygen-kerosene combustion - this assumes complete combustion of the propellants so the only exhaust gases are these products
gamma = 1.01
Pe = 81
Ve = np.power((((T * 8.314) / M_weighted) * (2*gamma / (gamma - 1)) * (1 - (np.power((Pe / Pc), (gamma-1)/gamma)))), 0.5)

print(np.power((Pe / Pc), (gamma-1)/gamma))

#print(Ve)

Isp = Ve / g

#print(c_star)
#print(Isp)

plt.plot(Pc, Isp)

plt.xlabel('Chamber Pressure (kPa)')
plt.ylabel('Specific Impulse (s)')
plt.title('Specific Impulse vs. Chamber Pressure')

plt.legend()

plt.show()

# Pc vs. Vehicle Weight (estimated, use hoop stress equation)

Dia = 0.33 # 0.5 meter diameter rocket
H = 7

# Stainless steel 316L properties
yield_strength_316L = 205e+3
hoop_stress_316L = yield_strength_316L * 0.95
density_316L = 7850 # density in kg/m^3

# AlLi 2195-T8 Properties
yield_stress_AlLi = 400e3
hoop_stress_AlLi = yield_stress_AlLi * 0.95
density_AlLi = 2700 # density in kg/m^3

#Carbon Fiber properties
yield_strength_CF = 5000e3
hoop_stress_CF = yield_strength_CF * 0.95
density_CF = 1750 # density in kg/m^3

t = (Pc * Dia) / hoop_stress_AlLi
tank_mass = ((np.pi * np.power(0.5,2) * H) - (np.pi * np.power(0.5-t, 2) * H)) * density_AlLi


# Calculate the mass of a pump-fed vehicle's tank, assuming the tanks are kept at about 50psi or 350kPa
pump_fed_tank_pressure = 350
t_pump_fed = (pump_fed_tank_pressure * Dia) / hoop_stress_AlLi
pump_fed_tank_mass = ((np.pi * np.power(0.5,2) * H) - (np.pi * np.power(0.5-t_pump_fed, 2) * H)) * density_AlLi


# Calculate battery mass for an electric pump-fed engine
battery_power_density = 430 # power density, W/kg
power_req = (((Pc * 0.069) * m_dot_tot) / 600) * 1000
battery_mass_power = power_req / battery_power_density
print(battery_mass_power)

battery_energy_density = 250 # energy density, Wh/kg
energy_req = (120/3600) * power_req
battery_mass_energy = energy_req / battery_energy_density
print(battery_mass_energy)

battery_mass = np.maximum(battery_mass_energy, battery_mass_power)


plt.plot(Pc, tank_mass+engine_mass, label="Pressure-fed Vehicle Mass")
plt.plot(Pc, np.full(tank_mass.size, pump_fed_tank_mass+engine_mass), label="Turbopump-fed Vehicle Mass", color="orange")
plt.plot(Pc, np.full(tank_mass.size, pump_fed_tank_mass+battery_mass+engine_mass), label="Electric Pump-fed Vehicle Mass", color="green")


plt.xlabel('Chamber Pressure (kPa)')
plt.ylabel('Vehicle Dry Mass (kg)')
plt.title('Vehicle Dry Mass vs. Chamber Pressure for Pump- and Pressure-fed Vehicles')

plt.legend()

plt.show()

# dV vs. Pc - rocket eqn
    #  show a plot up to a lower pressure with pump and pressure-fed. but also show the even higher
    # performance that can be obtained at higher pressures that are feasible with pump-fed engines
    # (past the point at which the tanks become way too heavy on a pressure-fed system)

deltaV_press = Ve * np.log((tank_mass+prop_mass+engine_mass)/(tank_mass+engine_mass))
deltaV_pump = Ve * np.log((pump_fed_tank_mass+prop_mass+engine_mass)/(pump_fed_tank_mass+engine_mass))
deltaV_electric = Ve * np.log((pump_fed_tank_mass+prop_mass+engine_mass+battery_mass)/(pump_fed_tank_mass+battery_mass+engine_mass))

plt.plot(Pc, deltaV_press, label="Pressure-fed Vehicle Performance")
plt.plot(Pc, deltaV_pump, label="Turbopump-fed Vehicle Performance", color="orange")
plt.plot(Pc, deltaV_electric, label="Electric Pump-fed Vehicle Performance", color="green")


plt.xlabel('Chamber Pressure (kPa)')
plt.ylabel(r'$\mathrm{\Delta}$' + 'V (m/s)')
plt.title(r'$\mathrm{\Delta}$' + 'V' + ' vs. Chamber Pressure for Pump- and Pressure-fed Vehicles')

plt.legend()

plt.show()
