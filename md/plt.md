# plt



#### plt.subplots

其中figsize用来设置图形的大小，a为图形的宽， b为图形的高，单位为英寸。

但是如果使用plt.subplots，就不一样了。

```python
fig, ax = plt.subplots(figsize = (a, b))
```

fig代表绘图窗口(Figure)；ax代表这个绘图窗口上的坐标系(axis)，一般会继续对ax进行操作。

> fig, ax = plt.subplots()等价于：
>
> - fig = plt.figure()
> - ax = fig.add_subplot(1, 1, 1)

exp

```python
f, ax = plt.subplots(figsize=(15, 7))
ax = sns.histplot(data=articles, y='garment_group_name', color='orange', \
   			hue='index_group_name',multiple="stack")
ax.set_xlabel('count by garment group')
ax.set_ylabel('garment group')
plt.show()
```



















