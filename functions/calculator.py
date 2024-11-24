#calculator.py
#funkcja tworzaca kalkulator Siesta o zadanych parametrach

from ase.calculators.siesta import Siesta
from ase.units import Ry


def get_calc(label):
    tmp_calc = Siesta(label=f'{label}',
                  xc='PBE',
                  basis_set='SZP',
                  kpts=[8, 8, 1],
                  mesh_cutoff=200 * Ry,
                  spin='polarized',
                  fdf_arguments={'MaxSCFIterations':    500,
                                'PAO.BasisSize':           'SZP',
                                'MD.NumCGsteps':        250,
                                'MD.TypeOfRun':         'CG',
                                'MD.VariableCell':      'F',
                                'MD.MaxCGDispl':        '0.2000000000  Bohr',
                                'MD.MaxForceTol':       '0.05 eV/Ang',
                                'SolutionMethod':     'Diagon',
                                'DM.MixingWeight':   0.1000000000,
                                'DM.NumberPulay':     '6',
                                'DM.NumberBroyden':        0,
                                'DM.OccupancyTolerance':   0.1000000000E-11,
                                'DM.NumberKick':           0,
                                'DM.KickMixingWeight':     0.5000000000,
                                'DM.Tolerance':       1.0E-3,
                                'DM.UseSaveDM':       '.true.',
                                'DM.UseSaveXV':      '.true',
                                'WriteMullikenPop':        1 ,
                                'WriteDenchar':            '.true.',
                                'WriteKpoints':            '.true.',
                                'WriteForces':             '.true.',
                                'WriteDM':                 '.true.',
                                'WriteXML':                '.true.',
                                'WriteEigenvalues':        '.false.',
                                'WriteCoorStep':           '.true.',
                                'WriteMDhistory':          '.true.',
                                'WriteMDXmol':             '.true.',
                                'WriteCoorXmol':           '.true.',
                                 },
                 )
    return tmp_calc