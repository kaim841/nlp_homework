# 代码核心功能说明
## 1. 数据预处理
### 1.1 提取单词并过滤无效字符
函数 `get_words` 用于读取邮件文本文件，提取单词并过滤无效字符和长度为1的词。

```python
def get_words(filename):
    """读取文本并过滤无效字符和长度为1的词"""
    words = []
    with open(filename, 'r', encoding='utf-8') as fr:
        for line in fr:
            line = line.strip()
            # 过滤无效字符
            line = re.sub(r'[.【】0-9、——。，！~\*]', '', line)
            # 使用 jieba.cut() 方法对文本切词处理
            line = cut(line)
            # 过滤长度为1的词
            line = filter(lambda word: len(word) > 1, line)
            words.extend(line)
    return words
```

- **功能**：
  - 使用正则表达式过滤无效字符（如标点符号、数字等）。
  - 使用 `jieba.cut` 对文本进行分词。
  - 过滤掉长度为1的词（如“的”、“了”等无意义的词）。

### 1.2 提取高频词
函数 `get_top_words` 遍历所有邮件，统计词频并返回出现次数最多的 `top_num` 个词。

```python
def get_top_words(top_num):
    """遍历邮件建立词库后返回出现次数最多的词"""
    filename_list = ['邮件_files/{}.txt'.format(i) for i in range(151)]
    # 遍历邮件建立词库
    for filename in filename_list:
        all_words.append(get_words(filename))
    # itertools.chain() 把 all_words 内的所有列表组合成一个列表
    # collections.Counter() 统计词个数
    freq = Counter(chain(*all_words))
    return [i[0] for i in freq.most_common(top_num)]
```

- 功能：
  - 遍历所有邮件文件，提取单词。
  - 使用 `Counter` 统计词频，返回出现次数最多的词。

## 2. 特征向量构建
将每封邮件转换为一个特征向量，表示邮件中每个高频词的出现次数。

```python
top_words = get_top_words(100)
vector = []
for words in all_words:
    word_map = list(map(lambda word: words.count(word), top_words))
    vector.append(word_map)
vector = np.array(vector)
```

- **功能**：
  - 对每封邮件，统计 `top_words` 中每个词的出现次数。
  - 将所有邮件的向量组合成一个矩阵 `vector`。

## 3. 模型训练
使用朴素贝叶斯算法训练分类器。

```python
# 标签：前127封邮件为垃圾邮件（1），后24封邮件为普通邮件（0）
labels = np.array([1]*127 + [0]*24)
model = MultinomialNB()
model.fit(vector, labels)
```

- **功能**：
  - 定义邮件的标签（垃圾邮件或普通邮件）。
  - 使用 `MultinomialNB` 训练分类器。

## 4. 预测
对未知邮件进行分类。

```python
def predict(filename):
    """对未知邮件分类"""
    # 构建未知邮件的词向量
    words = get_words(filename)
    current_vector = np.array(
        tuple(map(lambda word: words.count(word), top_words)))
    # 预测结果
    result = model.predict(current_vector.reshape(1, -1))
    return '垃圾邮件' if result == 1 else '普通邮件'
```

- **功能**：
  - 提取未知邮件的单词列表。
  - 将单词列表转换为特征向量。
  - 使用训练好的模型进行预测，返回分类结果。

## 5. 代码运行
对几封未知邮件进行分类预测。

```python
print('151.txt分类情况:{}'.format(predict('邮件_files/151.txt')))
print('152.txt分类情况:{}'.format(predict('邮件_files/152.txt')))
print('153.txt分类情况:{}'.format(predict('邮件_files/153.txt')))
print('154.txt分类情况:{}'.format(predict('邮件_files/154.txt')))
print('155.txt分类情况:{}'.format(predict('邮件_files/155.txt')))
```

<img src="img.png" width="800" alt="截图一">

# 增加模型评估指标，代码在文件py1.py

<img src="img_1.png" width="800" alt="截图二">