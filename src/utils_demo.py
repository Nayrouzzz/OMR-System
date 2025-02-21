# This file contains mock functions - simplified implementations- to demonstrate the functionality without revealing the actual code, as it was part of a frelance task and i can't publish it.

# utils_mock.py (Fully mocked version)

import json
import numpy as np
from PIL import Image
import cv2

# Mock function: Load JSON response
def load_response(file_path):
    """Mock function to load a JSON response."""
    print(f"Mock: Loading response from {file_path}")
    return {"example": "data"}

# Mock function: Convert PDF to images
def convert_pdf_to_images(pdf_file_path, dpi=150):
    """Mock function to convert PDF to images."""
    print(f"Mock: Converting PDF {pdf_file_path} to images with DPI {dpi}")
    # Return a dummy image (e.g., a blank white image)
    dummy_image = np.ones((800, 600, 3), dtype=np.uint8) * 255  # White image
    return [dummy_image]

# Mock function: Separate model and student answers
def seprate_model_student(allPages, num_pages_per_test):
    """Mock function to separate model and student answers."""
    print("Mock: Separating model and student answers")
    model_answer = allPages[:num_pages_per_test]
    student_answer = allPages[num_pages_per_test:]
    return model_answer, student_answer

# Mock function: Select a single ROI
def select_single_roi(image):
    """Mock function to select a single ROI."""
    print("Mock: Selecting a single ROI")
    return (100, 100, 50, 50)  # Dummy ROI coordinates

# Mock function: Extract needed data from response
def extract_needed_data(response, key):
    """Mock function to extract needed data from response."""
    print(f"Mock: Extracting data for key '{key}'")
    return ["dummy_data"]

# Mock function: Build ROI response
def build_response(model_answer):
    """Mock function to build ROI response."""
    print("Mock: Building ROI response")
    return [{"page_number": 1, "rois": [{"roi_coordinates": [100, 100, 50, 50]}]}]

# Mock function: Extract ROIs
def extract_rois(students_answer, all_coordinations, roi_response, num_pages_per_test):
    """Mock function to extract ROIs."""
    print("Mock: Extracting ROIs from student answers")
    # Return a dummy ROI (e.g., a small portion of the image)
    dummy_roi = students_answer[0][100:200, 100:200]  # Extract a small region
    return [[dummy_roi]]

# Mock function: Split image into boxes
def splitBoxes(img, vertical_split, horizontal_split):
    """Mock function to split image into boxes."""
    print("Mock: Splitting image into boxes")
    # Return a dummy list of boxes
    return [img[0:10, 0:10]]  # Dummy box

# Mock function: Detect circles using Hough Circle Transform
def HoughCircle_All(imgGray, box):
    """Mock function to detect circles."""
    print("Mock: Detecting circles using Hough Circle Transform")
    # Return dummy circle coordinates
    return np.array([[[50, 50, 10]]], dtype=np.uint16)  # Dummy circle

# Mock function: Count pixels in a circle
def count_pxls(imgGray, circle):
    """Mock function to count pixels in a circle."""
    print("Mock: Counting pixels in a circle")
    return 100  # Dummy pixel count

# Mock function: Get pixel values for ROIs
def get_rois_pxl_val(all_rois, row_col_numbers_list):
    """Mock function to process pixel values for ROIs."""
    print("Mock: Processing pixel values for ROIs")
    # Return dummy pixel values
    return [np.zeros((row_col_numbers_list[0][0], row_col_numbers_list[0][1]))]

# Mock function: Check for anomalies
def check_anomalies(row, average, max_tolerance=0.05, min_tolerance=0.05):
    """Mock function to check for anomalies."""
    print("Mock: Checking for anomalies")
    return "Normal"  # Dummy anomaly status

# Mock function: Get correct answers
def get_correct_answers(allpxlvals, data):
    """Mock function to get correct answers."""
    print("Mock: Getting correct answers")
    return [[0]]  # Dummy correct answers

# Mock function: Build final score
def build_final_score(students_allPxlValues, data, correct_answer):
    """Mock function to calculate the final score."""
    print("Mock: Calculating final score")
    # Return a dummy score
    return [{"id": 1, "score": 95, "answers": []}], {"1": "No anomalies detected"}

# Mock function: Add page numbers to final score
def finalScore_with_pgNum(final_score_list, response):
    """Mock function to add page numbers to final score."""
    print("Mock: Adding page numbers to final score")
    return final_score_list  # Return the input as-is

# Mock function: Clear final score
def clear_final_score(final_score_list):
    """Mock function to clear final score."""
    print("Mock: Clearing final score")
    return final_score_list  # Return the input as-is

# Mock function: Calculate maximum score
def calculate_max_score(response):
    """Mock function to calculate maximum score."""
    print("Mock: Calculating maximum score")
    return 100  # Dummy maximum score

# Mock function: Draw text on image
def draw_text_cv2(image, text, position, font_size=1, font_color=(255, 0, 0), font=cv2.FONT_HERSHEY_SIMPLEX, thickness=3):
    """Mock function to draw text on image."""
    print(f"Mock: Drawing text '{text}' on image")
    return image  # Return the input image

# Mock function: Draw circle on image
def draw_circle_cv2(image, center, radius, color, thickness=1):
    """Mock function to draw circle on image."""
    print(f"Mock: Drawing circle at {center} with radius {radius}")
    return image  # Return the input image

# Mock function: Annotate and save PDF
def annotate_and_save_pdf(student_answer, final_score, num_pages_per_test, anomalies, exam_grade, PDF_OUTPUT_PATH, response):
    """Mock function to annotate and save PDF."""
    print(f"Mock: Saving annotated PDF to {PDF_OUTPUT_PATH}")
    # Save a dummy image as PDF
    dummy_image = np.ones((800, 600, 3), dtype=np.uint8) * 255  # White image
    Image.fromarray(dummy_image).save(PDF_OUTPUT_PATH, "PDF")
    return anomalies
