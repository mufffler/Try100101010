from .employee import Employee

class AdministrativeEmployee(Employee):
    def __init__(self, social_security_number: str, name: str, email: str):
        super().__init__(social_security_number, name, email)
