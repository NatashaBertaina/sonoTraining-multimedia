# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 08:30:39 2024

@author: JMCasado; NBertaina
"""

#General import
import os
import sys
import argparse
import glob
import numpy as np
import datetime
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import math
import pandas as pd

sys.path.append("../pybrl")

import pybrl as brl

from pydub import AudioSegment

def wav_to_mp3(wav_path, mp3_path):
    sound_mp3 = AudioSegment.from_mp3(wav_path)
    sound_mp3.export(mp3_path, format='wav')

# Local imports
from data_transform import smooth
from data_export.data_export import DataExport
from data_import.data_import import DataImport
from sound_module.simple_sound import simpleSound
from data_transform import predef_math_functions

# Instanciate the sonoUno clases needed
_dataexport = DataExport(False)
_dataimport = DataImport()
_simplesound = simpleSound()
#_math = PredefMathFunctions()

# Sound configurations, predefined at the moment
_simplesound.reproductor.set_continuous()
_simplesound.reproductor.set_waveform('sine')  # piano; sine
_simplesound.reproductor.set_time_base(0.1)
_simplesound.reproductor.set_min_freq(380)
_simplesound.reproductor.set_max_freq(800)


def generate_plot_space(brailleweight=500):
    # Plot without data (cuad1)
    # Generate the blank plot
    figblank = plt.figure()
    axblank = plt.axes()
    axblank.set_title(' ')
    x = brl.translate('x')
    x = brl.toUnicodeSymbols(x, flatten=True)
    axblank.set_xlabel(' ', fontsize=24, fontfamily='serif', fontweight=brailleweight, labelpad=15)
    y = brl.translate('y')
    y = brl.toUnicodeSymbols(y, flatten=True)
    axblank.set_ylabel(' ', fontsize=24, fontfamily='serif', fontweight=brailleweight, labelpad=10, rotation=0)
    # Setting ticks
    num0 = brl.translate('0')
    num0 = brl.toUnicodeSymbols(num0, flatten=True)
    num25 = brl.translate('25')
    num25 = brl.toUnicodeSymbols(num25, flatten=True)
    num50 = brl.translate('50')
    num50 = brl.toUnicodeSymbols(num50, flatten=True)
    axblank.set_xticks([0,25,50], 
                        [' ',' ',' '], 
                        fontsize=24,
                        fontfamily='serif',
                        fontweight=brailleweight,
                        position=(0,-0.04))
    axblank.set_yticks([0,25,50], 
                        [' ',' ',' '], 
                        fontsize=24,
                        fontfamily='serif',
                        fontweight=brailleweight)
    # Resize
    figblank.tight_layout()
    # Save braille figure
    blankplot_path = 'plot-blank1.png'
    #figblank.savefig(blankplot_path)
    plt.close()

    # Plot without data (cuad all)
    # Generate the blank plot
    figblank_all = plt.figure()
    axblank_all = plt.axes()
    axblank_all.set_title(' ')
    x = brl.translate('x')
    x = brl.toUnicodeSymbols(x, flatten=True)
    axblank_all.set_xlabel(x, fontsize=24, fontfamily='serif', fontweight=brailleweight, labelpad=15)
    y = brl.translate('y')
    y = brl.toUnicodeSymbols(y, flatten=True)
    axblank_all.set_ylabel(y, fontsize=24, fontfamily='serif', fontweight=brailleweight, labelpad=10, rotation=0)
    # Setting ticks
    num_50 = brl.translate('50')
    caract_resta = [['001001']]
    for i in num_50[0]:
        caract_resta[0].append(i)
    num_50 = caract_resta
    num_50 = brl.toUnicodeSymbols(num_50, flatten=True)
    num0 = brl.translate('0')
    num0 = brl.toUnicodeSymbols(num0, flatten=True)
    num50 = brl.translate('50')
    num50 = brl.toUnicodeSymbols(num50, flatten=True)
    axblank_all.set_xticks([-50,0,50], 
                        [num_50,num0,num50], 
                        fontsize=24,
                        fontfamily='serif',
                        fontweight=brailleweight,
                        position=(0,-0.04))
    axblank_all.set_yticks([-50,0,50], 
                        [num_50,num0,num50], 
                        fontsize=24,
                        fontfamily='serif',
                        fontweight=brailleweight)
    # Setting limits
    axblank_all.set_xlim(-55,55)
    axblank_all.set_ylim(-55,55)
    # Axis
    axblank_all.axvline(x=0, color='k', linewidth=1)
    axblank_all.axhline(y=0, color='k', linewidth=1)
    # Legend I
    mayus = [['000101']]
    legend1 = brl.translate('i')
    for i in legend1[0]:
        mayus[0].append(i)
    legend1 = brl.toUnicodeSymbols(mayus, flatten=True)
    axblank_all.text(15, 20, legend1, size=24, fontfamily='serif', fontweight=brailleweight, va="bottom", ha="left", rotation=0)
    #Legend II
    mayus = [['000101']]
    legend2 = brl.translate('ii')
    for i in legend2[0]:
        mayus[0].append(i)
    legend2 = brl.toUnicodeSymbols(mayus, flatten=True)
    axblank_all.text(-35, 20, legend2, size=24, fontfamily='serif', fontweight=brailleweight, va="bottom", ha="left", rotation=0)
    #Legend III
    mayus = [['000101']]
    legend3 = brl.translate('iii')
    for i in legend3[0]:
        mayus[0].append(i)
    legend3 = brl.toUnicodeSymbols(mayus, flatten=True)
    axblank_all.text(-40, -30, legend3, size=24, fontfamily='serif', fontweight=brailleweight, va="bottom", ha="left", rotation=0)
    #Legend II
    mayus = [['000101']]
    legend4 = brl.translate('iv')
    for i in legend4[0]:
        mayus[0].append(i)
    legend4 = brl.toUnicodeSymbols(mayus, flatten=True)
    axblank_all.text(15, -30, legend4, size=24, fontfamily='serif', fontweight=brailleweight, va="bottom", ha="left", rotation=0)
    # Resize
    figblank_all.tight_layout()
    # Save braille figure
    blankplot_path = 'plot-blank-all.png'
    figblank_all.savefig(blankplot_path)
    plt.close()

def blankplot_onlyxy (brailleweight=500):
    # Plot without data, only the space plot and the x y labels
    # Generate the blank plot
    figblank_xy = plt.figure()
    axblank_xy = plt.axes()
    axblank_xy.set_title(' ')
    x = brl.translate('x')
    x = brl.toUnicodeSymbols(x, flatten=True)
    axblank_xy.set_xlabel(x, fontsize=24, fontfamily='serif', fontweight=brailleweight, labelpad=0)
    y = brl.translate('y')
    y = brl.toUnicodeSymbols(y, flatten=True)
    axblank_xy.set_ylabel(y, fontsize=24, fontfamily='serif', fontweight=brailleweight, labelpad=10, rotation=0)
    # Setting ticks
    num0 = brl.translate('0')
    num0 = brl.toUnicodeSymbols(num0, flatten=True)
    num25 = brl.translate('25')
    num25 = brl.toUnicodeSymbols(num25, flatten=True)
    num50 = brl.translate('50')
    num50 = brl.toUnicodeSymbols(num50, flatten=True)
    axblank_xy.set_xticks([0,25,50], 
                        [' ',' ',' '], 
                        fontsize=24,
                        fontfamily='serif',
                        fontweight=brailleweight,
                        position=(0,-0.04))
    axblank_xy.set_yticks([0,25,50], 
                        [' ',' ',' '], 
                        fontsize=24,
                        fontfamily='serif',
                        fontweight=brailleweight)
    # Resize
    figblank_xy.tight_layout()
    # Save braille figure
    blankplot_path = 'plot-blank-xy-labels.png'
    figblank_xy.savefig(blankplot_path)
    plt.close()

blankplot_onlyxy()