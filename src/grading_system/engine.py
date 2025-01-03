import requests
from requests import Response
from abc import abstractmethod, ABC


class BaseEngine(ABC):
    @abstractmethod
    def run(self, prompt: str, **kwargs) -> str:
        raise NotImplementedError


class EngineError(BaseException):
    def __init__(self, message: str):
        self.message = message


class OllamaEngine(BaseEngine):
    def __init__(self, model_name: str, host: str = "localhost", port: int = 11434) -> None:
        self.__model_name = model_name
        self.__host = host
        self.__port = port

    def __get_url(self) -> str:
        return f"http://{self.__host}:{self.__port}/api/chat"

    def __get_params(self, system_prompt: str, user_prompt: str) -> dict:
        return {
            "model": self.__model_name,
            "messages": [
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": user_prompt
                }
            ],
            "stream": False,
        }

    def run(self, prompt: str, system_prompt: str = "") -> str:
        url = self.__get_url()
        params = self.__get_params(system_prompt, prompt)
        response: Response = requests.post(url=url, json=params)
        if response.status_code != 200:
            error_message = f"status code: {response.status_code}, response text: {response.text}"
            raise EngineError(message=error_message)
        response_data = response.json()
        answer = response_data["response"]
        return answer
