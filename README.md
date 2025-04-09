# Extraction API using LLamaindex
Structured data extraction using pydantic and llama-index to define the structure and using openai as an example to extract
As a bonus you can chain it with a rag model

Take a look at the file struct here to get an understanding
```bash
models/client_details.py
```

You can define it with a field where 
a) you can use a default value
b) description, explaining to the AI what relevent fields you want to extract
```python
from pydantic import BaseModel, Field
from typing import Optional

class PersonalDetails(BaseModel):
    title: Optional[str] = Field(default="mr", description="The Person's title. E.g: Mr/Mrs/Ms")
    salutation: Optional[str] = Field(default="mr smith", description="The Person's preferred salutation if known. E.g: Mr. Smith")
    first_name: Optional[str] = Field(default="", description="First Name. E.g: Smith")
```

- Therefore when the output model you can have a json following what you defined

# Install
- Lets first start by installing dependecies
```bash
pip install -r requirements.txt
```

- Dont forget to export your openai key
```bash
export OPENAI_KEY=key
```

# Running Extraction
- Run pure extraction
```bash
python main.py extract
```

- Run extraction with RAG model
```bash
python main.py extract-rag
```

# Export the pydantic structure as a json for viewing
```bash
python models/export.py
```