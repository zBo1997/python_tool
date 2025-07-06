from pymilvus import model
from pymilvus import MilvusClient

client = MilvusClient("milvus_demo.db")

# Create a collection named "demo_collection" if it does not exist.
if client.has_collection(collection_name="demo_collection"):
    client.drop_collection(collection_name="demo_collection")
client.create_collection(
    collection_name="demo_collection",
    dimension=768,  # The vectors we will use in this demo has 768 dimensions
)


embedding_fn = model.DefaultEmbeddingFunction()

docs1 = [
    "Artificial intelligence was founded as an academic discipline in 1956.",
    "Alan Turing was the first person to conduct substantial research in AI.",
    "Born in Maida Vale, London, Turing was raised in southern England.",
]

vectors = embedding_fn.encode_documents(docs1)
# Print the dimension of the embedding function and the shape of the first vector  Dim: 768 (768,)
print("Dim:", embedding_fn.dim, vectors[0].shape)

data = [
    {"id": i, "vector": vectors[i], "text": docs1[i], "subject": "history"}
    for i in range(len(vectors))
]

print("Data has", len(data), "entities, each with fields: ", data[0].keys())
print("Vector dim:", len(data[0]["vector"]))

# Insert data into Milvus
res = client.insert(collection_name="demo_collection", data=data)



# Add more data to the same collection
docs2 = [
    "Machine learning has been used for drug design.",
    "Computational synthesis with AI algorithms predicts molecular properties.",
    "DDR1 is involved in cancers and fibrosis.",
]
vectors = embedding_fn.encode_documents(docs2)
data = [
    {"id": 3 + i, "vector": vectors[i], "text": docs2[i], "subject": "biology"}
    for i in range(len(vectors))
]

client.insert(collection_name="demo_collection", data=data)

query_vectors = embedding_fn.encode_queries(["Who is Alan Turing?"])

# Search for similar entities in Milvus
res1 = client.search(
    collection_name="demo_collection",  # target collection
    data=query_vectors,  # query vectors
    limit=2,  # number of returned entities
    output_fields=["text", "subject"],  # specifies fields to be returned
)

# search with Metadata filter
res2 = client.search(
    collection_name="demo_collection",
    data=embedding_fn.encode_queries(["tell me AI related information"]),
    filter="subject == 'biology'",
    limit=2,
    output_fields=["text", "subject"],
)

#res1 about Alan Turing ,res2 about biology
print("Search results:")
print(f'reset1: {res1}')
print(f'reset2: {res2}')

