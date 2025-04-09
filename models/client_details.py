from pydantic import BaseModel, Field
from typing import Optional

class PersonalDetails(BaseModel):
    title: Optional[str] = Field("", description="The Person's title. E.g: Mr/Mrs/Ms")
    salutation: Optional[str] = Field("", description="The Person's preferred salutation if known. E.g: Mr. Smith")
    first_name: Optional[str] = Field("", description="First Name. E.g: Smith")
    last_name: Optional[str] = Field("", description="Last Name. E.g: Rogers")
    maiden_name: Optional[str] = Field("", description="Maiden Name")
    middle_name: Optional[str] = Field("", description="The Person's middle name if they have one.")
    gender: Optional[str] = Field("Male", description="Gender. E.g: Male/Female")
    is_will_up_to_date: Optional[bool] = Field(False, description="Indicates if the person's will is up to date.")
    ni_number: Optional[str] = Field("", description="The Person's National Insurance number (in UK), Social Security Number (in US), or local equivalent.")
    date_of_birth: Optional[str] = Field("", description="Date of birth in YYYY-MM-DD format.")
    email: Optional[str] = Field("", description="Email")
    nationality: Optional[str] = Field("British", description="Nationality. E.g: British")
    marital_status: Optional[str] = Field("Single", description="Marital Status. E.g: Married/Single/Widowed")
    is_power_of_attorney_granted: Optional[bool] = Field(False, description="Indicates if power of attorney has been granted.")
    place_of_birth: Optional[str] = Field("London", description="Place of birth of the person. E.g: London/Manchester/Birmingham")
    country_of_birth: Optional[str] = Field("United Kingdom", description="Country of Birth. E.g: United Kingdom")
    marital_status_since: Optional[str] = Field("", description="Date since the marital status was established. YYYY-MM-DD")

class Address(BaseModel):
    address1: Optional[str] = Field("", description="Line 1 Address")
    address2: Optional[str] = Field("", description="Line 2 Address")
    address3: Optional[str] = Field("", description="Line 3 Address")
    address4: Optional[str] = Field("", description="")
    city: Optional[str] = Field("London", description="City")
    county: Optional[str] = Field("", description="County")
    country: Optional[str] = Field("GB", description="Country code. E.g: GB")
    postcode: Optional[str] = Field("AB12 3CD", description="Post Code")

class ClientDetails(BaseModel):
    personal_details: Optional[PersonalDetails] = Field(default_factory=PersonalDetails, description="")
    address: Optional[Address] = Field(default_factory=Address, description="")