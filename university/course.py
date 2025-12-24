class Course:
    def __init__(self, course_id: str, name: str, hours: int):
        self.course_id = course_id
        self.name = name
        self.hours = hours

    def register_course(self, university):
        # Логика регистрации курса
        return True
