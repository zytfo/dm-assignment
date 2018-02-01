# -*- coding: utf-8 -*-
'''
    Data Mining Assignment#1
    Khayaliev Artur
    Dataset: UNIX_user_data
'''
import numpy

def read_file():
    st = '/Users/zytfo/Desktop/University/DataMining/UNIX_user_data/USER'
    transactions = []
    arguments = ['<1>', '<2>', '<3>', '<4>']
    features = {}
    j = -1
    for i in range(9):
        with open(st + str(i), 'r') as file:
            for line in file:
                if '**SOF**' in line:
                    j += 1
                    transactions.append([])
                if '**EOF**' not in line and '**SOF**' not in line and line.rstrip() not in arguments:
                    transactions[j].append(line.rstrip())
                    if line.rstrip() not in features:
                        features[line.rstrip()] = []
                        features[line.rstrip()].append(j)
                    else:
                        features[line.rstrip()].append(j)
    return [transactions, features]


def calculate_support(features, number_of_transactions):
    supports = {}
    for f in features:
        supports[f] = features[f] / number_of_transactions
    return supports


def choose_features(number_of_transactions, features, min_support_threshold):
    supports = calculate_support(features, number_of_transactions)
    chosen_features = []
    for i in supports:
        if (supports[i] >= min_support_threshold):
            chosen_features.append(i)
    return chosen_features


def build_matrix(features, number_of_transactions):
    matrix = numpy.zeros((number_of_transactions, len(features)), dtype=bool) # rows, columns
    counter = 0
    for f in features:
        for i in range(len(features[f])):
            matrix[features[f][i]][counter] = True
        counter += 1
    return matrix
        
def write_csv(matrix, final_features):
    file = open('unix.csv', 'w')
    st = ''
    for f in final_features:
        st += f + ','
    st = st[:-1]
    file.write(st + '\n')
    for row in matrix:
        st = ''
        for i in row:
            if (i == True):                
                st += 'T,'
            else:
                st += 'F,'
        st = st[:-1]
        st += '\n'
        file.write(st)
    
def main():
    min_support_threshold = 0.005
    transactions, features = read_file()
    feature_transactions = {}
    for f in features:
        feature_transactions[f] = list(set(features[f]))
        features[f] = len(set(features[f])) # unique feature in transaction
    features = choose_features(len(transactions), features, min_support_threshold)
    final_features = {}
    for f in features:
        final_features[f] = feature_transactions[f]
    print(len(final_features))
    matrix = build_matrix(final_features, len(transactions))
    itemset = numpy.zeros((0, len(final_features)), dtype=bool)
    for row in matrix:
        flag = False
        for i in row:
            if (i == True):
                flag = True
                break
            else:
                flag = False
        if (flag == True):
            itemset = numpy.vstack([itemset, row])
        else:
            continue
    write_csv(itemset, final_features)
    
main()