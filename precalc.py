"""
This script precalculates functions that do not need to be called everytime.
This is to speed up calculations.
"""

import numpy as np

# import local modules
import cib 
import gal
import halo as h
import consts

# Calculate rho critical

# Radius of halo containing 200 * rho_crit mass
rad200 = h.r_delta(delta_h = 200) # shape (Mh, z) # units 

# slope of the power spectrum
dlnpk_dlnk = h.get_dlnpk_dlnk() # shape (z, Mh)
#nu_to_c200c_val = h.nu_to_c200c(rad, dlnpk_dlnk)

##--RADIAL KERNEL--##
z_all = consts.Plin['z']
w_cib = cib.get_W_cib(z_cib=z_all)
w_gal = gal.get_Wgal(dict_gal=consts.dict_gal['ELG'])
w_mu = gal.get_Wmu(dict_gal=consts.dict_gal['ELG'])
w_gal_tot = w_gal + w_mu
w_cibxgal = w_gal_tot * w_cib

##--BIAS MODEL--##
nu200 = h.nu_delta(rad200) # calculate peak height (Mh, z)

# calculate halo bias as a function of nu and z
halo_biases = np.zeros_like(nu200)
for i in range(len(halo_biases)):
    halo_biases[:,i] = h.b_nu(nu=nu200[:,i], z = consts.Plin['z'])