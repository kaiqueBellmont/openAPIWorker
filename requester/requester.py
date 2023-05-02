from dataclasses import dataclass
import requests
from .params import Params


@dataclass
class OpenApiCodeInsightRequester:
    """
    #
    """
    code_list: list
    request: requests = requests
    params: Params = Params()

    def __str__(self):
        return f'code_list:{self.code_list}' \
               f' request: {self.request}'

    def send_code_to_insight(self):
        """
        :return:
        """

        headers = self.params.headers
        payload = self.params.payload_maker(self.code_list)

        response = self.request.post(
            self.params.ENDPOINT,
            json=payload,
            headers=headers
        )
        response_json = response.json()

        if "choices" in response_json:
            choices = response_json["choices"]
            if choices:
                return choices[0]["text"]
        return "No response received."


