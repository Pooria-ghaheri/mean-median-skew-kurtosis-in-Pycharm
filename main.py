import pandas as pd
#replace the excel file please
df = pd.read_excel (r'C:\Users\Pooria\Desktop\sample3.xlsx')
#Converting str to int
df['age'] = df['age'].astype(int)

#sample size
samplesize = len(df)
print('sample size:', df)

#Sample Mean
SM = 0
for age in df:
   age = df['age'] + SM
mean = SM/samplesize
print('mean:', mean)

#variance
sumOfSquares = 0
s3 = 0
s4 = 0
for age in df:
   deviationscore = df['age'] - mean
   sumOfSquares =  deviationscore**2 + sumOfSquares
   s3 = deviationscore**3 + s3
   s4 = deviationscore**4 + s4
variance = sumOfSquares/(samplesize - 1)
print('variance: ', variance)

#satandard Deviation
SD = variance**0.5
print('satandard Deviation', SD)

#Kurtosis
n = samplesize
s2 = sumOfSquares
m2 = s2/n
m4 = s4//n
populationKurtosis = (m4/m2**2)-3
print('population Kurtosis:', populationKurtosis)
sampleKurtosis = (n*(n+1))/((n-1)*(n-2)*(n-3))*((n-1)**2)*(s4/(s2**2))-3
print('sample Kurtosis:' , sampleKurtosis)

#skewness
sampleSkew = s3/((n-1)*df['age']**3)
print('sample Skewness:' , sampleSkew)
