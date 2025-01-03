from abc import abstractmethod, ABC


class BasePrompter(ABC):
    @abstractmethod
    def prepare_system_prompt(self, **kwargs) -> str:
        raise NotImplementedError

    @abstractmethod
    def prepare_user_prompt(self, **kwargs) -> str:
        raise NotImplementedError


class MockPrompter(BasePrompter):
    def prepare_system_prompt(self, gh_repo_url: str) -> str:
        return (
            "Ты помощник преподавателя для проверки домашних заданий студентов по программированию. "
            "Оцени качество кода на Python согласно Заданию и Критериям оценки. "
            "В конце посчитай количество соблюденных критериев. \n"
            "Задание: реализовать функцию для сложения двух чисел \n"
            "Критерии оценки: \n"
            "1. Корректно указаны типы аргументов и возвращаемого функции \n"
            "2. Функция реализована корректно \n"
            "3. Для реализации функции используются только стандартные библиотеки Python \n"
        )

    def prepare_user_prompt(self, pr_description: str, file_path: str, code_lines: list[str]) -> str:
        user_prompt = (
            f"Описание работы, написанное студентом: {pr_description}"
            f"Название файла: {file_path}\n"
            "Код ниже:\n"
            "```\n"
            "\n".join(code_lines) + "\n"
            "```\n"
            # "\n".join(f"[{number+1}] " + line for number, line in enumerate(code_lines))
        )
        return user_prompt
