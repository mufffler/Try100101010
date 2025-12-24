from university.research_employee import ResearchEmployee
from university.project import Project
from university.university import University


def main():
    # Создаем университет
    uni = University("ВГУ")

    # Создаем научного сотрудника
    researcher = ResearchEmployee("Иванов И.И.", "ivanov@uni.edu")
    uni.add_employee(researcher)

    # Создаем проект
    project = Project("Проект ИИ", "2025-01-01", "2025-12-31")

    # Присоединяемся к проекту
    researcher.assign_to_project(project, 20)

    print("Система успешно запущена!")
    print(researcher.get_info())


if __name__ == "__main__":
    main()
