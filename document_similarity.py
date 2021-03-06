import math
import sys
import os
def read_file(filename):
    """ 
    read text file and return text lines
    """
    f = open(filename,'r')
    return f.readlines()

def get_words_from_line(L):
    word_list = []
    for line in L:
        words_in_line = get_words_from_string(line)
        word_list = word_list + words_in_line
    return word_list

def get_words_from_string(line):
    """
    convertt each word to lower case and return list
    """
    word_list = []    
    character_list = []
    for x in line:
        if x.isalnum():
            character_list.append(x)
        elif len(character_list)>0:
            word = "".join(character_list)
            word = word.lower()
            word_list.append(word)
            character_list = []
    if len(character_list)>0:
        word = "".join(character_list)
        word = word.lower()
        word_list.append(word)
    return word_list

# count frequency
def count_frequency(words):
    L = []
    for word in words:
        for p in L:
            if word == p[0]:
                p[1] = 1+p[1]
                break
        else:
            L.append([word,1])
    return L

#sorting
def insertion_sort(A):
    #insertion sort implementation
    for j in range(len(A)):
        key = A[j]
        i = j-1
        while i>-1 and A[i]>key:
            A[i+1] = A[i]
            i = i-1
        A[i+1] = key
    return A
    
def word_frequencies(filename):
    
    line_list = read_file(filename)
    word_list = get_words_from_line(line_list)
    freq = count_frequency(word_list)
    insertion_sort(freq)
    return freq

def inner_product(L1,L2):
    """
    vectors are represented as lists of (word,frequency) pairs
    """
    sum = 0.0
    for word1, count1 in L1:
        for word2, count2 in L2:
            if word1 == word2:
                sum += count1 * count2
    return sum

def vector_angle(L1,L2):
    """
    return the angle between two vectors.
    """
    numerator = inner_product(L1,L2)
    denominator = math.sqrt(inner_product(L1,L1)*inner_product(L2,L2))
    return math.acos(numerator/denominator)

def main():
    if len(sys.argv) != 3:
        print "Usage: document_similarity.py file1 file2"
    else:
        file1 = sys.argv[1]
        file2 = sys.argv[2]
        f1= word_frequencies(file1)
        f2 = word_frequencies(file2)
        distance = vector_angle(f1,f2)
        print "the similarity distance between the documents is: %0.4f (radians)"%distance

if __name__ == "__main__":
    import profile
    profile.run("main()")
