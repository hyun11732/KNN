# KNN

KNN is one of basic but powerful clustering algorithm.
Its algorithm is very simple.
It simply counts K number of the closest neighbors and label the point with the most common label of its neighbors.
However, the problem is as the number of point increases, the performance of this algorithm gets slower.
It will take O(nm) n= the number of training points, m = the number of testing points since we need to search all points in training for a test point.
There is more faster way to find the closest points by using KD-Tree.
KD-Tree is a good data structure using a tree and able to find the closest tree in the max time in O(h) when h is the height of the tree.
However, unfortunately, I could not implement KD-tree because I did not have enough time.
I will update KD-tree version later for sure!

Another mistake I made. I should use dictionary instead of list when I store point and label data to make it faster.
I made point and label lists separately and caused inefficiency. 
