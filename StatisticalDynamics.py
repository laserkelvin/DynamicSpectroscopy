#!/bin/python

import matplotlib.pyplot as plt
import matplotlib
from EnergyLevels import *
matplotlib.style.use('ggplot')

""" Routines for calculating statistical dynamics using
    very rudimentary models (e.g. prior distribution)

    Basic focus for now is on state counting.

"""

def StateCountRotatingVibrator(Frequencies, A, B, MaximumEnergy):
    """ Combines the harmonic oscillator and symmetric top
        rigid rotor energy levels to give a full state count.
    """
    EnergyLevels = []
    for index, frequency in enumerate(Frequencies):                # Loop over frequencies
        n = 0
        while HarmonicOscillator(frequency, n) <= MaximumEnergy:   # while we're not above maximum energy
            Evib = HarmonicOscillator(frequency, n)
            EnergyLevels.append(Evib)
            EnergyLevels = EnergyLevels + CalculateOblateTopLevels(A, B, MaximumEnergy, Origin=Evib)
            n = n + 1
    EnergyLevels.sort()
    print " There are a total of \t" + str(len(EnergyLevels)) + "\t states counted."
    return EnergyLevels

def PlotHistogram(Levels, Bins=100):
	fig = plt.figure(figsize=(10,7))
	plt.xlabel("Energy")
	plt.ylabel("Counts")
	n, bins, patches = plt.hist(Levels, Bins, facecolor="green", alpha=0.75)
	plt.show()
