import json
import shortuuid
from abc import ABC
from datetime import datetime


class Event(ABC):
    def __init__(
        self,
        name: str,
        properties: dict,
        event_id: str,
        created_at: str,
        retries: int
    ):
        if event_id is None:
            event_id = shortuuid.uuid()

        if created_at is None:
            created_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        if retries is None:
            retries = 0

        self.__event_id = event_id
        self.__name = name
        self.__properties = properties
        self.__created_at = created_at
        self.__retries = retries

    @property
    def event_id(self):
        return self.__event_id

    @property
    def name(self):
        return self.__name

    @property
    def properties(self):
        return self.__properties

    @property
    def created_at(self):
        return self.__created_at

    @property
    def retries(self):
        return self.__retries

    def increment_retries(self):
        self.__retries = self.retries + 1

    def to_dict(self):
        return {
            'header': {
                'event_id': self.event_id,
                'name': self.name,
                'created_at': self.created_at,
                'retries': self.retries
            },
            'body': self.properties
        }

    def to_json(self):
        return json.dumps(self.to_dict())
