from typing import List

class Project:
    def __init__(self, name: str, start_date: str, end_date: str):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.participants: List[tuple] = []  # (researcher, hours)

    def add_participant(self, researcher, hours: int) -> bool:
        # Добавляем участника в проект
        self.participants.append((researcher, hours))
        return True

    def confirm_enrollment(self) -> bool:
        return True
