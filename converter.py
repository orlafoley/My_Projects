'''Temperature Conversions'''
TempFtoC = lambda fahrenheit: ((fahrenheit - 32)*(5/9))*100/100
#convert temp from F to C
TempCtoF = lambda celsius: (((celsius)*(9/5))+32)*100/100
#convert temp from C to F
TempCtoK = lambda celsius: celsius + 273.15
TempKtoC = lambda kelvin: kelvin - 273.15
TempFtoK = lambda fahrenheit: int(TempCtoK(TempFtoC(fahrenheit))*100)/100
TempKtoF = lambda kelvin: int(TempCtoF(TempKtoC(kelvin))*100)/100






'''Distance Convertions'''
DistMtoK = lambda miles: (miles*(5/8))*100/100
#convert from miles to km
DistKtoM = lambda km: (km*(8/5))*100/100
#convert from km to miles
VolumeLtoG = lambda litre: int((litre/3.785)*1000)/1000
#convert from litres to US gallons
VolumeGtoL = lambda gallon: int((gallon*(3.785))*1000)/1000
#convert from US gallons to litres
VolumeImpGaltoUSGal = lambda imperial: int((imperial*1.201)*1000)/1000
#convert imperial gallons to US gallons
VolumeUSGaltoImpGal = lambda us: int((us/1.201)*1000)/1000
#convert US gallons to imperial gallons
#print(VolumeLtoG(VolumeUSGaltoImpGal(1)))
#convert litres to imperial gallons
#print(VolumeImpGaltoUSGal(VolumeGtoL(1)))
#convert imperial gallons to litres
VolumeLtoImpGal = lambda litre: int((VolumeLtoG(litre)/1.201)*1000)/1000
VolumeImpGaltoL = lambda imperial: int((VolumeGtoL(imperial)*1.201)*1000)/1000








'''Angle Conversions'''
import math
AngleDtoRad = lambda degrees: int((degrees*(math.pi/180))*100)/100
AngleRadtoD = lambda radians: int((radians*(180/math.pi))*100)/100






'''Weight Conversions'''
KilotoLbs = lambda kilograms: int((kilograms*2.205)*1000)/1000
LbstoKilo = lambda pounds: int((pounds/2.205)*1000)/1000
OztoLbs = lambda ounce: int((ounce/16)*100)/100
LbstoOz = lambda pounds: int((pounds*16)*100)/100
OztoStone = lambda ounce: int((ounce/224)*100000)/100000
StonetoOz = lambda stone: int((stone*224)*100)/100
StonetoLbs = lambda stone: int((stone*14)*100)/100
LbstoStone = lambda pounds: int((pounds/14)*100)/100
KgtoStone = lambda kilogram: int(LbstoStone(KilotoLbs(kilogram))*100)/100
StonetoKg = lambda stone: int(LbstoKilo(StonetoLbs(stone))*100)/100
