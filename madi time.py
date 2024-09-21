#-----------------VARIABLES--------------------
H = ''       #magnetic field intesity in amperes/meter
D = ''       #displacement flux density in coulombs/meters squared
J = ''       #current density in amperes/meters squared
E = ''       #electric field intensity in volts/meter
dl = ''      # infinitesimal dipole antenna with length dl
ω = ''       #frequency in rad/seconds
t = ''       #time in seconds
λ = ''       #wavelength in meters
ϵ = ''       #permittivity of the material surrounding the antenna in Farads/meter
r = ''       #spherical coordinate r
θ = ''       #spherical coordinate theta
ϕ = ''       #spherical coordinate phi
n = ''       #radiation efficiency in decibels
μ = ''       #usually has a specific value depending on material
σ = ''       #usually has a specific value depending on material
Z = 377      #in ohms, the impedance of free space

#-----------------EQUATIONS--------------------
sin current = I*cos(ωt)                         #sinusoidal current
P_receiver = P_transmitter * (A/(4*pi*r)^2)     #power of receiver 
R_rad = ((2*pi)/3)*Z*((d^2)/(λ^2))              #Radiation resistance
R_ohmic = sqrt((pi*f*μ)/σ)*(d/(2*pi*a))         #resistance of a metal wire at high frequency
near_field = 
far_field = 

