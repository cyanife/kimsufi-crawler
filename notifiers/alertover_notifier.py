"""Notifier that sends messages through Alertover"""

import logging
from notifiers.base_notifier import Notifier

_logger = logging.getLogger(__name__)


class AlertoverNotifier(Notifier):
    """Notifier class to work with Alertover"""

    def __init__(self, config):
        self.source = config.get('alterover_source', '')            
        self.receiver = config.get('alterover_receiver', '')

        super(AlertoverNotifier, self).__init__(config)
    
    def check_requirements(self):
        """Check requests library is installed"""
        try:
            __import__('requests')
        except ImportError:
            raise Warning(
                "requests Python library is required for freemobile notifications. ")

        
    def notify(self, title, text, url=False):
        """"""
        import requests
        data=dict()
        data["source"] = self.source
        data["receiver"] = self.receiver
        data["content"] = text
        data["title"] = 'Kimsufi' + title
        data["url"] = url
        requests.post("https://api.alertover.com/v1/alert", data)
