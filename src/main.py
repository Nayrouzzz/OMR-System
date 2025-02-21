import utils_demo #The mock utils file
import os



def extract_data(response):
    data = {
        "row_col_numbers": utils.extract_needed_data(response, "row_col_numbers"),
        "marked": utils.extract_needed_data(response, "marked"),
        "graded_by_teacher": utils.extract_needed_data(response, "graded_by_teacher"),
        "fractioned_grades": utils.extract_needed_data(response, "fractioned_grades"),
        "direction": utils.extract_needed_data(response, "direction_of_question"),
        "coordinations": utils.extract_needed_data(response, "roi_coordinates")
    }
    return data

def process_model_answers(model_answer, response, num_pages_per_test, data):
    model_all_rois = utils.extract_rois(model_answer, data['coordinations'], response, num_pages_per_test)
    model_all_pxl_vals = utils.get_rois_pxl_val(model_all_rois, data['row_col_numbers'])
    correct_answer = utils.get_correct_answers(model_all_pxl_vals, data)
    return correct_answer

def process_student_answers(student_answer, response, num_pages_per_test, data, correct_answer):
    students_all_rois = utils.extract_rois(student_answer, data['coordinations'], response, num_pages_per_test)
    students_all_pxl_vals = utils.get_rois_pxl_val(students_all_rois, data['row_col_numbers'])
    final_score, anomalies = utils.build_final_score(students_all_pxl_vals, data, correct_answer)
    
    return final_score, anomalies



def main(pdf_path,response_path,num_pages_per_test,PDF_OUTPUT_PATH):
    
    response = utils.load_response(response_path)
    allPages = utils.convert_pdf_to_images(pdf_path)
    model_answer, student_answer = utils.seprate_model_student(allPages, num_pages_per_test)    
    # response = utils.build_response(model_answer)    
    data = extract_data(response)



    correct_answer = process_model_answers(model_answer, response, num_pages_per_test, data)
    score_with_coords, anomalies = process_student_answers(student_answer, response, num_pages_per_test, data, correct_answer)
    final_score_with_exam_pg_num = utils.finalScore_with_pgNum(score_with_coords,response)
    
    exam_grade = utils.calculate_max_score(response)
    finalized_anomalies  = utils.annotate_and_save_pdf(student_answer, final_score_with_exam_pg_num, num_pages_per_test, anomalies, exam_grade, PDF_OUTPUT_PATH, response)
    clear_filan_score = utils.clear_final_score(final_score_with_exam_pg_num)
    result = {"final_score": clear_filan_score , "Problems":finalized_anomalies}
    print(result)
    return result

if __name__ == "__main__":

    no= int(input("Please enter the exam number: "))
    num_pages_per_test = int(input("Please enter count of pages in your exam: "))
    USER_RESPONSE_PATH= f"data/input/exam{no}/user_response.json"
    PDF_PATH= f"data/input/exam{no}/ex{no}.pdf"
    # IMAGES_DIR = f"data/output/exam{no}/images"
    # IMG_PATH=f"data/output/exam{no}/images/1.png"
    PDF_OUTPUT_PATH=f"data/output/exam{no}/ex{no}_result.pdf"
    # os.makedirs(IMAGES_DIR, exist_ok=True)
    
    main(PDF_PATH, USER_RESPONSE_PATH, num_pages_per_test, PDF_OUTPUT_PATH)

