from sklearn.datasets import load_iris


def iris_demo():
    """
    sklearn数据集使用
    :return:
    """

    iris = load_iris()
    print('鸢尾花数据集：\n', iris)
    print('查看描述：\n', iris['DESCR'])
    print('查看特征名：\n', iris.feature_names)
    print('查看特征值：\n', iris.data, iris.data.shape)
    return None


if __name__ == '__main__':
    iris_demo()
