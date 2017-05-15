# coding=utf-8


# 数据读取与处理
# input 文件路径
# output 带标签的数据集
def readData(file_path):
    # 数据归一化处理
    class_min = -1.87
    class_max = 0.965
    class_diff = class_max - class_min

    age_min = -0.228
    age_max = 4.38
    age_diff = age_max - age_min

    sex_min = -1.92
    sex_max = 0.521
    sex_diff = sex_max - sex_min

    data_set = []
    with open(file_path, 'r') as f:
        line = f.readline()
        while line:
            if line[0] != '@':
                datas = line.strip().split(",")
                datas[0] = (float(datas[0]) - class_min) / class_diff
                datas[1] = (float(datas[1]) - age_min) / age_diff
                datas[2] = (float(datas[2]) - sex_min) / sex_diff
                data_set.append(datas[:])
            line = f.readline()
    return data_set
