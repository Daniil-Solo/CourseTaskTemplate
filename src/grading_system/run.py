import os
import click
from src.grading_system.engine import BaseEngine, OllamaEngine
from src.grading_system.prompter import BasePrompter, MockPrompter
from src.grading_system.file_utils import get_files, USE_ONLY_PY_FILES, EXCLUDE_INIT_FILES, get_code_lines
from src.grading_system.gh_utils import GHUtils


class GradingSystem:
    def __init__(self, engine: BaseEngine, prompter: BasePrompter):
        self.engine = engine
        self.prompter = prompter
        self.parent_repo_url = os.environ["PARENT_REPO_URL"]
        self.gh_utils = GHUtils(
            os.environ["GITHUB_TOKEN"], os.environ["FULL_REPO_NAME"], int(os.environ["PULL_NUMBER"])
        )

    def run(self) -> None:
        pr_description = self.gh_utils.get_pr_description()
        system_prompt = self.prompter.prepare_system_prompt(gh_repo_url=self.parent_repo_url)

        file_paths = get_files("src/code", [USE_ONLY_PY_FILES, EXCLUDE_INIT_FILES])
        for file_path in file_paths:
            code_lines = get_code_lines(file_path)
            user_prompt = self.prompter.prepare_user_prompt(
                pr_description=pr_description, file_path=file_path, code_lines=code_lines
            )
            answer = self.engine.run(user_prompt, system_prompt=system_prompt)
            self.gh_utils.create_comment(answer)


@click.command()
@click.argument("model_name", type=click.STRING)
@click.option("-h", "--host", type=click.STRING, default="localhost")
@click.option("-p", "--port", type=click.INT, default=11434)
def run_grading_system(model_name, host, port):
    prompter = MockPrompter()
    engine = OllamaEngine(model_name, host, port)
    grading_system = GradingSystem(engine, prompter)
    grading_system.run()


if __name__ == "__main__":
    run_grading_system()
