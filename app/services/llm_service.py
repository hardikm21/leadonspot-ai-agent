import os
import json
from groq import Groq
from dotenv import load_dotenv
from app.services.prompt_templates import LEAD_QUALIFICATION_PROMPT

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def get_lead_qualification(lead) -> dict:
    prompt = LEAD_QUALIFICATION_PROMPT.format(
        name=lead.name,
        email=lead.email,
        phone=lead.phone,
        company=lead.company,
        designation=lead.designation,
        industry=lead.industry,
        employees=lead.employees,
        country=lead.country,
        source=lead.source,
        message=lead.message
    )

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    raw_text = response.choices[0].message.content.strip()

    if raw_text.startswith("```"):
        raw_text = raw_text.strip("`")
        raw_text = raw_text.replace("json", "", 1).strip()

    return json.loads(raw_text)