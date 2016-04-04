""" Routines for calculating the energy levels
    of classical models
"""


def HarmonicOscillator(Frequency, N):
    """ Calculate the nth energy level
        of a harmonic oscillator
    """
    return Frequency * (N + 0.5)

def SymmetricTop(A, B, J, K, Origin=0.0):
    """ Calculate energy levels of a symmetric top
        Here the variable A can be either the A or
        C constants.
    """
    return B * J * (J + 1) + (A - B) * K**2 + Origin

def CalculateVibrationalEnergyLevels(Frequencies, MaximumEnergy):
    """ Loop for calculating vibrational energy levels using
        a list of harmonic oscillators.
    """
    EnergyLevels = []                                   # initialise bin
    for index, frequency in enumerate(Frequencies):     # loop over frequencies
        n = 0
        while HarmonicOscillator(frequency, n) < MaximumEnergy:
            EnergyLevels.append(HarmonicOscillator(frequency, n))
            n = n + 1
    EnergyLevels.sort()                                 # sort in ascending order
    return EnergyLevels

def CalculateOblateTopLevels(A, B, MaximumEnergy, Origin=0.):
    RotationalLevels = []
    J = 0
    K = 0
    while SymmetricTop(A, B, J, K, Origin) <= MaximumEnergy:
        K = 0
        while K <= J and SymmetricTop(A, B, J, K, Origin) <= MaximumEnergy:
            CurrentJK = []
            CurrentJK.append(SymmetricTop(A, B, J, K, Origin))
            RotationalLevels = RotationalLevels + (CurrentJK * (2 * J + 1))       # Add 2J + 1 degeneracy
            K = K + 1
        J = J + 1
    return RotationalLevels