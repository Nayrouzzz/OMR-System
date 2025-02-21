# OMR (Optical Mark Recognition) System

An OMR system designed to automatically grade multiple-choice exams by processing scanned answer sheets. This project demonstrates the use of image processing techniques to detect and evaluate marked answers on exam sheets.

---

## **Code Availability**
Due to copyright restrictions, some parts of the code (e.g., `utils.py`) are not included in this repository. However, I can provide a high-level explanation of the system's functionality and demonstrate its usage through sample inputs and outputs.

---

## **High-Level Overview of the System**
The OMR system consists of the following components:
1. **PDF to Image Conversion**: Converts scanned PDF exam sheets into images for processing.
2. **ROI Extraction**: Extracts Regions of Interest (ROIs) from the answer sheets based on predefined coordinates selected by the user.
3. **Answer Detection**: Uses image processing techniques (e.g., Hough Circle Transform) to detect marked answers.
4. **Grading**: Compares student answers with the model answer and calculates scores.
5. **Annotated Output**: Generates an annotated PDF with correct (green) and incorrect (red) answers highlighted.

---

## **Features**
- **Anomaly Handling**: Detects and handles anomalies like multiple answers or no answers marked.
- **Flexible Layouts**: Supports both horizontal and vertical question layouts.
- **User-Friendly**: Allows manual selection of Regions of Interest (ROIs) for customization.
- **Detailed Output**: Provides an annotated PDF and a JSON file with scores and detected anomalies.

---

## **How It Works**
1. **Input**:
   - PDF exam sheets.
   - A JSON file (`user_response.json`) containing ROI coordinates and grading rules (generated after manual ROI selection).
2. **Processing**:
   - Converts PDF pages to images.
   - Extracts ROIs for model and student answers based on user-defined coordinates.
   - Detects marked answers using Hough Circle Transform and pixel analysis.
   - Compares student answers with the model answer to calculate scores.
3. **Output**:
   - An annotated PDF with correct answers highlighted in green and incorrect answers in red.
   - A JSON file containing scores and detected anomalies.

---

## **Example Workflow**
1. **Input Files**:
   - Exam PDF: `data/input/exam1.pdf`
   - JSON Response: `data/input/exam1_user_response.json`
2. **Processing**:
   - Run the system to process the exam sheets.
3. **Output Files**:
   - Annotated PDF: `data/output/exam1_result.pdf`
   - Scores and Anomalies: Printed in the terminal and saved in the output folder.

