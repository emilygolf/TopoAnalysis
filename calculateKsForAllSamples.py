import denudationRateAnalysis as dra
import dem as d
import numpy as np
import pickle

prefixes = ['brazil', 'costarica', 'guatemala', 'taiwan', 'venezuela']
suffixes = ['0_4', '0_5', '0_6']

ks = dict()

Ao = 250000.0

for prefix in prefixes:
    print(prefix)

    d8 = d.FlowDirectionD8.load(prefix + "/" + prefix + '_flow_direction')
    area = d.Area.load(prefix + '/' + prefix + '_area')
    locs = np.load(prefix + '/' + prefix +  '_sample_locations.npy')
    local_dict = dict()
    
    for suffix in suffixes:    
        ksi = d.Ksi.load(prefix + "/" + prefix + '_ksi' + suffix)
        relief = d.ScaledRelief.load(prefix + '/' + prefix + '_relief' + suffix)
        theta = float(suffix.replace('_','.'))
        print(theta)
        local_dict[suffix] = dra.calculate_ks_for_sample(locs, d8, ksi, relief, area, Ao, theta)
    
    ks[prefix] = local_dict

pickle.dump( ks, open( "ks.p", "wb" ) )