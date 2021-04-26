def calculate_gpa(student_id):
    marks = []
    credits = []
    for mark in markList:
        if mark.get_student().get_id() == student_id:
            marks.append(float(mark.get_mark()))
            credits.append(float(mark.get_course().get_credits()))
    return np.average(np.array(marks), weights=np.array(credits))

