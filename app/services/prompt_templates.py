LEAD_QUALIFICATION_PROMPT = """You are a B2B lead qualification analyst. Analyze the lead below and respond with ONLY valid JSON, no other text.

Lead Info:
Name: {name}
Email: {email}
Phone: {phone}
Company: {company}
Designation: {designation}
Industry: {industry}
Employees: {employees}
Country: {country}
Source: {source}
Message: {message}

Return ONLY this JSON structure (no markdown, no explanation):
{{
  "lead_score": <int 0-100>,
  "priority": "<HOT|WARM|COLD>",
  "buying_intent": "<High|Medium|Low>",
  "intent": "<short string>",
  "company_size": "<string>",
  "estimated_deal_size": "<string>",
  "pain_points": ["<string>", "..."],
  "recommended_next_action": "<string>",
  "sales_summary": "<1-2 line string>",
  "confidence_score": <float 0-1>
}}"""