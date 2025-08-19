from resume_parser import parse_resume
from job_scraper import scrape_jobs
from matcher import match_jobs
from cover_letter import generate_cover_letter

RESUME_PATH = "resume.pdf"


def main():
    # 1. Parse resume
    resume_text = parse_resume(RESUME_PATH)

    # 2. Scrape jobs (mock/simple version)
    jobs = scrape_jobs()

    # 3. Match jobs
    matches = match_jobs(resume_text, jobs)

    # 4. Generate cover letters
    with open("job_results.txt", "w", encoding="utf-8") as f:
        for job in matches:
            cover = generate_cover_letter(resume_text, job)
            f.write(f"Job: {job['title']} at {job['company']}\n")
            f.write(f"Link: {job['link']}\n")
            f.write("Cover Letter:\n")
            f.write(cover)
            f.write("\n" + "="*50 + "\n\n")

    print("Job results saved to job_results.txt")


if __name__ == "__main__":
    main()
