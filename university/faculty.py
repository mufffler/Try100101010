class Faculty:
    def __init__(self, name: str):
        self.name = name
        self.departments: List[str] = []
        self.dean: str = None

    def add_department(self, department: str):
        self.departments.append(department)

    def set_dean(self, dean: str):
        self.dean = dean
