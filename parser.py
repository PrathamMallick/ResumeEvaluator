import json

from config import client, model
from schemas import Resume
from prompts import RESUME_PARSER_PROMPT

resume_schema = Resume.model_json_schema()
def parse_resume(resume_text):
    system_prompt = RESUME_PARSER_PROMPT.format(
        schema_resume=resume_schema
    )

    user_prompt = f"""
    Parse the following resume:
    {resume_text}
    """

    message_system={
        "role" : "system",
        "content" : system_prompt
    }
    message_user={
        "role" : "user",
        "content" : user_prompt
    }
    messages=[message_system, message_user]
    response_format={
        "type": "json_object"
    }
    response=client.chat.completions.create(model=model, messages=messages, response_format=response_format)
    raw_output = response.choices[0].message.content
    data = json.loads(raw_output)
    resume = Resume(**data) #creates a Pydantic object
    return resume #returns the Pydantic object
