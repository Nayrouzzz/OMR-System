# OMR (Optical Mark Recognition) System

An OMR system designed to automatically grade multiple-choice exams by processing scanned answer sheets. 
---

## **Features**
- Converts PDF exam sheets into images for processing.
- Extracts Regions of Interest (ROIs) from answer sheets.
- Detects and grades marked answers using image processing techniques.
- Annotates the results on the PDF (correct answers in green, incorrect in red).
- Handles anomalies like multiple answers or no answers marked.
- Supports both horizontal and vertical question layouts.

---

## **How It Works**
1. **Input**: PDF exam sheets and a JSON file containing ROI coordinates and grading rules.
2. **Processing**:
   - Converts PDF pages to images.
   - Extracts ROIs for model and student answers.
   - Detects marked answers using Hough Circle Transform and pixel analysis.
   - Compares student answers with the model answer.
3. **Output**: An annotated PDF with results and a JSON file containing scores and anomalies.

---

## **Installation**
1. Clone the repository:
   ```bash
   git clone https://github.com/Nayrouzzz/OMR-System.git
