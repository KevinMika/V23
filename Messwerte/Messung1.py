import numpy as np
import matplotlib.pyplot as plt
import csv
import uncertainties.unumpy as unp
import scipy.stats as stats
#75 mm
f1 = np.genfromtxt("1_75mm.dat",delimiter=" ",unpack=True,usecols=0)
A1 = np.genfromtxt("1_75mm.dat",delimiter=" ",unpack=True,usecols=1)
#resonanzfrequenzen 75mm
fn1 = np.array([2390,4600,6870,9140])
n1 = np.linspace(1,4,4)
slope1, intercept1, r_value1, p_value1, std_err1 = stats.linregress(n1,fn1)
#150 mm
f2 = np.genfromtxt("1_150mm.dat",delimiter=" ",unpack=True,usecols=0)
A2 = np.genfromtxt("1_150mm.dat",delimiter=" ",unpack=True,usecols=1)
#resonanzfrequenzen 150mm
fn2 = np.array([2340,3470,4610,5760,6900,8040,9180])
n2 = np.linspace(1,7,7)
slope2, intercept2, r_value2, p_value2, std_err2 = stats.linregress(n2,fn2)
# 225mm
f3 = np.genfromtxt("1_225mm.dat",delimiter=" ",unpack=True,usecols=0)
A3 = np.genfromtxt("1_225mm.dat",delimiter=" ",unpack=True,usecols=1)
#resonanzfrequenzen 225mm
fn3 = np.array([2330,3090,3840,4610,5380,6130,6900,7660,8420,9180,9950])
n3 = np.linspace(1,11,11)
slope3, intercept3, r_value3, p_value3, std_err3 = stats.linregress(n3,fn3)
#300 mm
f4 = np.genfromtxt("1_300mm.dat",delimiter=" ",unpack=True,usecols=0)
A4 = np.genfromtxt("1_300mm.dat",delimiter=" ",unpack=True,usecols=1)
#resonanzfrequenzen 300mm
fn4 = np.array([1740,2320,2890,3470,4030,4600,5180,5750,6320,6890,7470,8050,8610,9180,9760])
n4 = np.linspace(1,15,15)
slope4, intercept4, r_value4, p_value4, std_err4 = stats.linregress(n4,fn4)
#600 mm
f5 = np.genfromtxt("1_600mm.dat",delimiter=" ",unpack=True,usecols=0)
A5 = np.genfromtxt("1_600mm.dat",delimiter=" ",unpack=True,usecols=1)
#resonanzfrequenzen 600mm
fn5 = np.array([1450,1730,2020,2310,2600,2890,3170,3460,3740,4030,4320,4600,4890,5180,5470,5750,6040,6320,6610,6900,7180,7470,7760,8040,8330,8620,8910,9190,9480,9760])
n5 = np.linspace(1,30,30)
slope5, intercept5, r_value5, p_value5, std_err5 = stats.linregress(n5,fn5)

plt.subplot(5, 1, 1)
plt.plot(f1,A1,label=r"$L=75$ mm")
plt.legend()
plt.subplot(5,1,2)
plt.plot(f2,A2,"red",label= r"$L=150$ mm")
plt.legend()
plt.subplot(5,1,3)
plt.legend()
plt.plot(f3,A3,"green",label= r"$L=225$ mm")
plt.legend()
plt.subplot(5, 1, 4)
plt.plot(f4,A4,label=r"$L=300$ mm")
plt.legend()
plt.subplot(5,1,5)
plt.plot(f5,A5,label=r"$L=600$ mm")
plt.legend()
#plt.show()
plt.clf()
plt.plot(n1,fn1,"bx",label=r"$L=75$ mm")
plt.plot(n2,fn2,"rx",label=r"$L=150$ mm")
plt.plot(n3,fn3,"gx",label=r"$L=225$ mm")
plt.plot(n4,fn4,"mx",label=r"$L=300$ mm")#
plt.plot(n5,fn5,"cx",label=r"$L=600$ mm")
plt.plot(n1,slope1*n1+intercept1,"b--")
plt.plot(n2,slope2*n2+intercept2,"r--")
plt.plot(n3,slope3*n3+intercept3,"g--")
plt.plot(n4,slope4*n4+intercept4,"m--")
plt.plot(n5,slope5*n5+intercept5,"c--")
#plt.show()
plt.clf()
# da 2*L=n*c/f, ist f=n*c/2*L, m=c/2*L und damit c=m*2*L
print("L= 75mm, m=",slope1,"mit fehler",std_err1)
print("L= 150mm, m=",slope2,"mit fehler",std_err2)
print("L= 225mm, m=",slope3,"mit fehler",std_err3)
print("L= 300mm, m=",slope4,"mit fehler",std_err4)
print("L= 600mm, m=",slope5,"mit fehler",std_err5)

############################################################################################
#Ab hier beginnt Messung 2
#einfach die Daten für 12*50mm
f1 = np.genfromtxt("2_12mal50mm.dat",delimiter=" ",unpack=True,usecols=0)
A1 = np.genfromtxt("2_12mal50mm.dat",delimiter=" ",unpack=True,usecols=1)
#resonanzfrequenzen für 12*50mm
fn1= np.array([590,870,1160,1450,1730,2020,2310,2600,2880,3170,3450,3740,4030,4310,4600,4890,5170,5460,5740,6040,6320,6610,6890,7180,7470,7750,8040,8320,8610,8900,9190,9470,9760,10050,10330,10620,10910,11190,11480,11760])
n1=np.linspace(1,40,40)*np.pi/60
slope1, intercept1, r_value1, p_value1, std_err1 = stats.linregress(n1,fn1)
print("Dispersions-fit-parameter",slope1)

plt.plot(f1,A1,label=r"$L=12\cdot50$ mm")
plt.legend()
plt.show()
plt.clf()
plt.plot(n1,fn1,"bx",label=r"$L=12\cdot50$ mm")
plt.plot(n1,slope1*n1+intercept1,"b")
plt.legend()
plt.show()
plt.clf()
#k=2pi*n/L,f(k)=d*k, d=steigung

############################################################################################
#Ab hier Messung 3
#Daten für 8*50mm und 10 mm irisen
f1 = np.genfromtxt("3_10mm.dat",delimiter=" ",unpack=True,usecols=0)
A1 = np.genfromtxt("3_10mm.dat",delimiter=" ",unpack=True,usecols=1)
#resonanzen
fn1=np.array([3490,3590,3740,3920,4090,6820,6890,6990,7110,7220,10230,10300,10400,10430,10480,10500])
n1=np.linspace(1,16,16)*np.pi/(5)

f2 = np.genfromtxt("3_13mm.dat",delimiter=" ",unpack=True,usecols=0)
A2 = np.genfromtxt("3_13mm.dat",delimiter=" ",unpack=True,usecols=1)

fn2=np.array([3380,3460,3660,3890,4130,4360,4560,6780,6900,7060,7250,7420,10080,10180,10320,10470,10630])
n2=np.linspace(1,17,17)*np.pi/5

f3 = np.genfromtxt("3_16mm.dat",delimiter=" ",unpack=True,usecols=0)
A3 = np.genfromtxt("3_16mm.dat",delimiter=" ",unpack=True,usecols=1)

fn3 = np.array([3350,3500,3770,4060,4370,4660,4920,5110,6640,6740,6930,7170,7430,7680,7890,9980,10150,10360,10580,10810])
n3 = np.linspace(1,20,20)*np.pi/5

plt.subplot(3,1,1)
plt.plot(f1,A1,"b",label=r"$d=10mm$")
plt.legend()
plt.subplot(3,1,2)
plt.plot(f2,A2,"m",label=r"$d=13$ mm")
plt.legend()
plt.subplot(3,1,3)
plt.plot(f3,A3,"c",label=r"$d=16$ mm")
plt.legend()
plt.show()
plt.clf()
plt.subplot(3,1,1)
plt.plot(n1,fn1,"bx",label=r"$d=10$ mm")
plt.legend()
plt.subplot(3,1,2)
plt.plot(n2,fn2,"mx",label=r"$d=13$ mm")
plt.legend()
plt.subplot(3,1,3)
plt.plot(n3,fn3,"cx",label=r"$d=16$ mm")
plt.legend()
plt.show()
plt.clf()

############################################################################################
#Ab hier Messung 4

f1 = np.genfromtxt("4_10mal50mm.dat",delimiter=" ",unpack=True,usecols=0)
A1 = np.genfromtxt("4_10mal50mm.dat",delimiter=" ",unpack=True,usecols=1)

f2 = np.genfromtxt("4_12mal50mm.dat",delimiter=" ",unpack=True,usecols=0)
A2 = np.genfromtxt("4_12mal50mm.dat",delimiter=" ",unpack=True,usecols=1)

f3 = np.genfromtxt("3_16mm.dat",delimiter=" ",unpack=True,usecols=0)
A3 = np.genfromtxt("3_16mm.dat",delimiter=" ",unpack=True,usecols=1)

plt.subplot(3,1,1)
plt.plot(f1,A1,"b",label=r"$N=10$")
plt.legend()
plt.subplot(3,1,2)
plt.plot(f2,A2,"m",label=r"$N=12$")
plt.legend()
plt.subplot(3,1,3)
plt.plot(f3,A3,"y",label=r"$N=8$")
plt.legend()
plt.show()
plt.clf()
############################################################################################
#Ab hier Messung 5

f1 = np.genfromtxt("5.dat",delimiter=" ",unpack=True,usecols=0)
A1 = np.genfromtxt("5.dat",delimiter=" ",unpack=True,usecols=1)

f2 = np.genfromtxt("3_16mm.dat",delimiter=" ",unpack=True,usecols=0)
A2 = np.genfromtxt("3_16mm.dat",delimiter=" ",unpack=True,usecols=1)

plt.subplot(2,1,1)
plt.plot(f1,A1,label=r"$l=75$ mm")
plt.legend()
plt.subplot(2,1,2)
plt.plot(f2,A2,label=r"$l=50$ mm")
plt.legend()
plt.show()
###############
# Zweiter Teil der Messung in nächster Datei
