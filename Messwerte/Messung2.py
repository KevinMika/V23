import numpy as np
import matplotlib.pyplot as plt
import csv
import uncertainties.unumpy as unp
import scipy.stats as stats
#Messung 6 und 7
f1 = np.genfromtxt("6.dat",delimiter=" ",unpack=True,usecols=0)
A1 = np.genfromtxt("6.dat",delimiter=" ",unpack=True,usecols=1)

f2 = np.genfromtxt("7.dat",delimiter=" ",unpack=True,usecols=0)
A2 = np.genfromtxt("7.dat",delimiter=" ",unpack=True,usecols=1)

#Ich plottte 6 und 7 gemeinsam, da man dann die unterschiede besser sieht
plt.subplot(2,1,1)
plt.plot(f1,A1,label=r"$l=50$ mm")
plt.legend()
plt.subplot(2,1,2)
plt.plot(f2,A2,"m",label=r"$l=75$ mm")
plt.legend()
#plt.show()
plt.clf()

#############################################################
#Messung 8
f1 = np.genfromtxt("8_10mm.dat",delimiter=" ",unpack=True,usecols=0)
A1 = np.genfromtxt("8_10mm.dat",delimiter=" ",unpack=True,usecols=1)

f2 = np.genfromtxt("8_13mm.dat",delimiter=" ",unpack=True,usecols=0)
A2 = np.genfromtxt("8_13mm.dat",delimiter=" ",unpack=True,usecols=1)

f3 = np.genfromtxt("8_16mm.dat",delimiter=" ",unpack=True,usecols=0)
A3 = np.genfromtxt("8_16mm.dat",delimiter=" ",unpack=True,usecols=1)

plt.subplot(3,1,1)
plt.plot(f1,A1,label=r"$d=10$ mm")
plt.legend()
plt.subplot(3,1,2)
plt.plot(f2,A2,"m",label=r"$d=13$ mm")
plt.legend()
plt.subplot(3,1,3)
plt.plot(f3,A3,"g",label=r"$d=16$ mm")
plt.legend()
#plt.show()
plt.clf()

#############################################################
#Messung 9

f1 = np.genfromtxt("9_3_10mm.dat",delimiter=" ",unpack=True,usecols=0)
A1 = np.genfromtxt("9_3_10mm.dat",delimiter=" ",unpack=True,usecols=1)

fn1=np.array([3410,3690,4120,6750,6910,7250,10200,10490])
n1=np.linspace(1,8,8)*np.pi/(5)

f2 = np.genfromtxt("9_3_13mm.dat",delimiter=" ",unpack=True,usecols=0)
A2 = np.genfromtxt("9_3_13mm.dat",delimiter=" ",unpack=True,usecols=1)

fn2=np.array([3360,3800,4430,6650,6960,7460,10160,10620])
n2=np.linspace(1,8,8)*np.pi/(5)

f3 = np.genfromtxt("9_3_16mm.dat",delimiter=" ",unpack=True,usecols=0)
A3 = np.genfromtxt("9_3_16mm.dat",delimiter=" ",unpack=True,usecols=1)

fn3=np.array([3320,3930,4730,6560,7020,7720,9590,10160,10800])
n3=np.linspace(1,9,9)*np.pi/(5)

#fick mein leben sind das viele plots
f4 = np.genfromtxt("9_4_10mm.dat",delimiter=" ",unpack=True,usecols=0)
A4 = np.genfromtxt("9_4_10mm.dat",delimiter=" ",unpack=True,usecols=1)

fn4=np.array([3410,3570,3910,4210,6860,7090,7310,10180,10350,10570])
n4=np.linspace(1,10,10)*np.pi/(5)

f5 = np.genfromtxt("9_4_13mm.dat",delimiter=" ",unpack=True,usecols=0)
A5 = np.genfromtxt("9_4_13mm.dat",delimiter=" ",unpack=True,usecols=1)

fn5=np.array([3370,3630,4120,4550,6660,6850,7210,7560,10100,10400,10720])
n5=np.linspace(1,11,11)*np.pi/(5)

f6 = np.genfromtxt("9_4_16mm.dat",delimiter=" ",unpack=True,usecols=0)
A6 = np.genfromtxt("9_4_16mm.dat",delimiter=" ",unpack=True,usecols=1)

fn6=np.array([3330,3720,4340,4910,6560,6860,7380,7870,9600,10050,10490,10960])
n6=np.linspace(1,12,12)*np.pi/(5)

f7 = np.genfromtxt("9_6_10mm.dat",delimiter=" ",unpack=True,usecols=0)
A7 = np.genfromtxt("9_6_10mm.dat",delimiter=" ",unpack=True,usecols=1)

fn7=np.array([3400,3480,3680,3900,4120,6810,6930,7090,7250,10160,10230,10380,10510])
n7=np.linspace(1,13,13)*np.pi/(5)

f8 = np.genfromtxt("9_6_13mm.dat",delimiter=" ",unpack=True,usecols=0)
A8 = np.genfromtxt("9_6_13mm.dat",delimiter=" ",unpack=True,usecols=1)

fn8=np.array([3370,3500,3790,4120,4430,6660,6770,6970,7220,7460,10050,10200,10410,10630,])
n8=np.linspace(1,14,14)*np.pi/(5)

f9 = np.genfromtxt("9_6_16mm.dat",delimiter=" ",unpack=True,usecols=0)
A9 = np.genfromtxt("9_6_16mm.dat",delimiter=" ",unpack=True,usecols=1)

fn9=np.array([3330,3540,3930,4340,4730,5050,6570,6740,7030,7380,7730,9950,10190,10500,10820])
n9=np.linspace(1,15,15)*np.pi/(5)

plt.subplot(3,1,1)
plt.plot(f1,A1,label=r"$d=10$ mm, $n=3$")
plt.legend()
plt.subplot(3,1,2)
plt.plot(f2,A2,"m",label=r"$d=13$ mm, $n=3$")
plt.legend()
plt.subplot(3,1,3)
plt.plot(f3,A3,"g",label=r"$d=16$ mm, $n=3$")
plt.legend()
plt.show()
plt.clf()

plt.subplot(3,1,1)
plt.plot(f4,A4,label=r"$d=10$ mm, $n=4$")
plt.legend()
plt.subplot(3,1,2)
plt.plot(f5,A5,"m",label=r"$d=13$ mm, $n=4$")
plt.legend()
plt.subplot(3,1,3)
plt.plot(f6,A6,"g",label=r"$d=16$ mm, $n=4$")
plt.legend()
plt.show()
plt.clf()

plt.subplot(3,1,1)
plt.plot(f7,A7,label=r"$d=10$ mm, $n=6$")
plt.legend()
plt.subplot(3,1,2)
plt.plot(f8,A8,"m",label=r"$d=13$ mm, $n=6$")
plt.legend()
plt.subplot(3,1,3)
plt.plot(f9,A9,"g",label=r"$d=16$ mm, $n=6$")
plt.legend()
plt.show()
plt.clf()

plt.subplot(3,1,1)
plt.plot(n1,fn1,"x",label=r"$d=10$ mm, $n=3$")
plt.plot(n2,fn2,"x",label=r"$d=13$ mm, $n=3$")
plt.plot(n3,fn3,"x",label=r"$d=16$ mm, $n=3$")
plt.legend()
plt.subplot(3,1,2)
plt.plot(n4,fn4,"x",label=r"$d=10$ mm, $n=4$")
plt.plot(n5,fn5,"x",label=r"$d=13$ mm, $n=4$")
plt.plot(n6,fn6,"x",label=r"$d=16$ mm, $n=4$")
plt.legend()
plt.subplot(3,1,3)
plt.plot(n7,fn7,"x",label=r"$d=10$ mm, $n=6$")
plt.plot(n8,fn8,"x",label=r"$d=13$ mm, $n=6$")
plt.plot(n9,fn9,"x",label=r"$d=16$ mm, $n=6$")
plt.legend()
plt.show()
plt.clf()
#############################################################
#Messung 10

f1 = np.genfromtxt("10.dat",delimiter=" ",unpack=True,usecols=0)
A1 = np.genfromtxt("10.dat",delimiter=" ",unpack=True,usecols=1)

f2 = np.genfromtxt("3_13mm.dat",delimiter=" ",unpack=True,usecols=0)
A2 = np.genfromtxt("3_13mm.dat",delimiter=" ",unpack=True,usecols=1)

plt.subplot(2,1,1)
plt.plot(f1,A1,label=r"$d=13/16$ mm")
plt.legend()
plt.subplot(2,1,2)
plt.plot(f2,A2,"c",label=r"$d=13$ mm")
plt.legend()
plt.show()
plt.clf()

#############################################################
#Messung 11

f1 = np.genfromtxt("11.dat",delimiter=" ",unpack=True,usecols=0)
A1 = np.genfromtxt("11.dat",delimiter=" ",unpack=True,usecols=1)

fn1=np.array([2570,2710,2890,3080,3980,4130,5080,5220,5370,6700,6810,6960,7130,7330,7490,7650,9290,9380,10360,10450,10560])
n1=np.linspace(1,21,21)*np.pi/5

fn2=np.array([3380,3460,3660,3890,4130,4360,4560,6780,6900,7060,7250,7420,10080,10180,10320,10470,10630])
n2=np.linspace(1,17,17)*np.pi/5

plt.plot(f1,A1,label=r"$l=50/75$ mm, $d=16$ mm")
plt.legend()
plt.show()
plt.clf()
plt.subplot(2,1,1)
plt.plot(n1,fn1,"bx",label=r"$l=50/75$ mm, $d=16$ mm")
plt.legend()
plt.subplot(2,1,2)
plt.plot(n2,fn2,"mx",label=r"$d=13$ mm")
plt.legend()
plt.show()
plt.clf()
