#This will be a file for a PD tremor project
import matplotlib
from netpyne import specs, sim 
from neuron import h
import os

%matplotlib auto

os.chdir(r"C:\Users\Mariia Popova\Desktop\PhD\Code\Tremor model\Tremor")

!nrnivmodl

#%% Network parameters
netParams = specs.NetParams()  # object of class NetParams to store the network parameters

#%% Create cells

# Initialize ion concentrations for stn and gpe/i neurons
h("cai0_ca_ion = 5e-6 ")
h("cao0_ca_ion = 2")
h("ki0_k_ion = 105") 
h("ko0_k_ion = 3")
h("nao0_na_ion = 108")
h("nai0_na_ion = 10")

# from hahn, fleming, nambu, otsuka
netParams.cellParams['GPe'] = {
    "conds": {},
    "secs": {
        "soma": {
            "geom": {
                "nseg": 1,
                "diam": 60,
                "L": 60,
                "Ra": 200.0,
                "cm": 1
            },
            "mechs": {
                'myions': {},
                "GPeA": {
                    "gnabar": 0.04,
                    "gkdrbar": 0.0042,
                    "gkcabar": 0.1e-3, 
                    "gcatbar": 6.7e-5, 
                    "kca": 2, 
                    "gl": 4e-5
                }
            }
        }
    }
}

#from fleming
netParams.cellParams['STN'] = {
    "conds": {},
    "secs": {
        "soma": {
            "geom": {
                "nseg": 1,
                "diam": 60,
                "L": 60,
                "Ra": 200.0,
                "cm": 1
            },
            "mechs": {
                'myions': {},
                "stn": {
                    "gnabar": 49e-3,
                    "gkdrbar": 57e-3,
                    "gkabar": 5e-3, 
                    "gkcabar": 0.7e-3, #changed to hahn
                    "gcalbar": 15e-3,
					"gcatbar": 5e-3, 
                    "kca": 2, 
                    "gl": 0.29e-3 #changed to hahn
                }
            }
        }
    }
}

#from santaniello
netParams.cellParams['Th'] = {
    "conds": {},
    "secs": {
        "soma": {
            "geom": {
                "nseg": 1,
                "diam": 96,
                "L": 96,
                #"Ra": 200.0,
                "cm": 1
            },
            "mechs": {
                'tcfastNa': {},
                'tcslowK': {},
                'tcCaT': {},
                'tcCaConc': {},
                'tcfastK': {},
                'tch': {},
                'tcpas2': {}
            },
            'ions': {
                'na': {
                    'e': 45
                },
                'k': {
                    'e': -95
                }
            }
        }
    }
}

#from santaniello
netParams.cellParams['PYR'] = {
    "conds": {},
    "secs": {
        "soma": {
            "geom": {
                "nseg": 1,
                "diam": 96,
                "L": 96,
                "Ra": 100.0,
                "cm": 1
            },
            "mechs": {
                'pas': {
                    'g': 1e-5,
                    'e': -85
                },
                'mchh2': {
                    "vtraub": -55,
                    'gnabar': 0.05,
                    'gkbar': 0.005
                },
                'mcIm': {
                    'tau_m': 1000,
                    'gkbar': 3e-5
                },
                'mcCad': {
                    'depth': 1,
                    'taur': 5,
                    'cainf': 2.4e-4,
                    'kt': 0
                },
                'mcIt': {
                    'gcabar': 4e-4
                }
            },
            'ions': {
                'na': {
                    'e': 50
                },
                'k': {
                    'e': -100
                },
                'ca': {
                    'cai': 2.4e-4,
                    'cao': 2,
                    'eca': 120
                }
            }
        }
    }
}

#from santaniello
netParams.cellParams['FSI'] = {
    "conds": {},
    "secs": {
        "soma": {
            "geom": {
                "nseg": 1,
                "diam": 67,
                "L": 67,
                "Ra": 100.0,
                "cm": 1
            },
            "mechs": {
                'pas': {
                    'g': 0.00015,
                    'e': -70
                },
                'mchh2': {
                    "vtraub": -55,
                    'gnabar': 0.05,
                    'gkbar': 0.01
                }
            },
            'ions': {
                'na': {
                    'e': 50
                },
                'k': {
                    'e': -100
                }
            }
        }
    }
}

#dummy izhi - size like gpe
netParams.cellParams['Str'] = {
    "conds": {},
    "secs": {
        "soma": {
            "geom": {
                "nseg": 1,
                "diam": 60,
                "L": 60,
                "Ra": 200.0,
                "cm": 1
            },
            "pointps": {
                "Izhi": { #???
                    'mod': 'Izhi2007b',
                    'C':1,
                    'k':0.7,
                    'vr':-60,
                    'vt':-40,
                    'vpeak':35,
                    'a':0.03,
                    'b':-2,
                    'c':-50,
                    'd':100,
                    'celltype':1
                }
            }
        }
    }
}

#dummy izhi - size like santaniello
netParams.cellParams['Cer_nuc'] = {
    "conds": {},
    "secs": {
        "soma": {
            "geom": {
                "nseg": 1,
                "diam": 20.248,
                "L": 65,
                "Ra": 35.4,
                "cm": 1
            },
            "pointps": {
                "Izhi": { #???
                    'mod': 'Izhi2007b',
                    'C':1,
                    'k':0.7,
                    'vr':-60,
                    'vt':-40,
                    'vpeak':35,
                    'a':0.03,
                    'b':-2,
                    'c':-50,
                    'd':100,
                    'celltype':1
                }
            }
        }
    }
}

#dummy izhi - size like santaniello
netParams.cellParams['Cer_ctx'] = {
    "conds": {},
    "secs": {
        "soma": {
            "geom": {
                "nseg": 1,
                "diam": 20,
                "L": 20,
                #"Ra": 200.0,
                "cm": 1
            },
            "pointps": {
                "Izhi": { #???
                    'mod': 'Izhi2007b',
                    'C':1,
                    'k':0.7,
                    'vr':-60,
                    'vt':-40,
                    'vpeak':35,
                    'a':0.03,
                    'b':-2,
                    'c':-50,
                    'd':100,
                    'celltype':1
                }
            }
        }
    }
}
#%% Create populations

pop_Size=10

netParams.popParams['GPe_pop'] = {
    "cellModel": "",
    "cellType": 'GPe',
    "numCells": pop_Size,
    "yRange": [
        250,
        750
    ],
    "xRange": [
        0,
        250
    ],
    "zRange": [
        0,
        100
    ]
}

netParams.popParams['GPi_pop'] = {
    "cellModel": "",
    "cellType": 'GPe',
    "numCells": pop_Size,
    "yRange": [
        0,
        500
    ],
    "xRange": [
        250,
        750
    ],
    "zRange": [
        0,
        100
    ]
}

netParams.popParams['STN_pop'] = {
    "cellModel": "",
    "cellType": 'STN',
    "numCells": pop_Size,
    "yRange": [
        250,
        500
    ],
    "xRange": [
        0,
        500
    ],
    "zRange": [
        0,
        100
    ]
}

#add some noise in th! 
netParams.popParams['VLA_pop'] = {
    "cellModel": "",
    "cellType": 'Th',
    "numCells": pop_Size,
    "yRange": [
        250,
        500
    ],
    "xRange": [
        750,
        825
    ],
    "zRange": [
        0,
        100
    ]
}

#add some noise in th! 
netParams.popParams['VLP_pop'] = {
    "cellModel": "",
    "cellType": 'Th',
    "numCells": pop_Size,
    "yRange": [
        250,
        500
    ],
    "xRange": [
        825,
        1000
    ],
    "zRange": [
        0,
        100
    ]
}

#noise in ctx?
netParams.popParams['PYR_pop'] = {
    "cellModel": "",
    "cellType": 'PYR',
    "numCells": 20*pop_Size, #scale to santaniello
    "yRange": [
        0,
        250
    ],
    "xRange": [
        0,
        1000
    ],
    "zRange": [
        0,
        100
    ]
}

#noise in ctx?
netParams.popParams['FSI_pop'] = {
    "cellModel": "",
    "cellType": 'FSI',
    "numCells": 2*pop_Size, #scale to santaniello
    "yRange": [
        0,
        250
    ],
    "xRange": [
        0,
        1000
    ],
    "zRange": [
        0,
        100
    ]
}

#dummy
netParams.popParams['Str_pop'] = {
    "cellModel": "",
    "cellType": 'Str',
    "numCells": pop_Size,
    "yRange": [
        250,
        500
    ],
    "xRange": [
        0,
        250
    ],
    "zRange": [
        0,
        100
    ]
}

#dummy
netParams.popParams['Cern_pop'] = {
    "cellModel": "",
    "cellType": 'Cer_nuc',
    "numCells": pop_Size, #scale to santaniello
    "yRange": [
        750,
        1000
    ],
    "xRange": [
        750,
        850
    ],
    "zRange": [
        0,
        100
    ]
}

#dummy
netParams.popParams['Cerc_pop'] = {
    "cellModel": "",
    "cellType": 'Cer_ctx',
    "numCells": 40*pop_Size, #scale from santaniello
    "yRange": [
        750,
        1000
    ],
    "xRange": [
        850,
        1000
    ],
    "zRange": [
        0,
        100
    ]
}

#%% Add stimulus
#check out amplitude again!! #currently from fleming biases, for tc,ctx,cern,cerc? biases from santaniello
netParams.stimSourceParams['bias_gpe'] = {'type': 'IClamp', 'del': 0, 'dur': 1e12, 'amp':-0.009}
netParams.stimSourceParams['bias_gpi'] = {'type': 'IClamp', 'del': 0, 'dur': 1e12, 'amp': 0.006}
netParams.stimSourceParams['bias_stn'] = {'type': 'IClamp', 'del': 0, 'dur': 1e12, 'amp': -0.125}
netParams.stimSourceParams['bias_pyr'] = {'type': 'IClamp', 'del': 0, 'dur': 1e10, 'amp': 0.17} #0.245
netParams.stimSourceParams['bias_fsi'] = {'type': 'IClamp', 'del': 0, 'dur': 1e10, 'amp': 0.15} #0.070
netParams.stimSourceParams['bias_cern'] = {'type': 'IClamp', 'del': 0, 'dur': 1e10, 'amp': -5.3e-2} #(spontaneous 50 hz?)
#%% Add target
netParams.stimTargetParams['bias_gpe->gpe'] = {'source': 'bias_gpe','sec':'soma', 'loc': 0.5, 'conds': {'pop':'GPe_pop'}}
netParams.stimTargetParams['bias_gpi->gpi'] = {'source': 'bias_gpi','sec':'soma', 'loc': 0.5, 'conds': {'pop':'GPi_pop'}}
netParams.stimTargetParams['bias_stn->stn'] = {'source': 'bias_stn','sec':'soma', 'loc': 0.5, 'conds': {'pop':'STN_pop'}}
netParams.stimTargetParams['bias_pyr->pyr'] = {'source': 'bias_pyr','sec':'soma', 'loc': 0.5, 'conds': {'pop':'PYR_pop'}}
netParams.stimTargetParams['bias_fsi->fsi'] = {'source': 'bias_fsi','sec':'soma', 'loc': 0.5, 'conds': {'pop':'FSI_pop'}}
netParams.stimTargetParams['bias_cern->cern'] = {'source': 'bias_cern','sec':'soma', 'loc': 0.5, 'conds': {'pop':'Cern_pop'}}
#%% Synaptic mechanism parameters - taken from fleming
netParams.synMechParams['AMPA'] = {'mod': 'AMPA_S'}  # excitatory synaptic mechanism
netParams.synMechParams['GABA'] = {'mod': 'GABAa_S'}  # inhibitory synaptic mechanism

#%% Connections - change connectivity rules, now 1 to 1!!!! from fleming
netParams.connParams['STN->GPe'] = {
    'preConds': {'pop': 'STN_pop'}, 
    'postConds': {'pop': 'GPe_pop'},
    'weight': 0.111111,
    'convergence': 1, 
    'sec': 'soma',
    'loc': 0.5,
    'synMech': 'AMPA',
    'delay': 4}

netParams.connParams['STN->GPi'] = {
    'preConds': {'pop': 'STN_pop'}, 
    'postConds': {'pop': 'GPi_pop'},
    'weight': 0.111111,
    'sec': 'soma',
    'loc': 0.5,
    'convergence': 1,
    'synMech': 'AMPA',
    'delay': 2}

netParams.connParams['GPe->GPi'] = {
    'preConds': {'pop': 'GPe_pop'}, 
    'postConds': {'pop': 'GPi_pop'},
    'weight': 0.111111,
    'convergence': 1,
    'sec': 'soma',
    'loc': 0.5,
    'synMech': 'GABA',
    'delay': 2}

netParams.connParams['GPe->STN'] = {
    'preConds': {'pop': 'GPe_pop'}, 
    'postConds': {'pop': 'STN_pop'},
    'weight': 0.111111,
    'convergence': 2,
    'sec': 'soma',
    'loc': 0.5,
    'synMech': 'GABA',
    'delay': 3}

#change weight for parkinsonian state
netParams.connParams['GPe->GPe'] = {
    'preConds': {'pop': 'GPe_pop'}, 
    'postConds': {'pop': 'GPe_pop'},
    'weight': 0.015, #0.005
    'sec': 'soma',
    'loc': 0.5,
    'convergence': 1,
    'synMech': 'GABA',
    'delay': 4}

netParams.connParams['GPi->VLA'] = {
    'preConds': {'pop': 'GPi_pop'}, 
    'postConds': {'pop': 'VLA_pop'},
    'weight': 3,
    'sec': 'soma',
    'loc': 0.5,
    'convergence': 1,
    'synMech': 'GABA',
    'delay': 2}

#change this!!!! for now like fleming but div from santaniello
netParams.connParams['VLA->PYR'] = {
    'preConds': {'pop': 'VLA_pop'}, 
    'postConds': {'pop': 'PYR_pop'},
    'weight': 5, 
    'sec': 'soma',
    'loc': 0.5,
    'divergence': 6,
    'synMech': 'AMPA',
    'delay': 2}

netParams.connParams['VLA->FSI'] = {
    'preConds': {'pop': 'VLA_pop'}, 
    'postConds': {'pop': 'FSI_pop'},
    'weight': 0.3, #same as backwards but 16 times smaller
    'sec': 'soma',
    'loc': 0.5,
    'divergence': 2,
    'synMech': 'AMPA',
    'delay': 4} #2 times bigger

netParams.connParams['VLP->PYR'] = {
    'preConds': {'pop': 'VLP_pop'}, 
    'postConds': {'pop': 'PYR_pop'},
    'weight': 5,
    'sec': 'soma',
    'loc': 0.5,
    'divergence': 6,
    'synMech': 'AMPA',
    'delay': 2}

netParams.connParams['VLP->FSI'] = {
    'preConds': {'pop': 'VLP_pop'}, 
    'postConds': {'pop': 'FSI_pop'},
    'weight': 0.3, #same as backwards but 16 times smaller
    'sec': 'soma',
    'loc': 0.5,
    'divergence': 2,
    'synMech': 'AMPA',
    'delay': 4} #2 times bigger

netParams.connParams['PYR->VLA'] = {
    'preConds': {'pop': 'PYR_pop'}, 
    'postConds': {'pop': 'VLA_pop'},
    'weight': 0.3, # same as backwards but 16 times smaller
    'sec': 'soma',
    'loc': 0.5,
    'convergence': 4,
    'synMech': 'AMPA',
    'delay': 2}

netParams.connParams['PYR->VLP'] = {
    'preConds': {'pop': 'PYR_pop'}, 
    'postConds': {'pop': 'VLP_pop'},
    'weight': 0.3, # same as backwards but 16 times smaller
    'sec': 'soma',
    'loc': 0.5,
    'convergence': 4,
    'synMech': 'AMPA',
    'delay': 2}

netParams.connParams['FSI->FSI'] = {
    'preConds': {'pop': 'FSI_pop'}, 
    'postConds': {'pop': 'FSI_pop'},
    'weight': 0.5, #same as backwards but 10 times smaller, maybe change to 11%??
    'sec': 'soma',
    'loc': 0.5,
    'convergence': 19,
    'synMech': 'GABA',
    'delay': 0} #no delay

netParams.connParams['PYR->PYR'] = {
    'preConds': {'pop': 'PYR_pop'}, 
    'postConds': {'pop': 'PYR_pop'},
    'weight': 9, #same as backwards but 1.8 times bigger, maybe change to 20%??
    'sec': 'soma',
    'loc': 0.5,
    'divergence': 5,
    'synMech': 'AMPA',
    'delay': 0} #no delay

netParams.connParams['PYR->FSI'] = {
    'preConds': {'pop': 'PYR_pop'}, 
    'postConds': {'pop': 'FSI_pop'},
    'weight': 0.8, #same as backwards but 6 times smaller also scaled, maybe change to 20%??
    'sec': 'soma',
    'loc': 0.5,
    'convergence': 20*pop_Size,
    'synMech': 'AMPA',
    'delay': 0} #no delay

netParams.connParams['FSI->PYR'] = {
    'preConds': {'pop': 'FSI_pop'}, 
    'postConds': {'pop': 'PYR_pop'},
    'weight': 7.3, #santaniello scaled to fleming, maybe change to 10%??
    'sec': 'soma',
    'loc': 0.5,
    'divergence': 20*pop_Size,
    'synMech': 'GABA',
    'delay': 0} #no delay

netParams.connParams['PYR->STN'] = {
    'preConds': {'pop': 'PYR_pop'}, 
    'postConds': {'pop': 'STN_pop'},
    'weight': 0.12, 
    'sec': 'soma',
    'loc': 0.5,
    'convergence': 5,
    'synMech': 'AMPA',
    'delay': 1}

netParams.connParams['PYR->Str'] = {
    'preConds': {'pop': 'PYR_pop'}, 
    'postConds': {'pop': 'Str_pop'},
    'weight': 0.12, #like to STN
    'sec': 'soma',
    'loc': 0.5,
    'convergence': 5, #like to STN
    'synMech': 'AMPA',
    'delay': 1} #like to STN

netParams.connParams['Str->GPe'] = {
    'preConds': {'pop': 'Str_pop'}, 
    'postConds': {'pop': 'GPe_pop'},
    'weight': 0.01, #fleming
    'sec': 'soma',
    'loc': 0.5,
    'convergence': 1, #fleming
    'synMech': 'GABA',
    'delay': 1} #fleming

#taken from cern-vlp
netParams.connParams['Cern->Str'] = {
    'preConds': {'pop': 'Cern_pop'}, 
    'postConds': {'pop': 'Str_pop'},
    'weight': 0.5, 
    'sec': 'soma',
    'loc': 0.5,
    'divergence': 1,
    'synMech': 'AMPA',
    'delay': 4} 

netParams.connParams['Cern->VLP'] = {
    'preConds': {'pop': 'Cern_pop'}, 
    'postConds': {'pop': 'VLP_pop'},
    'weight': 0.5, #santaniello scaled yo fleming 10 times smaller
    'sec': 'soma',
    'loc': 0.5,
    'divergence': 1,
    'synMech': 'AMPA',
    'delay': 4} #santaniello 2 times more (scaled to fleming)

netParams.connParams['Cerc->Cern'] = {
    'preConds': {'pop': 'Cerc_pop'}, 
    'postConds': {'pop': 'Cern_pop'},
    'weight': 0.3, #santaniello scaled to fleming
    'sec': 'soma',
    'loc': 0.5,
    'convergence': 40,
    'synMech': 'GABA', #from santaniello scheme
    'delay': 8.4} #santaniello scaled 2 times more

netParams.connParams['PYR->Cerc'] = {
    'preConds': {'pop': 'PYR_pop'}, 
    'postConds': {'pop': 'Cerc_pop'},
    'weight': 1276, #santaniello scaled to fleming (3.828)
    'sec': 'soma',
    'loc': 0.5,
    'divergence': 2.5, #cause there are gtl in between
    'synMech': 'AMPA',
    'delay': 8} #santaniello scaled 2 times more

netParams.connParams['PYR->Cern'] = {
    'preConds': {'pop': 'PYR_pop'}, 
    'postConds': {'pop': 'Cern_pop'},
    'weight': 0.11, #santaniello scaled to fleming 
    'sec': 'soma',
    'loc': 0.5,
    'convergence': 20, 
    'synMech': 'AMPA',
    'delay': 3.4} #santaniello scaled 2 times more

#taken from cern-vlp
netParams.connParams['STN->Cerc'] = {
    'preConds': {'pop': 'STN_pop'}, 
    'postConds': {'pop': 'Cerc_pop'},
    'weight': 0.5,
    'sec': 'soma',
    'loc': 0.5,
    'divergence': 1,
    'synMech': 'AMPA',
    'delay': 4} 

#change weight for parkinsonian state
netParams.connParams['Str->Str'] = {
    'preConds': {'pop': 'Str_pop'}, 
    'postConds': {'pop': 'Str_pop'},
    'weight': 0.015, 
    'sec': 'soma',
    'loc': 0.5,
    'convergence': 1,
    'synMech': 'GABA',
    'delay': 4}
#What to do with striato-striatal connections?, now like for gpe
#%% cfg  
cfg = specs.SimConfig()					            # object of class SimConfig to store simulation configuration
cfg.duration = 1*1e3 						            # Duration of the simulation, in ms
cfg.dt = 0.01								                # Internal integration timestep to use
cfg.verbose = 0						                # Show detailed messages 
cfg.recordTraces = {'V_soma':{'sec':'soma','loc':0.5,'var':'v'}}  # Dict with traces to record
#cfg.recordTraces['dend_K'] =  { "sec": "soma", "loc": 0.0, "var": "ena"}
cfg.recordStep = 0.01 			
cfg.filename = 'model_output'  			# Set file output name
cfg.saveJson = False
cfg.analysis['plotTraces'] = {'include': [0,pop_Size,2*pop_Size,3*pop_Size,4*pop_Size,5*pop_Size,250,270,280,290]} # Plot recorded traces for this list of cells
cfg.hParams['celsius'] = 36
cfg.hParams['v_init'] = -68

#%% run
sim.createSimulateAnalyze(netParams = netParams, simConfig = cfg)
sim.analysis.plotConn(includePre = ['GPe_pop','STN_pop','GPi_pop','VLA_pop','VLP_pop','PYR_pop','FSI_pop','Str_pop','Cern_pop','Cerc_pop'], includePost = ['GPe_pop','STN_pop','GPi_pop','VLA_pop','VLP_pop','PYR_pop','FSI_pop','Str_pop','Cern_pop','Cerc_pop'],feature='numConns', graphType='bar')
#sim.analysis.plot2Dnet(include = ['GPe_pop','STN_pop','GPi_pop','VLA_pop','VLP_pop','PYR_pop','FSI_pop','Str_pop','Cern_pop','Cerc_pop']);
sim.analysis.plotSpikeStats(include = ['GPe_pop','STN_pop','GPi_pop','VLA_pop','VLP_pop','PYR_pop','FSI_pop','Str_pop','Cern_pop','Cerc_pop'], saveFig=False);
#sim.analysis.plotRateSpectrogram(include=['GPi_pop']);