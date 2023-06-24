import os
from llama_index import VectorStoreIndex, SimpleDirectoryReader

print ("0 test")

os.environ["OPENAI_API_KEY"] = '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'
print ("first test")


documents = SimpleDirectoryReader("data").load_data()
print("second test")

index = VectorStoreIndex.from_documents(documents)

print ("third test")


query_engine = index.as_query_engine()
print ("fourth test")
out = query_engine.query("what is a test")

print ("test")                      
print (out)                        




