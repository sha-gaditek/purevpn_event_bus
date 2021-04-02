from purevpn_event_bus.src.event import Event
from purevpn_event_bus.src.event_logger import EventLogger
from purevpn_event_bus.src.event_handler import EventHandler


class EventRegistry():
    @classmethod
    def __init__(cls):
        cls.__event_handlers = []
        cls.__event_logger = None

    @classmethod
    def register_event_handler(cls, event_handler: EventHandler):
        cls.__event_handlers.append(event_handler)

    @classmethod
    def register_event_handlers(cls, event_handlers: List[EventHandler]):
        cls.__event_handlers.extend(event_handlers)

    @classmethod
    def register_event_logger(cls, event_logger: EventLogger):
        cls.__event_logger = event_logger

    @classmethod
    def publish(cls, event: Event):
        try:
            if cls.__event_logger is not None:
                cls.__event_logger.log_event(event.to_json())

            for event_handler in self.__event_handlers:
                if event_handler.is_subscribed_to_event(event.name):
                    event_handler.handle(event)
        except Exception:
            if cls.__event_logger is not None:
                cls.__event_logger.log_failed_event(event.to_json())
            raise
