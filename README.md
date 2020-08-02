# Document-Similarity
This program computes the "distance" between two text files as the angle between their word frequency vectors (in radians).

For each input file, a word-frequency vector is computed as :
->the specified file is read 
->it is converted into a list of alphanumeric "words". Here a "word" is a sequence of consecutive alphanumeric characters.
->for each word, its frequency of occurrence is determined
->the word/frequency lists are sorted into order alphabetically

The "distance" between two vectors is the angle between them. If x = (x1, x2, ..., xn) is the first vector (xi = freq of word i) and y = (y1, y2, ..., yn) is the second vector,then the angle between them is defined as: d(x,y) = arccos(inner_product(x,y) / (norm(x)*norm(y))) where:
inner_product(x,y) = x1*y1 + x2*y2 + ... xn*yn
norm(x) = sqrt(inner_product(x,x))
The code has been taken from MIT course of Algorithms. 

