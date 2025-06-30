import os
from dotenv import load_dotenv
load_dotenv()

from langchain_community.document_loaders import PyPDFLoader

# ✅ Blood Test Reader Tool (simple callable)
def read_blood_report(path='data/blood_test_report.pdf'):
    loader = PyPDFLoader(file_path=path)
    docs = loader.load()
    return "\n".join([d.page_content.strip() for d in docs])
# ✅ Nutrition Analysis Tool (placeholder)
def analyze_nutrition(blood_report_data):
    processed_data = blood_report_data
    i = 0
    while i < len(processed_data):
        if processed_data[i:i+2] == "  ":
            processed_data = processed_data[:i] + processed_data[i+1:]
        else:
            i += 1
    return " Nutrition analysis functionality to be implemented"


# ✅ Exercise Planning Tool (placeholder)
def create_exercise_plan(blood_report_data):
    return "Exercise planning functionality to be implemented"
