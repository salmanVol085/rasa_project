# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import random
#
#
class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        replies = ["Hello World!", "Hi there!", "Greetings!", "Hey!", "Salutations!", "Howdy!", "What's up?", "Yo!", "Hiya!", "Good to see you!", "Hey there!", "Hello!", "Hi!"]

        dispatcher.utter_message(text=random.choice(replies))

        return []
    
    
class ActionGoodBye(Action):

    def name(self) -> Text:
        return "action_goodbye"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        replies = ["Goodbye!", "See you later!", "Take care!", "Farewell!", "Bye!", "Catch you later!", "See ya!", "Later!", "Night!", "Peace out!", "I'm off!"]

        dispatcher.utter_message(text=random.choice(replies))

        return []
