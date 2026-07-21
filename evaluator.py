import json

from config import client, model
from schemas import JobD, MatchResult
from prompts import JOB_PARSER_PROMPT, MATCH_PROMPT

jobd_schema = JobD.model_json_schema()
match_schema = MatchResult.model_json_schema()

def parse_job_description(job_description):
    system_prompt = JOB_PARSER_PROMPT.format(
        schema_job=jobd_schema
    )

    user_prompt = f"""
    Analyze the following job description:
    {job_description}
    """
    message_system={
        "role" : "system",
        "content" : system_prompt
    }
    message_user={
        "role" : "user",
        "content" : user_prompt
    }
    response_format={
        "type" : "json_object"
    }

    messages=[message_system, message_user]

    response=client.chat.completions.create(model=model, messages=messages, response_format=response_format)

    answer=response.choices[0].message.content

    job_data=json.loads(answer) #converts raw_json to Python dictionary.

    job = JobD(**job_data)  #creates a Pydantic object
    return job
    #print(job.minimum_experience)
    #print(job.education_requirements)

def final_score(job,resume):
    
    prompt = MATCH_PROMPT.format(
        job=job.model_dump_json(indent=2),
        resume=resume.model_dump_json(indent=2),
        schema_match=match_schema
    )
    message={
        "role": "user",
        "content" : prompt
    }
    messages=[message]
    response_format={
        "type": "json_object"
    }
    response = client.chat.completions.create(model=model, messages=messages, response_format=response_format)
    data = json.loads(response.choices[0].message.content)
    return MatchResult(**data)
