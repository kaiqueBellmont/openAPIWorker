from dataclasses import dataclass


@dataclass
class Responser:
    """
    A simple Parser Response Class.
    """
    response: str

    def to_json(self):
        """
        :return:
        """
        return {self.response}
