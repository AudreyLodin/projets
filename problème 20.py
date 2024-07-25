import statistics

observations = [4, 7, 9, 12, 20, 5, 9]

# Calcul de la médiane
median = statistics.median(observations)

# Calcul de la médiane inférieure
lower_median = statistics.median([x for x in observations if x < median])

# Calcul de la médiane supérieure
upper_median = statistics.median([x for x in observations if x > median])

# Calcul de l'écart interquartile
first_quartile = statistics.quantiles(observations, n=4)[0]
third_quartile = statistics.quantiles(observations, n=4)[-1]
interquartile_range = third_quartile - first_quartile

print("Médiane :", median)
print("Médiane inférieure :", lower_median)
print("Médiane supérieure :", upper_median)
print("Écart interquartile :", interquartile_range)