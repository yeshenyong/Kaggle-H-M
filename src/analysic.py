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

    # 获得邮编相同customers
    data_postal = customers.groupby('postal_code', as_index=False)\
        .count().sort_values('customer_id', ascending=False)

    print(data_postal.head())

    # Ages, club_member_status are different, like customer_ids.
    print(customers[customers['postal_code']=='2c29ae653a9282cce4151bd87643c90' \
                                '7644e09541abc28ae87dea0d1f6603b1c'].head())

    # The Most common age is about 21-23
    sns.set_style("darkgrid")
    f, ax = plt.subplots(figsize=(10, 5))
    ax = sns.histplot(data=customers, x='age', bins=50, color='orange')
    ax.set_xlabel('Distribution of the customers age')
    plt.show()

    # Status in H&M club. Almost every customer has an active club status,
    # some of them begin to activate it (pre-create).
    # A tiny part of customers abandoned the club.
    sns.set_style('darkgrid')
    f, ax = plt.subplots(figsize=(10, 5))
    ax = sns.histplot(data=customers, x='club_member_status', color='orange')
    ax.set_xlabel('Distribution of club member status')
    plt.show()

    # Monthly Regularly None
    sns.set_style('darkgrid')
    f, ax = plt.subplots(figsize=(10, 5))
    ax = sns.histplot(data=customers, x='fashion_news_frequency', color='orange')
    ax.set_xlabel('Distribution of fashion_news_frequency')
    plt.show()

    # Here we have three types for No DATA. Let's unite these values.
    print(customers['fashion_news_frequency'].unique())
    # array(['NONE', 'Regularly', nan, 'Monthly', 'None'], dtype=object)
    # 除了isin 的数据, 其他都是None
    customers.loc[~customers['fashion_news_frequency'].isin
        (['Regularly', 'Monthly']), 'fashion_news_frequency'] = 'None'
    print(customers['fashion_news_frequency'].unique())
    # array(['None', 'Regularly', 'Monthly'], dtype=object)
    pie_data = customers[['customer_id', 'fashion_news_frequency']].groupby('fashion_news_frequency').count()

    # Customers prefer not to get any messages about the current news.
    sns.set_style("darkgrid")
    f, ax = plt.subplots(figsize=(10, 5))
    # ax = sns.histplot(data=customers, x='fashion_news_frequency', color='orange')
    # ax = sns.pie(data=customers, x='fashion_news_frequency', color='orange')
    colors = sns.color_palette('pastel')
    ax.pie(pie_data.customer_id, labels=pie_data.index, colors=colors)
    ax.set_facecolor('lightgrey')
    ax.set_xlabel('Distribution of fashion news frequency')
    plt.show()


def transaction_analysic():
    """
    t_dat : A unique identifier of every customer
    customer_id : A unique identifier of every customer (in customers table)
    article_id : A unique identifier of every article (in articles table)
    price : Price of purchase
    sales_channel_id : 1 or 2
    :return: void
    """
    print(transaction.head())

    # Here we see outliers for price.
    pd.set_option('display.float_format', '{:.4f}'.format)
    print(transaction.describe()['price'])  # series describe

    print(transaction.head())

    # price Distribution
    sns.set_style("darkgrid")
    f, ax = plt.subplots(figsize=(10, 5))
    ax = sns.boxplot(data=transaction, x='price', color='orange')
    ax.set_xlabel('Price outliers')
    plt.show()

    # Top 10 customers by num of transactions
    transaction_byid = transaction.groupby('customer_id').count()
    print(transaction_byid.sort_values(by='price', ascending=False)['price'][:10])

    # Get subset from articles and merge it to transactions.
    articles_for_merge = articles[['article_id', 'prod_name', 'product_type_name',
                                   'product_group_name', 'index_name']]
    articles_for_merge = transaction[['customer_id', 'article_id', 'price',
                                      't_dat']].merge(articles_for_merge,
                                                      on='article_id', how='left')
    # Here we see outliers for group name prices.
    # Lower/Upper/Full body have a huge price variance.
    sns.set_style("darkgrid")
    f, ax = plt.subplots(figsize=(25, 18))
    _ = articles_for_merge[articles_for_merge['product_group_name'] == 'Accessories']
    ax = sns.boxplot(data=_, x='price', y='product_type_name')
    ax.set_xlabel('Price outliers', fontsize=22)
    ax.set_ylabel('Index names', fontsize=22)
    ax.xaxis.set_tick_params(labelsize=22)
    ax.yaxis.set_tick_params(labelsize=22)
    del _
    plt.show()

    # The index with the highest mean price is Ladieswear.
    # With the lowest - children.
    articles_index = articles_for_merge[['index_name', 'price']].groupby('index_name').mean()
    sns.set_style("darkgrid")
    f, ax = plt.subplots(figsize=(10, 5))
    ax = sns.barplot(x=articles_index.price, y=articles_index.index, color='orange', alpha=0.8)
    ax.set_xlabel('Price by index')
    ax.set_ylabel('Index')
    plt.show()

if __name__ == '__main__':
    # 让我们看看表格，并尝试获得一些关于内部数据的结果。
    articles = pd.read_csv("../../H&M competition/articles.csv")
    customers = pd.read_csv("../../H&M competition/customers.csv")
    # transaction = pd.read_csv("../../H&M competition/transactions_train.csv") # too large

    articles_analysic()
    customer_analysic()
    # transaction_analysic()

