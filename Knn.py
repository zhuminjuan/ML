# coding=utf-8
from numpy import *
import loadData


# 随机划分训练集
# input：带类标的数据集（类标是最后的m个）, 训练集占比
def splitData(data_set, split):
    train_list = []
    test_list = []
    train_label = []
    test_label = []
    # 按照比例随机分隔训练集和测试集
    for data in data_set:
        if random.random() < split:
            train_list.append(data[:-1])
            train_label.append(data[-1])
        else:
            test_list.append(data[:-1])
            test_label.append(data[-1])
    return train_list, train_label, test_list, test_label


# KNN分类算法
# test_input 待分类数据集
# data_set 训练数据集
# label 训练数据对应的标签
# k k近邻，选择近邻的数据个数
def knnClassify(test_inputs, data_set, label, k):
    data_set_size = len(data_set)
    result_label = []
    if len(test_inputs) == 0 or data_set_size == 0:
        return result_label

    for test_input in test_inputs:
        # tile
        # tile(A,(2,3))
        # [[A,A，A], [A,A,A]]
        diff = tile(test_input, (data_set_size, 1)) - data_set
        squared_diff = diff ** 2
        squared_dist = sum(squared_diff, axis=1)
        distance = squared_dist ** 0.5

        sorted_dist_indices = argsort(distance)

        class_count = {}
        for i in xrange(k):
            vote_label = label[sorted_dist_indices[i]]
            class_count[vote_label] = class_count.get(vote_label, 0) + 1
        max_count = 0
        for key, value in class_count.items():
            if value > max_count:
                max_count = value
                max_index = key
        result_label.append(max_index)
    return result_label


# 计算精确度
def accuracy(real, predict):
    acc_cnt = 0
    total_cnt = 0
    for label in real:
        # print label,predict[total_cnt]
        if label == predict[total_cnt]:
            # print label, predict_res[total_cnt]
            acc_cnt += 1
        total_cnt += 1
    return acc_cnt / float(total_cnt)


# 读取数据集
dataSet = loadData.readData("data/titanic.dat")
# 划分训练集和测试集
train_data, train_labels, test_data, test_labels = splitData(dataSet, 0.7)
# k = 1, 3, 5, 7, 9时KNN的精确度
# range (i,j,k)   i , i + k,...,i+nk<j
for i in range(1, 8, 2):
    predict_res = knnClassify(test_data, train_data, train_labels, i)
    print "k =", i, "accuracy rate is", accuracy(test_labels, predict_res)
