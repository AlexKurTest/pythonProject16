class Event:
    def __init__(self, timestamp, event_type, session_id):
        self.timestamp = timestamp
        self.type = event_type
        self.session_id = session_id
events = [
            {
                "timestamp": 1554583508000,
                "type": "itemViewEvent",
                "session_id": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
            },
            {
                "timestamp": 1555296337000,
                "type": "itemViewEvent",
                "session_id": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
            },
            {
                "timestamp": 1549461608000,
                "type": "itemBuyEvent",
                "session_id": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
            },
        ]
for event in events:
    event_obj = Event()
    event_obj.init_from_dict(event)
    print(event_obj.timestamp)