from typing import List

class University:
    def __init__(self, name: str):
        self.name = name
        self.employees: List[ResearchEmployee] = []
        self.projects: List[Project] = []

    def add_employee(self, employee):
        self.employees.append(employee)
        employee.university = self

    def update_statistics(self):
        # Логика обновления статистики
        pass

    def send_notification(self, employee):
        print(f"Уведомление отправлено: {employee.name}")
