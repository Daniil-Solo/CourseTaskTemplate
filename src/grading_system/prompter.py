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
            "Ты помощник преподавателя для проверки домашних заданий студентов по программированию на Python. "
            "Оцени качество кода на Python согласно Заданию и Критериям оценки. "
            "## Задание\nНеобходимо реализовать функцию для сложения двух чисел \n"
            "## Критерии проверки: \n"
            "1. Корректно указаны типы аргументов и возвращаемого значения функции \n"
            "2. В функции складываются значения двух аргументов \n"
            "3. В функции есть проверка, что аргументы являются целыми числами \n"
            "4. Для реализации функции используются только стандартные библиотеки Python \n\n"
            "## Формат ответа: \n"
            "Напиши для каждого критерия: соблюден ли он, какая возможно есть проблема\n"
            "Сделай отступ и напиши наводящие вопросы по каждому несоблюденному критерию, избегая его раскрытие \n"
        )

    def prepare_user_prompt(self, pr_description: str, file_path: str, code_lines: list[str]) -> str:
        user_prompt = (
            f"Описание решения от студента: {pr_description}"
            f"Название файла: {file_path}\n"
            "Код ниже:\n"
            "```\n"
            "\n".join(code_lines) + "\n"
            "```\n"
        )
        return user_prompt
