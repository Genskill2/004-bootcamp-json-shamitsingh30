# Add the functions in this file
import json
import math

def load_journal(foo):
    with open(foo) as f:
        data = json.load(f)
    return data
    
def compute_phi(foo, event):
    data = load_journal(foo)
    n1 , n2, n3, n4, n5, n6, n7, n8 = 0,0,0,0,0,0,0,0
    for dictionary in data:
        if (event in dictionary['events'] and dictionary['squirrel']==True):
            n1 = n1 + 1
        if (event not in dictionary['events'] and dictionary['squirrel']==False):
            n2 = n2 + 1
        if (event in dictionary['events'] and dictionary['squirrel']==False):
            n3 = n3 + 1
        if (event not in dictionary['events'] and dictionary['squirrel']==True):
            n4 = n4 + 1
        if (event in dictionary['events']):
            n5 = n5 + 1
        if (event not in dictionary['events']):
            n6 = n6 + 1
        if (dictionary['squirrel']==True):
            n7 = n7 + 1
        if (dictionary['squirrel']==False):
            n8 = n8 + 1
    phi = ((n1 * n2) - (n3 * n4)) / math.sqrt(n5 * n6 * n7 * n8)
    return phi

def compute_correlations(foo):
    data = load_journal(foo)
    corr = {}
    for dictionary in data:
        for event in dictionary['events']:
            if event not in corr:
                corr[event] = compute_phi(foo, event)
    return corr
    
def diagnose(foo):
    data = load_journal(foo)
    corr = compute_correlations(foo)
    max_value = max(corr.values())
    min_value = min(corr.values())
    for key, value in corr.items():
        if value==max_value:
            likely = key
        elif value==min_value:
            unlikely = key 
    return likely, unlikely  

ans = diagnose('journal.json')
print(ans)
