import typer
from client_details import ClientDetails
import json
import os
import logging

logging.basicConfig(level=logging.INFO)
app = typer.Typer()

def write_json(json_path, data):
    with open(json_path, 'w') as jsonf:
        json.dump(data, jsonf, indent=4)

@app.command()
def main(outpath:str=typer.Option('./schema')):
    if not os.path.exists(outpath):
        logging.info('Creating {}'.format(outpath))
        os.makedirs(outpath)
    
    query = """
        Your an ai asistant task is a Named Entity Recognition (NER) task. 
        Predict the category of each entity, then place the entity into the list associated with the category in an output JSON payload.
        Entities to extract: {text}
    """
    logging.info('Exporting Schema: {}'.format(ClientDetails.__name__))
    write_json(os.path.join(outpath, 'schema.json'), {
        '{}'.format(ClientDetails.__name__): {
            "query": query, 'schema': ClientDetails.schema()
        }
    })

if __name__ == "__main__":
    app()