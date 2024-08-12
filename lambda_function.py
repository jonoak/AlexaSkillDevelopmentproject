import logging
import json
import requests
from datetime import datetime

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.utils import is_intent_name, is_request_type
from ask_sdk_model import Response

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

sb = SkillBuilder()

class LaunchRequestHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        speech_text = "Welcome to your personal task manager! You can ask me to manage your tasks or set reminders."
        return handler_input.response_builder.speak(speech_text).set_should_end_session(False).response

class AddTaskIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return is_intent_name("AddTaskIntent")(handler_input)

    def handle(self, handler_input):
        task_name = handler_input.request_envelope.request.intent.slots["task"].value
        # Code to add task to a database or external service
        speech_text = f"Task {task_name} has been added to your list."
        return handler_input.response_builder.speak(speech_text).set_should_end_session(True).response

class SetReminderIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return is_intent_name("SetReminderIntent")(handler_input)

    def handle(self, handler_input):
        task_name = handler_input.request_envelope.request.intent.slots["task"].value
        reminder_time = handler_input.request_envelope.request.intent.slots["time"].value
        # Code to set a reminder using an external service like Google Calendar
        speech_text = f"Reminder for {task_name} has been set at {reminder_time}."
        return handler_input.response_builder.speak(speech_text).set_should_end_session(True).response

class HelpIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        speech_text = "You can ask me to add tasks or set reminders."
        return handler_input.response_builder.speak(speech_text).set_should_end_session(False).response

class CancelOrStopIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return (is_intent_name("AMAZON.CancelIntent")(handler_input) or 
                is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        speech_text = "Goodbye!"
        return handler_input.response_builder.speak(speech_text).set_should_end_session(True).response

sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(AddTaskIntentHandler())
sb.add_request_handler(SetReminderIntentHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())

lambda_handler = sb.lambda_handler()
