from abc import ABC, abstractmethod
from purevpn_event_bus.src.event import Event


class EventLogger(ABC):
    @abstractmethod
    def log_event(self, event: Event):
        raise NotImplementedError

    @abstractmethod
    def log_failed_event(self, event: Event):
        raise NotImplementedError
