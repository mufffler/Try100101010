from .research_employee import ResearchEmployee

class Lecturer(ResearchEmployee):
    def __init__(self, social_security_number: str, name: str, email: str, research_area: str):
        super().__init__(social_security_number, name, email, research_area)
