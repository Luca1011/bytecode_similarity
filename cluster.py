#!/usr/bin/python3
import sys

def jaccard_similarity(hv1, hv2):
    similarity = 0.9
    #TODO
    return similarity

def cluster(hv1, hv2, similarity):
    clusters = [[1,2,3], [2,4,6]]
    #TODO: If hv1 not already in a cluster then add new cluster containing hv1
    if similarity > 0.8:
        #Add hv2 to cluster containing hv1
        print("Happy holidays!")
    return clusters

def compare_hypervectors(filename):
    
    hypervectors = []

    with open(filename, 'r') as hv_file:
        for line in hv_file.read().splitlines():
            values = line.split(',')
            hypervectors.append(values)
      
        for i in hypervectors:
            for j in hypervectors[hypervectors.index(i)+1:]:
                similarity = jaccard_similarity(i, j)
                cluster(i, j, similarity)

        #with open("clusters.csv",'w') as output_file:
            #output_file.write(clusters)

    return


if __name__ == "__main__":
    
    if sys.argv[1] != None:
        compare_hypervectors(sys.argv[1])
