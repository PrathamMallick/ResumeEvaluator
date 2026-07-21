# AI Resume Evaluator

An AI-powered resume screening tool that automatically parses resumes, extracts structured candidate information, and evaluates each candidate against a given job description using Large Language Models (LLMs).

## Features

- Extracts structured information from PDF and DOCX resumes
- Parses job descriptions into a structured format
- Compares resumes against job requirements
- Calculates an overall match score
- Highlights:
  - Matching skills
  - Missing skills
  - Experience match
  - Final hiring recommendation
- Ranks candidates based on their suitability for the role

## Project Structure

```text
resume_evaluator/
│
├── main.py
├── parser.py
├── evaluator.py
├── file_reader.py
├── prompts.py
├── schemas.py
├── config.py
├── resumes/
└── ...
```

## Tech Stack

- Python
- Groq API
- Pydantic
- python-docx
- pypdf
- python-dotenv
- JSON

## How it Works

1. Read resumes from the `resumes/` folder.
2. Extract text from PDF/DOCX files.
3. Parse resumes into structured JSON using an LLM.
4. Parse the job description into structured requirements.
5. Compare each resume against the job description.
6. Generate:
   - Match score
   - Matching skills
   - Missing skills
   - Final recommendation
7. Rank candidates based on their scores.

## Installation

Clone the repository

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
GROQ_API_KEY=your_api_key
```

Run the project:

```bash
python main.py
```

## Example Output

```
Processing Resume1.pdf
Completed: John Doe (91%)

Processing Resume2.pdf
Completed: Jane Smith (83%)

========== TOP CANDIDATES ==========

John Doe
Score: 91%

Jane Smith
Score: 83%
```

## Future Improvements

- Web interface using Streamlit or Flask
- Batch processing of hundreds of resumes
- Resume ranking dashboard
- ATS compatibility scoring
- Export results to Excel/CSV
- Support for additional resume formats

## What I Learned

While building this project, I realized that writing the initial functionality was only part of the challenge. As the codebase grew, maintaining a single large file became increasingly difficult.

To improve readability and maintainability, I refactored the project into a modular architecture by separating configuration, prompt templates, file parsing, schema definitions, evaluation logic, and the application entry point into dedicated modules. This made the code easier to understand, extend, and debug.
