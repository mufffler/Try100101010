class Employee:
    def __init__(self, social_security_number: str, name: str, email: str):
        self.social_security_number = social_security_number
        self.name = name
        self.email = email

    def get_info(self) -> str:
        return f"ID: {self.social_security_number}, Name: {self.name}, Email: {self.email}"
