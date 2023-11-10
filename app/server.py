from fastapi import FastAPI
from langserve import add_routes
from cassandra_entomology_rag import chain as cassandra_entomology_rag_chain

app = FastAPI()

# Edit this to add the chain you want to add

add_routes(app, cassandra_entomology_rag_chain, path="/cassandra-entomology-rag")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
