import csv

def consistent(hypothesis, instance):
    for x, y in zip(hypothesis, instance):
        if not (x == '?' or x == y):
            return False
    return True

def candidate_elimination(data):
    # Initialize boundaries
    S = data[0][:-1]
    G = [['?' for _ in range(len(S))]]
    
    for instance in data:
        if instance[-1] == 'Yes':  # Positive example
            for i in range(len(S)):
                if S[i] != instance[i]:
                    S[i] = '?'
        else:  # Negative example
            G = [g for g in G if not consistent(g, instance[:-1])]
    
    return S, G

# Example usage
with open('training.csv') as f:
    reader = csv.reader(f)
    data = list(reader)[1:]  # skip header
    S, G = candidate_elimination(data)
    print("Specific boundary:", S)
    print("General boundary:", G)
