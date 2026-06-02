from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)
print("OPENAI_API_KEY =", os.getenv("OPENAI_API_KEY"))
def summarize(errors):

    prompt = f"""
    Analyze these log errors.

    Provide:
    1. Root cause
    2. Frequency pattern
    3. Troubleshooting steps

    Errors:
    {errors}
    """

    response = client.responses.create(
        model="gpt-5",
        input=prompt
    )

    return response.output_text