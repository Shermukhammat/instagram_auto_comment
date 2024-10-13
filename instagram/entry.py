from datetime import datetime
import pytz
# Import modules based on whether the script is run directly or imported
if __name__ == '__main__':
    from user import User
    from media import Media
else:
    from .user import User
    from .media import Media



class WebhookEntry:
    """
    A class to represent a webhook entry from Instagram's API.
    Attributes:
        entry (dict): The raw data from the webhook entry.
        changes (dict): Changes extracted from the entry data.
        entry_id (str): ID of the entry.
        change_id (str): ID of the change.
        text (str): Text of the change.
        type (str): Type of the field that changed.
    """
    def __init__(self, entry: dict) -> None:
        """
        Initialize the WebhookEntry instance.
        Args:
            entry (dict): The raw data from the webhook entry.
        """
        if not isinstance(entry, dict):
            raise Exception("Inlvalid data type gived to WbehookEntry class")
        

        self.data = entry
        self.changes = self.get_changes()
        self.entry_id: str = self.data.get('id')
        self.change_id: str = self.changes.get('id')
        self.text: str = self.changes.get('text')
        self.type: str = self.changes.get('field')
        self.time : datetime = self.get_time()
        self.from_user : User = self.get_user()
        self.media : Media = self.get_media()
        self.filed = self.changes.get('field')


    def get_changes(self) -> dict:
        """
        Extract changes from the entry data.
        Returns:
            dict: A dictionary containing the changes.
        """
        if self.data.get('changes') and isinstance(self.data['changes'], list):
            if isinstance(self.data['changes'][0], dict):
                field = self.data['changes'][0].get('field')
                answer = self.data['changes'][0].get('value', {})
                if field:
                    answer['field'] = field
                return answer
        return {}
    


    def get_time(self) -> datetime:
        """
        Get the time of the entry as a datetime object in UTC.
        Returns:
            datetime: The datetime object representing the time in UTC.
        """
        if self.data.get('time') and isinstance(self.data['time'], int):
            return datetime.fromtimestamp(self.data['time'], tz=pytz.UTC)
        

    def get_user(self) -> User:
        """
        Get the user who made the change.
        Returns:
            User: An instance of the User class representing the user who made the change.
        """
        return User(self.changes)
    

    def get_media(self) -> Media:
        """
        Get the media related to the change.
        Returns:
            Media: An instance of the Media class representing the media.
        """
        return Media(self.changes)
    
    
if __name__ == '__main__':
    pass
    # for data in sample_entry_dict['entry']:
    #     entry = WebhookEntry(data)
    #     print(entry.time)
    #     print(entry.type)
    #     print(entry.from_user.username)
    #     print(entry.from_user.id)
    #     print(entry.media.id)
    #     print(entry.media.type)
    #     print(entry.text)
    #     print(entry.change_id)
    #     print(entry.entry_id)
    #     break