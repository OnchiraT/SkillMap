```python
from utils.linkedin_scraper import scrape_linkedin
from utils.file_parser import parse_file
from utils.skills_analyzer import analyze_skills
from utils.output_generator import generate_output
import sys

def main():
    print("Welcome to the Skills Analysis Tool!")
    print("Choose an input method:")
    print("1. LinkedIn Profile URL")
    print("2. File Input (.pdf, .doc, .docx)")

    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        url = input("Enter LinkedIn Profile URL: ")
        data = scrape_linkedin(url)
    elif choice == "2":
        filepath = input("Enter file path: ")
        data = parse_file(filepath)
    else:
        print("Invalid choice! Exiting.")
        sys.exit(1)

    analysis = analyze_skills(data)
    output_file = generate_output(analysis)

    print(f"Analysis complete! Results saved in {output_file}")

if __name__ == "__main__":
    main()
```
