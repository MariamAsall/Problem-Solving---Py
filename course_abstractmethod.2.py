from abc import ABC, abstractmethod

class course(ABC):
    def __init__(self, course_code, course_name, credit_hours):
        self.course_code = course_code
        self.course_name = course_name
        self.credit_hours = credit_hours

    @abstractmethod 
    def calculate_course_fee(self):
        pass

class mathcourse(course):
    def calculate_course_fee(self):
        base_fee_per_credit_hour = 100
        return self.credit_hours * base_fee_per_credit_hour 

class sciencecourse(course):
    def calculate_course_fee(self):
        base_fee_per_credit_hour = 120
        return self.credit_hours * base_fee_per_credit_hour 
    
def total_course_fees(courses):
    total = 0
    for course in courses:
        total += course.calculate_course_fee()
    return total 
    
math_course1 = mathcourse("MATH101", "INTRO to math", 3)
science_course =sciencecourse("SCI201", "INTRO to science", 4)
total_fees = total_course_fees([math_course1, science_course])
print("Total course fees:", total_fees)

        
