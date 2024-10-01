g = 9.8 % gravity, m/s^2
rho = 1141 % density of kerosene, kg/m^3
m_dot = 0.3 % mass flow rate, kg/s

r_1 = 0.1; % impeller inlet radius
r_2 = 0.2; % impeller outlet radius

rps = 15000 / 60; % impeller angular velocity, rpm converted to rps

inlet_angle = 30; % blade inlet angle, degrees
outlet_angle = 20; % blade outlet angle, degrees

b_1 = 0.04; % width of blade at inlet
b_2 = 0.04; % width of blade at outlet

V_r1 = 2*pi * rps * r_1 * tand(inlet_angle) % radial flow velocity at inlet
% 
% Q = 2*pi*r_1 * b_1 * V_r1 % volume flow rate at inlet

Q = m_dot / rho;

V_r2 = Q / (2*pi*r_2*b_2) % radial flow velocity at outlet

V_t2 = (2*pi * rps * r_2) - (V_r2 * cotd(outlet_angle)) % tangential flow velocity at outlet

pump_power = rho * Q * (rps*r_2) * V_t2

pump_head = pump_power / ( rho * g * Q)

pump_outlet_pressure_Pa = pump_head * rho * g % outlet pressure in Pa for a given fluid

pump_outlet_pressure_psi = pump_outlet_pressure_Pa * 0.00014504 % outlet pressure in psi for a given fluid

pump_torque = (9450 * pump_power * 1e-3) / (rps * 60) % pump motor torque in N*m