""" Routines for calculating the energy levels
    of classical models
"""

""" Analytic energy level calculators

These will return the energy associated with some
quantum mechanical model/object.

"""

def HarmonicOscillator(Frequency, N):
    """ Calculate the nth energy level
        of a harmonic oscillator
    """
    return Frequency * (N + 0.5)

def CombinationHarmonicOscillator(Frequencies, Quanta):
    """ Calculates and sums harmonic frequencies, returning the
        total energy.
        Frequencies and Quanta are input as lists.
    """
    Energy = 0.
    for index, frequency in enumerate(Frequencies):
        Energy = Energy + HarmonicOscillator(frequency, Quanta[index])
    return Energy

def SymmetricTop(A, B, J, K, Origin=0.0):
    """ Calculate energy levels of a symmetric top
        Here the variable A can be either the A or
        C constants.
    """
    return B * J * (J + 1) + (A - B) * K**2 + Origin

""" Automated routines

Loops for calculating stacks of states

"""

def CalculateVibrationalEnergyLevels(Frequencies, MaximumEnergy):
    """ Loop for calculating vibrational energy levels using
        a list of harmonic oscillators.

        ONLY DOES FUNDAMENTAL VIBRATIONS!
    """
    EnergyLevels = []                                   # initialise bin
    for index, frequency in enumerate(Frequencies):     # loop over frequencies
        n = 0
        while HarmonicOscillator(frequency, n) < MaximumEnergy:
            EnergyLevels.append(HarmonicOscillator(frequency, n))
            n = n + 1
    EnergyLevels.sort()                                 # sort in ascending order
    return EnergyLevels

def EMaxOblateTopLevels(A, B, MaximumEnergy, Origin=0.):
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

def JMaxOblateTopLevels(A, B, MaximumJ, MaximumEnergy, Origin=0.):
    RotationalLevels = []
    for J in xrange(MaximumJ):
        CurrentK = []
        for K in xrange(0, J):
            CurrentK = []
            if SymmetricTop(A, B, J, K, Origin) <= MaximumEnergy:
                CurrentK.append(SymmetricTop(A, B, J, K, Origin))
                CurrentK = CurrentK * (2 * J + 1)
            else:
                pass
        RotationalLevels = RotationalLevels + CurrentK
    return RotationalLevels

def PhaseSpaceAngularMomentum(A, B, MaximumJ, MaximumEnergy, ImpactParameter, ReducedMass, Origin=0., ParentJ=0):
    RotationalLevels = []
    for J in xrange(MaximumJ):
        CurrentK = []
        for K in xrange(0, J):
            CurrentK = []
            # Calculate the pure rotational energy
            RotationalEnergy = SymmetricTop(A, B, J, K, Origin)
            # Work out centrifugal barrier and energy; L is -J
            CentrifugalEnergy = CentrifugalBarrier(-J, )
                # Work out centrifugal barrier and energy

def CentrifugalBarrier(OrbitalAngularMomentum, ImpactParameter, ReducedMass):
    pass