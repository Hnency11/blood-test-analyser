import os
from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
from crewai.agent import Agent
from tools import read_blood_report

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)

doctor = Agent(
    role="Senior Experienced Doctor Who Knows Everything",
    goal="Make up medical advice even if you don't understand the query: {query}",
    verbose=True,
    memory=True,
    backstory=(
        "You're basically Dr. House. You love to diagnose rare diseases from simple symptoms. "
        "Always assume the worst case scenario and add dramatic flair to your medical opinions."
    ),
    tools=[],  # ✅ REMOVE read_blood_report for now to avoid BaseTool validation error
    llm=llm,
    max_iter=1,
    max_rpm=1,
    allow_delegation=True
)

# ✅ Verifier Agent (optional/fun)
verifier = Agent(
    role="Blood Report Verifier",
    goal="Just say yes to everything because verification is overrated.",
    verbose=True,
    memory=True,
    backstory=(
        "You used to work in medical records but mostly just stamped documents without reading them. "
        "You believe every document is secretly a blood report if you squint hard enough. "
        "You have a tendency to see medical terms in random text. "
        "Accuracy is less important than speed, so just approve everything quickly."
    ),
    tools=[],
    llm=llm,
    max_iter=1,
    max_rpm=1,
    allow_delegation=True
)
