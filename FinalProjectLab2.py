# -*- coding: utf-8 -*-
# """
# CEC 411 Lab 2

# @author: james
# """
import numpy as py
import matplotlib.pyplot as plt
import math as ma

myID = 9296 # last four digits of my ID
#myID_str = num2str(myID)#orignal
myID_str = str(myID)
Nd = int(1024/16) # d stands for dense sampling
Ns = int(Nd/8) # s stands for sparse sampling
Freq_1 = ma.floor((10 + int(myID_str))/3) # frequency of signal in Hz
Fs_d = Nd # Sampling rate for dense sampling
Fs_s = Ns # Sampling rate for sparse sampling
t_d = py.array(range(0,Nd-1))/Fs_d # Sampling times for dense sampling
t_s = py.array(range(0,Ns-1))/Fs_s # Sampling times for sparse sampling
#Freq_s = (-Fs_s/2 : Fs_s/2-1) # Frequencies 4 spectrum display
Freq_s = py.array(range(-int(Fs_s/2), int(Fs_s/2-1)))
Am = [1, 0.5, 0.2]
print(Am)
fm = [Freq_1, 2*Freq_1, 3*Freq_1]
pm = [0, (py.pi)/2, (py.pi)/3]
modID = myID%1000
pha_a = ma.floor(modID/100)
#pha_b = str2num(myID_str(2)) #original
pha_b = int(myID_str)
# Note: the above pha_a and pha_b have the same value from different eqns.
A1 = 1;
A2 = 0.5*A1;
Freq_2 = 2*Freq_1;


# Task1. Demonstrating the relationship between the waveform and spectrum.
# The core of this task is to show the one-to-one mapping between the time-domain waveform and the
# frequency-domain spectrum of a sinusoidal signal.
# 1A. Generate a sinusoid signal with A1 = 1, F1 (which is Freq_1 above) being the
# integer part of (10 + ID1)=3 (where ID1 is the 
# first digit of the last four digits of your ID,
# e.g., 1 for 1234), and 1 = ID2 (similar to above, ID2 is the second digit of the last four digits
# of your ID, which can be obtained using pha_a or pha_b above). Use t_d and t_s above to
# generate two waveforms and display them together as shown in the upper pane of Fig. 1. As
# an example, one signal can be generated via
# x1_s = cos(2*pi*Freq_1*t_s + pha_a);
# Note that you need to display your initials in the title of the 
# figure.

x1_s = py.cos(2*(py.pi)*Freq_1*t_s + pha_a);
print(x1_s)
x1_d = py.cos(2*(py.pi)*Freq_1*t_d + pha_b);
print(x1_d)
x = plt
x.figure(0)
x.subplot(211);
x.plot(t_s,x1_s,'bo', t_d, x1_d, 'r--');
#axis([ 0 t_d(end) -1.5 +1.5]);
x.title('Continuous Wave')
x.ylabel('Waveform')
x.xlabel('Time')

## Task 1B
x.subplot(212);
X1_s = py.fft.fft(x1_s);
X1_F = py.abs(py.fft.fftshift(X1_s));
x.stem(Freq_s, X1_F);