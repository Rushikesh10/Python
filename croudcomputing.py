from statistics import mean
from scipy import stats
Estimate=[15,51,5,45,455,42,424,654,245,456,999,888,777,55,44,66,22,44,885,456,951,753,159,852,789,654,123,369,258,147,305]
Estimate.sort()
m=stats.trim_mean(Estimate,0.1)
print(m)