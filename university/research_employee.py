from .project import Project
from .university import University

class ResearchEmployee:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email
        self.projects: List[Project] = []
        self.university: University = None

    def assign_to_project(self, project: Project, hours: int):
        if project.add_participant(self, hours):
            self.projects.append(project)
            self.university.update_statistics()
            self.university.send_notification(self)

    def get_info(self) -> str:
        return f"Сотрудник: {self.name}, Email: {self.email}"
