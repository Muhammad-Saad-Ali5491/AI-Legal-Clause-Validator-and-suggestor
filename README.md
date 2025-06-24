# AI Legal Clause Validator & Suggestion Tool

A powerful Streamlit-based web application that leverages advanced NLP models (LegalBERT and Gemini) to analyze legal contracts, classify clauses, suggest improvements, and generate detailed reports. This tool is designed for legal professionals, contract analysts, and businesses to streamline contract review processes with AI-driven insights.

---

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Environment Setup](#environment-setup)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

---

## Project Overview
The AI Legal Clause Validator & Suggestion Tool is an intelligent application that processes legal documents (PDF or DOCX) to:
- Extract and segment clauses.
- Classify clauses using LegalBERT for accuracy.
- Provide professional rewrite suggestions using Gemini.
- Generate downloadable DOCX reports with analysis results.

This tool is ideal for automating contract reviews, ensuring compliance, and improving clause clarity.

---

## Features
- **Document Upload**: Supports PDF and DOCX legal contracts.
- **Clause Segmentation**: Automatically splits documents into individual clauses using SpaCy.
- **Clause Classification**: Uses LegalBERT to classify clauses with confidence scores.
- **Rewrite Suggestions**: Generates improved clause versions via Gemini's generative capabilities.
- **Document Type Detection**: Predicts the type of legal document based on clause patterns.
- **Report Generation**: Exports analysis results as a polished DOCX report.
- **User-Friendly Interface**: Built with Streamlit for an intuitive, web-based experience.
- **Progress Tracking**: Displays real-time progress for clause analysis.

---

## Technology Stack
- **Frontend**: Streamlit (web interface)
- **Backend**: Python
- **NLP Models**:
  - **LegalBERT**: For clause classification (Hugging Face Transformers)
  - **Gemini**: For clause rewrite suggestions (Google Generative AI)
  - **SpaCy**: For text processing and clause segmentation
- **Document Processing**:
  - **PyMuPDF**: For PDF text extraction
  - **python-docx**: For DOCX handling and report generation
- **Environment Management**: python-dotenv
- **Dependencies**: Managed via `requirements.txt`

---

## Project Structure
```
AI Legal Clause Validator and Suggestor
├── app/
│   ├── __init__.py        # Initializes the app package, loads models (SpaCy, LegalBERT, Gemini)
│   ├── utils.py           # Core functions for text extraction, clause processing, and report generation
│   ├── routes.py          # Streamlit frontend logic for rendering the web interface
├── run.py                 # Entry point to launch the Streamlit app
├── .env                   # Environment variables (e.g., Gemini API key)
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

---

## Installation
Follow these steps to set up the project locally:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/ai-legal-validator.git
   cd ai-legal-validator
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**:
   - Create a `.env` file in the project root.
   - Add your Gemini API key:
     ```plaintext
     API_KEY=your_gemini_api_key
     ```
   - Obtain a Gemini API key from [Google Cloud Console](https://cloud.google.com/).

5. **Download SpaCy Model**:
   ```bash
   python -m spacy download en_core_web_sm
   ```

---

## Usage
1. **Run the Application**:
   ```bash
   python run.py
   ```
   This launches the Streamlit app at `http://localhost:8501`.

2. **Upload a Document**:
   - Navigate to the web interface.
   - Upload a PDF or DOCX legal contract.

3. **Review Results**:
   - View segmented clauses, classifications, and rewrite suggestions.
   - Download the DOCX report for a detailed analysis.

---

## How It Works
1. **Text Extraction** (`utils.py`):
   - Uses PyMuPDF for PDFs and python-docx for DOCX files to extract raw text.

2. **Legal Document Validation** (`utils.py`):
   - Checks for legal keywords to confirm the document is a contract.

3. **Clause Segmentation** (`utils.py`):
   - Employs SpaCy to split text into sentences, filtering for clauses longer than 20 characters.

4. **Clause Classification** (`utils.py`):
   - LegalBERT processes each clause to assign a label (e.g., "Obligation", "Termination") with a confidence score.

5. **Rewrite Suggestions** (`utils.py`):
   - Gemini generates professional rewrites based on the clause's category and content.

6. **Document Type Detection** (`utils.py`):
   - Analyzes clause labels to predict the document type (e.g., "NDA", "Service Agreement").

7. **Report Generation** (`utils.py`):
   - Creates a DOCX report summarizing clauses, labels, confidence scores, and suggestions.

8. **Frontend Rendering** (`routes.py`):
   - Streamlit displays the interface, progress bars, and results in an interactive format.

---

## Environment Setup
The `.env` file stores sensitive configurations:
```plaintext
API_KEY=your_gemini_api_key
```
Ensure this file is excluded from version control (e.g., add to `.gitignore`).

---

## Dependencies
Key dependencies (see `requirements.txt` for the full list):
- `streamlit`: Web interface
- `spacy`: NLP processing
- `transformers`: LegalBERT model
- `google-generativeai`: Gemini API
- `PyMuPDF`: PDF extraction
- `python-docx`: DOCX handling
- `torch`: PyTorch for LegalBERT
- `python-dotenv`: Environment variable management

Install all dependencies with:
```bash
pip install -r requirements.txt
```

---

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/your-feature`).
3. Commit changes (`git commit -m "Add your feature"`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a Pull Request.

Please ensure code follows PEP 8 guidelines and includes tests where applicable.

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments
- **Hugging Face**: For providing the LegalBERT model.
- **Google**: For the Gemini generative AI API.
- **Streamlit**: For the intuitive web framework.
- **SpaCy**: For robust NLP capabilities.
