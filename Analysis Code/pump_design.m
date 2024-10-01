%% Fuel Pump Calculations

m_dot_f = 0.24964; % mass flow rate of fuel, kg/s
rho_f = 800; % density of fuel, kg/m^3

Q_f = m_dot_f / rho_f; % volume flow rate of fuel, m^3/s

SG_f = 0.8; % specific gravity of fuel

omega_rps = 15000/60; % angular velocity of impeller, rpm to rps
omega_f = omega_rps * 2*pi;

r_f = 0.05; % radius of impeller, m

A_2 = pi*((6.35e-3)^2); % area at pump outlet, a 1/2" diameter or 1/4" (6.35 mm) radius pipe

beta_2 = -75; % blade metal angle at outlet, negative means swept back from radial vector
% approximately equal to relative flow angle, neglecting slip

phi_f = Q_f / (A_2 * omega_f * r_f); % flow coefficient

psi_f = 1 + phi_f * tand(beta_2); % head coefficient

H_f = (psi_f * (r_f * omega_f)^2) / 9.81; % Head

P_psi_f = (0.433 * H_f * SG_f) * 3.28 % Head converted into pressure in psi

%% Liquid Oxygen Pump Calculations

m_dot_o = 0.54921; % mass flow rate of LOX, kg/s
rho_o = 1100; % density of LOX, kg/m^3

Q_o = m_dot_o / rho_o; % volume flow rate of LOX, m^3/s

SG_o = 1.1; % specific gravity of LOX

omega_rps = 12000/60; % angular velocity of impeller, rpm to rps
omega_o = omega_rps * 2*pi;

r_o = 0.05; % radius of impeller, m

A_2 = pi*((6.35e-3)^2); % area at pump outlet, a 1/2" diameter or 1/4" (6.35 mm) radius pipe

beta_2 = -75; % blade metal angle at outlet, negative means swept back from radial vector
% approximately equal to relative flow angle, neglecting slip

phi_o = Q_o / (A_2 * omega_o * r_o); % flow coefficient

psi_o = 1 + phi_o * tand(beta_2); % head coefficient

H_o = (psi_o * (r_o * omega_o)^2) / 9.81; % Head

P_psi_o = (0.433 * H_o * SG_o) * 3.28 % Head converted into pressure in psi