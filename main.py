import time
from pathlib import Path

from file_reader import read_resume
from parser import parse_resume
from evaluator import parse_job_description, final_score


# -----------------------------
# Job Description
# -----------------------------
job_description = """
Description
Do you want to solve real customer problems through innovative technology? Do you enjoy working on scalable services in a collaborative team environment? Do you want to see your code directly impact millions of customers worldwide?

At Amazon, we hire the best minds in technology to innovate and build on behalf of our customers. Customer obsession is part of our company DNA, which has made us one of the world's most beloved brands.

Our Software Development Engineers (SDEs) use modern technology to solve complex problems while seeing their work's impact first-hand. The challenges SDEs solve at Amazon are meaningful and influence millions of customers, sellers, and products globally. We seek individuals passionate about creating new products, features, and services while managing ambiguity in an environment where development cycles are measured in weeks, not years.

At Amazon, we believe in ownership at every level. As an SDE-I, you'll own the entire lifecycle of your code - from design through deployment and ongoing operations. This ownership mindset, combined with our commitment to operational excellence, ensures we deliver the highest quality solutions for our customers.

We're looking for curious minds who think big and want to define tomorrow's technology. At Amazon, you'll grow into the high-impact engineer you know you can be, supported by a culture of learning and mentorship. Every day brings exciting new challenges and opportunities for personal growth.
Key job responsibilities
• Collaborate and communicate effectively with experienced cross-disciplinary Amazonians to design, build, and operate innovative products and services that delight our customers, while participating in technical discussions to drive solutions forward.
• Design and develop scalable solutions using cloud-native architectures and microservices in a large distributed computing environment.
• Participate in code reviews and contribute to technical documentation.
• Build and maintain resilient distributed systems that are scalable, fault-tolerant, and cost-effective.
• Leverage and contribute to the development of GenAI and AI-powered tools to enhance development productivity while staying current with emerging technologies.
• Write clean, maintainable code following best practices and design patterns.
• Work in an agile environment practicing CI/CD principles while participating in operational responsibilities including on-call duties.
• Demonstrate operational excellence through monitoring, troubleshooting, and resolving production issues.
Basic Qualifications
- Experience with at least one general-purpose programming language such as Java, Python, C++, C#, Go, Rust, or TypeScript
- Experience with data structure implementation, basic algorithm development, and/or object-oriented design principles
- Currently has, or is in the process of obtaining a bachelor’s degree in Computer Science, Computer Engineering, Data Science, Information Systems, or related Engineering fields
- Must be 18 years of age of older
Preferred Qualifications
- Experience from previous technical internship(s) or demonstrated project experience
- Experience with one or more of the following: AI tools for development productivity, Cloud platforms (preferably AWS), Database systems (SQL and NoSQL), Contributing to open-source projects, Version control systems, Debugging and troubleshooting complex systems
- Demonstrated ability to learn and adapt to new technologies quickly
- Basic understanding of software development lifecycle (SDLC)
- Strong problem-solving and analytical skills
- Excellent written and verbal communication skills
"""


def main():
    # Parse the Job Description only once
    job = parse_job_description(job_description)

    results = []

    resume_folder = Path("resumes")

    # Iterate through every resume in the folder
    for resume_file in resume_folder.iterdir():

        if resume_file.suffix.lower() not in [".pdf", ".docx"]:
            continue

        print(f"\nProcessing: {resume_file.name}")

        try:
            # Read resume file
            resume_text = read_resume(resume_file)

            # Parse resume into structured object
            resume = parse_resume(resume_text)

            # (Optional) avoid rate limits
            time.sleep(5)

            # Compare resume against JD
            result = final_score(job, resume)

            # (Optional) avoid rate limits
            time.sleep(5)

            results.append(result)

            print(
                f"Completed: {result.details['candidate_name']} "
                f"({result.score}%)"
            )

        except Exception as e:
            print(f"Error processing {resume_file.name}: {e}")

    # -----------------------------
    # Sort Results
    # -----------------------------
    results.sort(
        key=lambda x: x.score,
        reverse=True
    )

    print("\n" + "=" * 60)
    print("TOP CANDIDATES")
    print("=" * 60)

    for result in results[:2]:
        print(result.model_dump())

    print("\n" + "=" * 60)
    print("LOWEST CANDIDATES")
    print("=" * 60)

    for result in results[-2:]:
        print(result.model_dump())


if __name__ == "__main__":
    main()