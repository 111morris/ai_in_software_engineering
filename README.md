# AI in Software Engineering — Week 4 Assignment

## Overview
This project demonstrates the practical application of artificial intelligence (AI) to software engineering problems, including code completion, automated testing, predictive analytics, and ethical assessment. Each component is clearly separated, well-commented, and designed to be reproducible for evaluation and peer learning.

***

## Table of Contents
- [Overview](#overview)
- [Directory Structure](#directory-structure)
- [Features](#features)
- [Setup & Installation](#setup--installation)
- [Usage Instructions](#usage-instructions)
- [Assignment Tasks](#assignment-tasks)
- [Results & Screenshots](#results--screenshots)
- [Ethical Reflection](#ethical-reflection)
- [Innovation Challenge](#innovation-challenge)
- [Contributing](#contributing)
- [License](#license)

***

## Directory Structure
```
├── code_completion/           # Copilot/manual code comparison
│   └── sort_dicts.py         # Sorting function (AI & manual versions)
├── automated_testing/        # Selenium or Testim.io test scripts
│   └── login_test.py         # Automated login test
├── predictive_analytics/     # notebooks
│   └── breast_cancer.ipynb
├── innovation_challenge/     # Proposal doc for new AI tool
│   └── testsense-proposal.md
├── README.md                 # (this file)
└── ...
```

***

## Features
- **AI-Powered Code Suggestions:** Compare human and AI-written code for a common sorting task.
- **AI-Driven Automated Testing:** Login page automation using Selenium (or Testim.io).
- **Predictive Analytics:** Random Forest model predicts resource allocation needs using real data.
- **Ethics Analysis:** Practical reflection on bias and fairness in AI-powered software systems.
- **Innovation Challenge:** Thoughtful proposal for an original AI tool in software engineering recognized gaps.

***

## Setup & Installation
1. **Clone this repository:**
   ```bash
   git clone https://github.com/111morris/ai_in_software_engineering.git
   cd ai_in_software_engineering
   ```
2. **Install core dependencies:**
   - Python 3.8+
   - Install required Python packages:
     ```bash
     pip install -r requirements.txt
     ```
     _Typical requirements: `selenium`, `scikit-learn`, `pandas`, `jupyter`, `matplotlib`, `webdriver-manager`._
   - For Selenium: Download ChromeDriver/FirefoxDriver as needed and ensure paths are set (Google Colab setup instructions included in notebook if needed).

3. **Place datasets:**
   - Download the [Kaggle Breast Cancer Dataset](https://www.kaggle.com/competitions/iuss-23-24-automatic-diagnosis-breast-cancer/data) and save to `predictive_analytics/data/`.

***

## Usage Instructions
- Open any notebook or script and follow inline comments for step-by-step instructions.
- To rerun automated tests, start the Python script in `automated_testing/` after configuring driver dependencies.
- Predictive analytics is performed in Jupyter (`breast_cancer.ipynb`):
    - Load data, run all cells, inspect and export results/snapshots.
- Innovation Challenge proposal is in simple Markdown for clarity.

***

## Assignment Tasks
1. **Code Completion (Copilot/Manual):**
   - Found in `code_completion/sort_dicts.py`.
   - Demonstrates both AI-suggested and manual approaches, with efficiency analysis and sample inputs/outputs.
2. **Automated Testing:**
   - `automated_testing/login_test.py` covers both valid and invalid scenarios for demo credentials.
   - Screenshots are generated for each outcome.
3. **Predictive Analytics:**
   - `predictive_analytics/breast_cancer.ipynb` trains a Random Forest on the breast cancer dataset, reporting accuracy and F1.
   - Classification report and resource allocation insights included.
4. **Ethical Analysis:**
   - Critical discussion of dataset/model bias and mitigation steps; included in both the PDF and notebook.
5. **Innovation Challenge:**
   - Original tool idea and 1-page proposal found in `innovation_challenge/`.

***



## Ethical Reflection
This project acknowledges real-world risks of AI-driven automation, including bias, fairness, data privacy, and over-reliance on automated code. See the main report/`resource_allocation.ipynb` for critical reflection and steps taken to audit and mitigate these risks.

***

## Innovation Challenge
**[TestSense: AI-Powered Test Gap Explorer]**
- See `innovation_challenge/testsense-proposal.md` for a full 1-page description of the tool’s purpose, workflow, and expected impact.

***

## Contributing
This project was completed by Morris Mulandi for coursework, but suggestions for improvements are welcome via Issues or Pull Requests. If reusing for your own learning or teaching, please credit the contributor : ).

***

## License
MIT License. This project and all code are for educational demonstration purposes only. See `LICENSE` for details.

***

## Acknowledgments
Special thanks to the course instructors, the open source community and tool contributors for Selenium, Scikit-learn, and related AI frameworks.
