from transformers import pipeline

# Load a free text-generation pipeline (Falcon or GPT-2 like model)
generator = pipeline("text-generation", model="gpt2")


def generate_cover_letter(resume_text, job):
    prompt = f"""
    professional cover letter for the job '{job['title']}' at {job['company']}'.
    The candidate has the following resume details: {resume_text}.
    """

    # Generate text (max 250 tokens for quick response)
    result = generator(prompt, max_length=250,
                       do_sample=True, temperature=0.7, top_p=0.9)

    return result[0]["generated_text"]
