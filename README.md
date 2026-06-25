# Code-Breakers

An AI-powered HR assistant platform that streamlines recruitment, onboarding, and policy support through specialized AI agents.

## Live Demo

**Website:** https://codebreakers.streamlit.app/

##  Features

###  Policy Agent

* Answers employee policy-related queries.
* Retrieves relevant information from company policy documents.
* Provides quick and consistent policy guidance.

###  Resume Screening Agent

* Evaluates resumes against predefined hiring criteria.
* Scores candidates based on:

  * Skills (40%)
  * Projects (30%)
  * Education (20%)
  * Certifications (10%)
* Supports both individual and bulk resume screening.
* Generates candidate rankings and screening reports.

###  Onboarding Agent

* Assists new employees through the onboarding process.
* Generates personalized onboarding plans.
* Provides role-specific onboarding information.

###  Central Orchestrator

* Routes user requests to the appropriate agent.
* Coordinates interactions between agents.
* Maintains a seamless end-to-end workflow.

##  Workflow

### Applicant Workflow

1. Select desired role.
2. Verify vacancy availability.
3. Upload resume (PDF/DOCX).
4. Resume is analyzed and scored.
5. Candidate receives screening results and feedback.

### HR Manager Workflow

1. Select hiring role.
2. Upload multiple resumes.
3. Automated resume screening and ranking.
4. Generate candidate reports and top candidate recommendations.

### Policy Workflow

1. User submits a policy-related query.
2. Policy Agent retrieves relevant information.
3. Response is returned to the user.

##  Flowchart

CodeBreakers Workflow:
![Code-Breakers Workflow](assets/workflow.png)


##  Tech Stack

| Component      | Technology                |
| -------------- | ------------------------- |
| Language       | Python                    |
| Frontend       | Streamlit                 |
| AI Integration | OpenAI API                |
| Data Storage   | CSV Files                 |
| Deployment     | Streamlit Community Cloud |

##  Project Structure

```text
Code-Breakers/
├── agents/
├── data/
├── main.py
├── requirements.txt
└── README.md
```

##  Deployment

The application is deployed using Streamlit Community Cloud. All agents are integrated through a central orchestration layer implemented in `main.py`, enabling dynamic routing and workflow management.

##  Contributors

* Shradha Kedia
* Avani Mandlik
* Sanjita Kumar

##  License

This project was developed as part of Build2Break 2025.
