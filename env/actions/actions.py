# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import random
#
#


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_greet"

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
    

    
class ActionAskHours(Action):

    def name(self) -> Text:
        return "action_ask_hours"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        replies = ["We are open Monday to Friday, from 9 AM to 6 PM.", "Our working hours are 9 AM to 6 PM, Monday to Friday.", "You can visit us between 9 AM and 6 PM on weekdays.", "We operate from 9 in the morning till 6 in the evening, Monday through Friday."]

        dispatcher.utter_message(text=random.choice(replies))

        return []

class ActionAskLocation(Action):

    def name(self) -> Text:
        return "action_ask_location"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        replies = ["Our office is in Pune, near Pimpri Chowk.", 
                   "You can find us in Pune, close to Pimpri Chowk.",
                   "We are located in Pune, near the Pimpri Chowk area.",
                   "Our location is in Pune, just by Pimpri Chowk."]

        dispatcher.utter_message(text=random.choice(replies))

        return []

class ActionAskContact(Action):

    def name(self) -> Text:
        return "action_ask_contact"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        replies = ["You can contact us at 9876543210 "]
        dispatcher.utter_message(text=random.choice(replies))
        return []

class ActionAskMatchCricket(Action):

    def name(self) -> Text:
        return "action_match_cricket"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        replies = [
            "The next cricket match is on Saturday at 3 PM between Team A and Team B at the National Stadium.",
            "Team A will face Team B in the next cricket match on Saturday at 3 PM at the National Stadium.",
            "The upcoming cricket match is scheduled for Saturday at 3 PM, featuring Team A vs Team B at the National Stadium.",
            "You can watch the next cricket match between Team A and Team B on Saturday at 3 PM at the National Stadium."
            
        ]

        dispatcher.utter_message(text=random.choice(replies))

        return []
    


            
            