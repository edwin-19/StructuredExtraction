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

- Therefore when the output model you can have a json following what you defined, as defined below:
```json
{
    "personal_details": {
        "title": "",
        "salutation": "",
        "first_name": "test",
        "last_name": "test 2",
        "maiden_name": "",
        "middle_name": "",
        "gender": "Male",
        "is_will_up_to_date": true,
        "ni_number": "NP341350A",
        "date_of_birth": "1967-12-13",
        "email": "",
        "nationality": "British",
        "marital_status": "Living with partner",
        "is_power_of_attorney_granted": false,
        "place_of_birth": "London",
        "country_of_birth": "United Kingdom",
        "marital_status_since": ""
    },
    "address": {
        "address1": "",
        "address2": "",
        "address3": "",
        "address4": "",
        "city": "London",
        "county": "",
        "country": "GB",
        "postcode": "AB12 3CD"
    }
}
```

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