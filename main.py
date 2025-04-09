import typer
from async_typer import AsyncTyper
from models.client_details import ClientDetails
from markitdown import MarkItDown
from pathlib import Path
from pprint import pprint

app = AsyncTyper()
md = MarkItDown()

@app.async_command()
async def extract(
    data_path:Path=typer.Option("data")
):
    # Init workflow 
    from workflow.extract import ExtractWorkFlow
    workflow = ExtractWorkFlow(timeout=400)
    
    # Extract text out
    data = ''.join([md.convert(str(d)).text_content for d in list(data_path.glob("*"))])
    
    query = """
        Your an ai asistant task is a Named Entity Recognition (NER) task. 
        Predict the category of each entity, then place the entity into the list associated with the category in an output JSON payload.
        Entities to extract: {text}
    """
    results = await workflow.run(
        schema=ClientDetails, text=data, query=query
    )
    pprint(results.model_dump())

@app.async_command()
async def extract_rag(data_path:Path=typer.Option("data")):
    # Init workflow 
    from workflow.extract import ExtractRAGWorkflow
    workflow = ExtractRAGWorkflow(timeout=400)

    # Extract text out
    data = ''.join([md.convert(str(d)).text_content for d in list(data_path.glob("*"))])
    
    query = """
        Your an ai asistant task is a Named Entity Recognition (NER) task. 
        Predict the category of each entity, then place the entity into the list associated with the category in an output JSON payload.
        Entities to extract: {text}
    """
    results = await workflow.run(
        schema=ClientDetails, text=data, query=query
    )
    pprint(results.model_dump())
    
if __name__ == "__main__":
    app()