from llama_index.core.workflow import (
    Context,
    Workflow,
    StartEvent,
    StopEvent,
    step,
)
from llama_index.core.workflow import Event
from llama_index.core.schema import NodeWithScore

class GenEvent(Event):
    """Result of running retrieval"""

    nodes: list[NodeWithScore]
    text:str

from llama_index.core.schema import Document
from llama_index.core import VectorStoreIndex
from llama_index.core.ingestion import IngestionPipeline
from llama_index.core.node_parser import MarkdownNodeParser
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import PromptTemplate
import os
from llama_index.llms.openai import OpenAI
import uuid

class ExtractWorkFlow(Workflow):
    os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_KEY", "")
    llm = OpenAI(model=os.getenv("OPENAI_MODEL", "gpt-4o"))
        
    @step
    async def extract(self, ctx: Context, ev: StartEvent) -> StopEvent | None:
        text = ev.get("text")
        schema = ev.get("schema")
        query = ev.get("query")
        
        prompt = PromptTemplate(query)
        result = self.llm.structured_predict(
            schema, prompt, text=text
        )
        
        return StopEvent(result=result)

class ExtractRAGWorkflow(Workflow):
    embedding_model = HuggingFaceEmbedding(model_name=os.getenv("EMBEDDING_MODEL", "BAAI/bge-base-en-v1.5"))
    os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_KEY", "")
    llm = OpenAI(model=os.getenv("OPENAI_MODEL", "gpt-4o"))
    
    node_parser = MarkdownNodeParser()
    pipeline = IngestionPipeline(
        transformations=[
            node_parser,
            embedding_model,
        ],
    )
    
    @step
    async def rag(self, ctx: Context, ev: StartEvent) -> GenEvent | None:
        text = ev.get("text")
        schema = ev.get("schema")
        query = ev.get("query")
        
        await ctx.set("schema", schema)
        await ctx.set("question", query)
        
        document = Document(doc_id=str(uuid.uuid4()), text=text)
        nodes = self.pipeline.run(documents=[document])
        index = VectorStoreIndex(nodes, embed_model=self.embedding_model)
        retriever = index.as_retriever(similarity_top_k=int(os.getenv("TOP_K", "20")))
        
        nodes = await retriever.aretrieve(query)
        return GenEvent(nodes=nodes, text=text)
    
    @step
    async def gen(self, ctx: Context, ev: GenEvent) -> StopEvent | None:
        schema = await ctx.get("schema", default=None)
        question = await ctx.get("question", default=None)
        
        text = ""
        for node in ev.nodes:
            text += node.text
        
        # sllm = self.openai_llm.as_structured_llm(pydantic_schema)
        prompt = PromptTemplate(question)
        result = self.llm.structured_predict(schema, prompt, text=text)
        
        return StopEvent(result=result)