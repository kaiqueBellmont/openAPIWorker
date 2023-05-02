"""
Params File
"""
import os
from dataclasses import dataclass

from dotenv import load_dotenv


@dataclass
class Params:
    """
    Params classe to make easier request
    """
    load_dotenv()  # take environment variables from .env.

    KEY: str = os.getenv("OPENAI_API_KEY")
    ENDPOINT: str = os.getenv("ENDPOINT")

    headers = {
        "Authorization": f"Bearer {KEY}",
        "Content-Type": "application/json"
    }

    @staticmethod
    def payload_maker(code_list):
        """
        :param code_list:
        :return:
        """
        payload = {
            "model": "text-davinci-003",
            "prompt": "What could be improved in these codes?\n\n" + str(code_list),
            "max_tokens": 1000,
        }
        return payload
