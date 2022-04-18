import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from tqdm.notebook import tqdm


def articles_analysic():
    """
    此表包含所有h&m文章，详细信息包括产品类型、颜色、产品组和其他功能。
    文章数据描述：
    article_id : 每件article的唯一标识符.
    product_code, prod_name : 每个产品及其名称的唯一标识符（不同）
    product_type, product_type_name : 产品代码组及其名称
    graphical_appearance_no, graphical_appearance_name : 图形组及其名称
    colour_group_code, colour_group_name : 颜色组及其名称
    perceived_colour_value_id, perceived_colour_value_name,
    perceived_colour_master_id, perceived_colour_master_name
    : 添加的颜色信息
    department_no, department_name: : 每个dep及其名称的唯一标识符
    index_code, index_name: : 每个索引及其名称的唯一标识符
    index_group_no, index_group_name: : 一组索引及其名称
    section_no, section_name: : 每个部分及其名称的唯一标识符
    garment_group_no, garment_group_name: : 每件衣服及其名称的唯一标识符
    detail_desc: : Details

    :return: void
    """
    # 获得前面 5个
    print(articles.head())

    # 查看index_name占比图
    f, ax = plt.subplots(figsize=(15, 7))
    ax = sns.histplot(data=articles, y='index_name', color='orange')
    ax.set_xlabel('count by index name')
    ax.set_ylabel('index name')
    plt.show()

    # 查看服装分类占比图
    f, ax = plt.subplots(figsize=(15, 7))
    ax = sns.histplot(data=articles, y='garment_group_name', color='orange', \
                      hue='index_group_name', multiple="stack")
    ax.set_xlabel('count by garment group')
    ax.set_ylabel('garment group')
    plt.show()

    # 类比和服装分类占比分组
    print(articles.groupby(['index_group_name', 'index_name']).count()['article_id'])

    # 查看产品结构图, 如裤子、背包、帽子分类数量
    pd.options.display.max_rows = None
    print(articles.groupby(['product_group_name', 'product_type_name']).count()['article_id'])

    # 列中具有唯一值的表
    unique_str = ['no', 'code', 'id']
    for col in articles.columns:
        if not 'no' in col and not 'code' in col and not 'id' in col:
            un_n = articles[col].nunique()
            print(f'n of unique {col}: {un_n}')

def customer_analysic():
    """
    customer_id : 每个客户的唯一标识符
    FN : 1 or missed
    Active : 1 or missed
    club_member_status : Status in club
    fashion_news_frequency : H&M向客户发送新闻的频率
    age : The current age
    postal_code : 客户的邮政编码
    :return: void
    """
    pd.options.display.max_rows = 50
    print(customers.head())

    # There are no duplicates(重复) in customer
    print(customers.shape[0] - customers['customer_id'].nunique())




if __name__ == '__main__':
    # 让我们看看表格，并尝试获得一些关于内部数据的结果。
    articles = pd.read_csv("../../H&M competition/articles.csv")
    customers = pd.read_csv("../../H&M competition/customers.csv")
    # transaction = pd.read_csv("../../H&M competition/transactions_train.csv")

    articles_analysic()


