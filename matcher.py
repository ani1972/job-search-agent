def match_jobs(resume_text, jobs):
    keywords = ["python", "data", "machine learning", "AI"]
    matches = []
    for job in jobs:
        score = sum(1 for kw in keywords if kw.lower() in resume_text.lower())
        if score > 0:  # at least some overlap
            matches.append(job)
    return matches
