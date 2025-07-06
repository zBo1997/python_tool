# Milvus 向量搜索演示

这个项目展示了如何使用 Milvus 向量数据库进行文本嵌入和语义搜索。通过将文本转换为高维向量，并利用 Milvus 的向量搜索能力，可以实现基于语义的相似度搜索。

## 项目概述

本演示项目使用 PyMilvus 客户端连接到本地 Milvus 数据库，将文本数据转换为向量并存储，然后执行向量相似度搜索。这种技术常用于：

- 语义搜索引擎
- 推荐系统
- 相似文档检索
- 问答系统

## 功能特点

- 使用 PyMilvus 客户端连接本地数据库
- 创建向量集合并设置维度
- 使用默认嵌入函数将文本转换为向量
- 将文本数据和对应的向量插入到 Milvus 集合中
- 执行向量相似度搜索查询

## 安装指南

### 前提条件

- Python 3.6+
- pip 包管理器

### 安装依赖

```bash
pip install pymilvus
```

## 使用说明

1. 克隆此仓库或下载代码文件
2. 确保已安装所有依赖
3. 运行示例代码：

```bash
python milvus_demo.py
```

## 代码示例解析

### 连接到 Milvus 数据库

```python
from pymilvus import MilvusClient

client = MilvusClient("milvus_demo.db")
```

### 创建集合

```python
client.create_collection(
    collection_name="demo_collection",
    dimension=768,  # 向量维度为768
)
```

### 文本嵌入

```python
from pymilvus import model

embedding_fn = model.DefaultEmbeddingFunction()

docs = [
    "Artificial intelligence was founded as an academic discipline in 1956.",
    "Alan Turing was the first person to conduct substantial research in AI.",
    "Born in Maida Vale, London, Turing was raised in southern England.",
]

vectors = embedding_fn.encode_documents(docs)
```

### 数据插入

```python
data = [
    {"id": i, "vector": vectors[i], "text": docs[i], "subject": "history"}
    for i in range(len(vectors))
]

res = client.insert(collection_name="demo_collection", data=data)
```

### 向量搜索

```python
query_vectors = embedding_fn.encode_queries(["Who is Alan Turing?"])

res = client.search(
    collection_name="demo_collection",
    data=query_vectors,
    limit=2,
    output_fields=["text", "subject"],
)
```

## 依赖项

- [PyMilvus](https://github.com/milvus-io/pymilvus): Milvus 的 Python 客户端
- [Milvus](https://milvus.io/): 开源向量数据库，专为嵌入相似度搜索和 AI 应用设计

## 进阶使用

- 尝试使用不同的嵌入模型
- 增加更多的文本数据
- 调整搜索参数以优化结果
- 实现更复杂的查询逻辑

## 许可证

请参阅项目许可证文件。
