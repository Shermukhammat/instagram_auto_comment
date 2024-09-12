def get_id(changes: dict) -> str:
    """
    Extract the user ID from the changes dictionary.

    Args:
        changes (dict): The dictionary containing changes.

    Returns:
        str: The user ID if present, otherwise None.
    """
    if changes.get('from') and isinstance(changes['from'], dict):
        if changes['from'].get('id'):
            return changes['from']['id']

def get_username(changes: dict) -> str:
    """
    Extract the username from the changes dictionary.

    Args:
        changes (dict): The dictionary containing changes.

    Returns:
        str: The username if present, otherwise None.
    """
    if changes.get('from') and isinstance(changes['from'], dict):
        return changes['from'].get('username')

class User:
    """
    A class to represent a user associated with a change.

    Attributes:
        username (str): The username of the user.
        id (str): The ID of the user.
    """

    def __init__(self, changes: dict) -> None:
        """
        Initialize the User instance.

        Args:
            changes (dict): The dictionary containing changes.
        """
        self.username = get_username(changes)
        self.id = get_id(changes)
