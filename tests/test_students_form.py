from pages.student_form_page import StudentFormPage


def test_fill_student_form(driver):
    form_page = StudentFormPage(driver)

    print("Step 1: Read title")
    title_text = form_page.get_title_text()
    print(title_text)
    assert "Automation Practice Form" in title_text

    print("Step 2: Click accordion")
    form_page.click_element_block()

    print("Step 3: Enter name")
    form_page.enter_name("Somesh")

    print("Step 4: Enter email")
    form_page.enter_email("somesh@gmail.com")

    print("Step 5: Select gender")
    form_page.select_gender()

    print("Step 6: Enter mobile")
    form_page.enter_mobile("1234567890")

    print("Step 7: Enter DOB")
    form_page.date_of_birth("26-02-1994")

    print("Step 8: Enter subjects")
    form_page.enter_subjects("English, Maths, Science")

    print("Step 9: Upload file")
    form_page.upload_file(r"C:\Users\kalya\OneDrive\Documents\Feature User Login.txt")

    print("Step 10: Select state")
    form_page.select_state("NCR")

    print("Step 11: Select city")
    form_page.select_city("Agra")

    print("Step 12: Submit")
    form_page.click_submit()