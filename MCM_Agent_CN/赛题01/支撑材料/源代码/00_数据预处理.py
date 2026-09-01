# -*- coding: utf-8 -*-
"""
数据预处理：空白→0填充、有效样本筛选(85%-105%)、闭合归一化(至100%)、CLR变换
对应论文：2 数据预处理
"""
import pandas as pd
import numpy as np


def load_data(raw_path):
    """读取原始成分数据"""
    df = pd.read_excel(raw_path)  # 或其他格式
    return df


def fill_missing(df):
    """空白值填充：缺失→0，并做闭合修正"""
    df = df.fillna(0)
    return df


def filter_valid_samples(df, comp_cols, low=0.85, high=1.05):
    """有效样本筛选：成分和落在[85%,105%]才保留"""
    s = df[comp_cols].sum(axis=1)
    mask = (s >= low) & (s <= high)
    return df[mask]


def closed_normalize(df, comp_cols):
    """闭合归一化：各成分之和归一到100%"""
    return df[comp_cols].div(df[comp_cols].sum(axis=1), axis=0) * 100


def clr_transform(X):
    """中心对数比变换 CLR：消除成分数据闭合效应"""
    X = np.asarray(X, dtype=float)
    X = np.where(X == 0, np.finfo(float).eps, X)  # 避免log(0)
    geo_mean = np.exp(np.mean(np.log(X), axis=1, keepdims=True))
    return np.log(X / geo_mean)


if __name__ == "__main__":
    # 示例调用，请按实际数据路径修改
    pass
