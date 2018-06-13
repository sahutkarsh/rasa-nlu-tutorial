from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet

class ActionWeather(Action):
    def name(self):
        return 'action_weather'
    
    def run(self, dispatcher, tracker, domain):
        from apixu.client import ApixuClient
        api_key = '5ed103a862bd442182385105181306'
        client = ApixuClient(api_key)
        loc = tracker.get_slot('location')
        current = client.getCurrentWeather(q=loc)
        city = current['location']['name']
        condition = current['current']['condition']['text']
        response = """It is currently {} in {} at the moment.""".format(condition,city)
        dispatcher.utter_message(response)
        return [SlotSet('location',loc)]