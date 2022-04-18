## seaborn



```python
import seaborn as sns
```



### histplot

```python
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
```















