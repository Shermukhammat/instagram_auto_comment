def get_id(changes: dict) -> str:
    """
    Extract the media ID from the changes dictionary.

    Args:
        changes (dict): The dictionary containing changes.

    Returns:
        str: The media ID if present, otherwise None.
    """
    if changes.get('media') and isinstance(changes['media'], dict):
        return changes['media'].get('id')

def get_type(changes: dict) -> str:
    """
    Extract the media type from the changes dictionary.

    Args:
        changes (dict): The dictionary containing changes.

    Returns:
        str: The media type if present, otherwise None.
    """
    if changes.get('media') and isinstance(changes['media'], dict):
        return changes['media'].get('media_product_type')

class Media:
    """
    A class to represent media associated with a change.

    Attributes:
        id (str): The ID of the media.
        type (str): The type of media (e.g., REELS).
    """

    def __init__(self, changes: dict) -> None:
        """
        Initialize the Media instance.

        Args:
            changes (dict): The dictionary containing changes.
        """
        self.id = get_id(changes)
        self.type = get_type(changes)
