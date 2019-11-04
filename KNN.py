import math

K = 3

#calculate distance between trees
def distance(point1, point2):
    dim = len(point1)
    dis = 0
    for i in range(dim):
        dis += (point1[i] - point2[i]) ** 2
    return math.sqrt(dis)

def K_nearest(train_matrix, test_matrix, label_vector):
    result = []
    for test_point in test_matrix:
        k_points = []
        distances = []
        idx = 0
        for train_point in train_matrix:
            temp = [tuple(train_point), label_vector[idx], distance(test_point, train_point)]
            distances.append(temp)
            idx += 1
        # Find k-nearest neighbor by smaller distance and label.
        k_neighbors = sorted(distances, key=lambda l: (l[2], l[1]))[:K]
        scores = dict()
        for neighbor in k_neighbors:
            label = neighbor[1]
            if label not in scores.keys():
                scores[label] = 1
            else:
                scores[label] += 1
        # Find the most label from K-nearest neighbors. If tie, use smaller label
        max_label = sorted(scores, key=lambda l: (-scores[l], l))[0]
        result.append(max_label)
    return result

if __name__ == "__main__":
    attri_dict = dict()
    test_matrix = []
    train_matrix = []
    label_vector = []
    label_dic = dict()
    string = input()
    values = string.split()
    label = values[0]
    for i in range(1, len(values)):
        temp = values[i].split(":")
        attri_dict[temp[0]] = i - 1
    train_row = 0
    test_row = 0
    labels = []
    # change the format of input to [(point1), (point2), (point3)], [label1, label2, label3]
    while string != "":
        values = string.split()
        label = values[0]
        if int(label) != 0:
            train_matrix.append([1] * len(attri_dict))
            label_vector.append(label)
            for i in range(1, len(values)):
                attr = values[i].split(":")
                train_matrix[train_row][attri_dict[attr[0]]] = float(attr[1])
            label_dic[tuple(train_matrix[train_row])] = label
            labels.append(label)
            train_row += 1
        else:
            test_matrix.append([1] * len(attri_dict))
            for i in range(1, len(values)):
                attr = values[i].split(":")
                test_matrix[test_row][attri_dict[attr[0]]] = float(attr[1])
            test_row += 1
        try:
            string = input()
        except:
            break
    labels = list(set(labels))
    KNN_values = K_nearest(train_matrix, test_matrix, label_vector)
    for value in KNN_values:
        print(value)
