from abc import ABC, abstractmethod
from typing import List
from purevpn_event_bus.src.event import Event


class EventHandler(ABC):
    def __init__(self, subscribed_events: List[str]):
        self.__subscribed_events = subscribed_events

    @abstractmethod
    def handle(self, event: Event):
        raise NotImplementedError

    def is_subscribed_to_event(self, event_name: str) -> bool:
        return event_name in self.__subscribed_events
