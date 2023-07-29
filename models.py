import google.generativeai as palm
from dotenv import load_dotenv
import os


load_dotenv()

palm.configure(api_key=os.environ.get("PALM_API_KEY"))


def generate_text_with_palm(prompt):
    models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
    model = models[0].name

    completion = palm.generate_text(
        model=model,
        prompt=prompt,
        temperature=0,
        max_output_tokens=800,
    )

    return completion.result