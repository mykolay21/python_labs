ages = {
    'Matt': 30,
    'Katie': 29,
    'Nik': 31,
    'Jack': 43,
    'Alison': 72,
    'Kevin': 38
}

#max_value = max(ages, key=ages.get)
#print(max_value)

#  bids = {'Jon': 16, 'Brian': 45, 'Ivan': 12}

max_bidder = max(ages, key=lambda k: ages[k])
print(max_bidder)

print(f"The maximum bid is {ages[max_bidder]} by {max_bidder}")

# Jack