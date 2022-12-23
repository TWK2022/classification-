import os
import numpy as np
import pandas as pd


def data_get(args):
    data_dict = data_prepare(args)._load()
    return data_dict


class data_prepare(object):
    def __init__(self, args):
        self.args = args

    def _load(self):
        data_dict = {}
        data_dict['train'] = self._load_train()
        data_dict['val'] = self._load_val()
        data_dict['class'] = self._load_class()
        return data_dict

    def _load_train(self):
        with open(self.args.data_path + '/' + 'train.txt')as f:
            txt = [_.strip().split(' ') for _ in f.readlines()]
        data_list = [[0, 0] for _ in range(len(txt))]
        for i in range(len(txt)):
            data_list[i][0] = txt[i][0]
            data_list[i][1] = np.zeros(self.args.output_class, dtype=np.float32)
            for j in txt[i][1:]:
                data_list[i][1][int(j)] = 1
        return data_list

    def _load_val(self):
        with open(self.args.data_path + '/' + 'train.txt')as f:
            txt = [_.strip().split(' ') for _ in f.readlines()]
        data_list = [[0, 0] for _ in range(len(txt))]
        for i in range(len(txt)):
            data_list[i][0] = txt[i][0]
            data_list[i][1] = np.zeros(self.args.output_class, dtype=np.float32)
            for j in txt[i][1:]:
                data_list[i][1][int(j)] = 1
        return data_list

    def _load_class(self):
        cls = pd.read_csv(self.args.data_path + '/' + 'class.csv', header=None).values.tolist()
        return cls


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--data_path', default='../dataset/classification/mask', type=str)
    parser.add_argument('--input_size', default=640, type=int)
    args = parser.parse_args()
    data_dict = data_get(args)
