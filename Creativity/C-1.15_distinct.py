def distinct(odds):
    tempOdds = odds
    oddsToSet = set(odds)

    if len(tempOdds) == len(oddsToSet):
        return True
    else:
        return False

odds = [1,3,5,7,9]
print(distinct(odds))
