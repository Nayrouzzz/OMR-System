# OMR (Optical Mark Recognition) System

An OMR system designed to automatically grade multiple-choice exams by processing scanned answer sheets. 
---

## **Features**
- Converts PDF exam sheets into images for processing.
- Extracts Regions of Interest (ROIs) from answer sheets -as a user input-.
- Detects and grades marked answers using image processing techniques.
- Annotates the results on the PDF (correct answers in green, incorrect in red).
- Handles anomalies like multiple answers.
- Supports both horizontal and vertical question layouts.

---

## **How It Works**
1. **Input**: PDF exam sheets and a JSON file containing ROI coordinates and grading rules.
2. **Processing**:
   - Converts PDF pages to images.
   - The user starts to manually select regiion of interest.
   - Extract ROIs for model and student answers and generate user_response.json.
   - Detects marked answers using Hough Circle Transform and pixel analysis.
   - Compares student answers with the model answer.
3. **Output**: An annotated PDF with results and a JSON file containing scores and anomalies.

---
