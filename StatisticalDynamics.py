#!/bin/python

import matplotlib.pyplot as plt
import matplotlib
from EnergyLevels import *
from itertools import combinations, combinations_with_replacement
matplotlib.style.use('ggplot')

""" Routines for calculating statistical dynamics using
    very rudimentary models (e.g. prior distribution)

    Basic focus for now is on state counting.

"""
def StateCountRotatingVibrator(Frequencies, A, B, Method="EMax", MaximumEnergy=100., MaximumJ=20):
    """ Combines the harmonic oscillator and symmetric top
        rigid rotor energy levels to give a full state count.
    """
    EnergyLevels = []
    for index, frequency in enumerate(Frequencies):                # Loop over frequencies
        n = 0
        while HarmonicOscillator(frequency, n) <= MaximumEnergy:   # while we're not above maximum energy
            Evib = HarmonicOscillator(frequency, n)
            EnergyLevels.append(Evib)
            if Method == "EMax":
                EnergyLevels = EnergyLevels + EMaxOblateTopLevels(A, B, MaximumEnergy, Origin=Evib)
            elif Method == "JMax":
                EnergyLevels = EnergyLevels + JMaxOblateTopLevels(A, B, MaximumJ, MaximumEnergy, Origin=Evib)
            else:
                print " Method error. Specified method does not exist."
                break
            n = n + 1
    EnergyLevels.sort()
    print " There are a total of \t" + str(len(EnergyLevels)) + "\t states counted."
    return EnergyLevels

def BruteForceVibrator(Frequencies, MaxQuanta=10, Mode="Run"):
    """ Calculates and sums harmonic frequencies, returning the
        total energy.
        Frequencies are input as a list, and MaxQuanta is an
        integer.
    """
    EnergyLevels = []
    for length in xrange(len(Frequencies) + 1):
        # Loop over length number of modes to be considered; i.e. 1 combination, 2 combination etc.
        LevelGenerator = combinations(Frequencies, length)
        for Combination in LevelGenerator:
            # For a given combination of bands, generate a list of quantum numbers
            if Mode != "Run":
                print Combination
            # For a combination of frequencies, we now go through quanta
            QuantumNumbers = range(0, MaxQuanta)
            QuantaGenerator = combinations_with_replacement(QuantumNumbers, length)
            for Quanta in QuantaGenerator:
                Energy = CombinationHarmonicOscillator(Combination, Quanta)
                if Mode != "Run":
                    print Quanta
                    print Energy
                EnergyLevels.append(CombinationHarmonicOscillator(Combination, Quanta))
    print " Total of \t" + str(len(EnergyLevels)) + "\t vibrational states counted."
    EnergyLevels.sort()
    return EnergyLevels

def BruteForceRotator(VibrationalEnergies, A, B, MaximumEnergy=1000., MaximumJ=30):
    """ Supplementary to the BruteForceVibrator; for each vibrational level
        we tack on rotational levels too.
    """
    EnergyLevels = []
    for Vibration in VibrationalEnergies:
        EnergyLevels = EnergyLevels + JMaxOblateTopLevels(A, B, MaximumJ, MaximumEnergy, Origin=Vibration)
    EnergyLevels.sort()
    print " Total of \t" + str(len(EnergyLevels)) + "\t rovibrational states counted."
    return EnergyLevels

def PlotHistogram(Levels, Bins=100):
	fig = plt.figure(figsize=(10,7))
	plt.xlabel("Energy")
	plt.ylabel("Counts")
	n, bins, patches = plt.hist(Levels, Bins, facecolor="green", alpha=0.75)
	plt.show()
