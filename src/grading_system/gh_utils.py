from github import Github


class GHUtils:
    def __init__(self, github_token: str, full_repo_name: str, pull_number: int):
        self.g = Github(login_or_token=github_token)
        self.repo = self.g.get_repo(full_repo_name)
        self.pull_request = self.repo.get_pull(pull_number)
        self.comments = []

    def get_pr_description(self) -> str:
        return self.pull_request.body

    def create_comment(self, comment_text: str) -> None:
        self.pull_request.create_issue_comment(comment_text)


# from github import PullRequest
# last_commit = pr.get_commits()[pr.commits - 1]
# comments = []
# for file in pr.get_files():
#     with open(file.filename, "r", encoding="utf-8") as f:
#         content = f.read()
#     comment_text = f"Code\n```\n{content}\n```"
#     new_comment = PullRequest.ReviewComment(path=file.filename, position=1, body=comment_text)
#     comments.append(new_comment)
# pr.create_review(last_commit, "New answer" + pr.body, "REQUEST_CHANGES", comments)
