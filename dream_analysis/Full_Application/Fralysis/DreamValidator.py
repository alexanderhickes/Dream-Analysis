from enum import Enum
from Fralysis.Dream import Dream

#Enum for requests.
class Request(Enum):

    """
    Enum for requesting dream features
    """

    NAME = 1
    SUBJECT = 2
    DIR_OBJ = 3
    TOPIC = 4
    RATING = 5

class DreamValidator:

    """
    Class to validate whether a dream has all required features for interpretation
    """

    def __init__(self, dream: Dream):
        self.dream_to_validate = dream

    def is_valid(self):

        """
        Checks whether there are outstanding features in dream

        :return: dream vaidity
        """
        if not self.outstanding_features():
            return True
        return False


    def outstanding_features(self):

        """
        Get a list of features missing from the dream

        :return: list of missing features
        """

        outstanding = []
        if not self.has_subject():
            outstanding.append(Request.SUBJECT)
        if not self.has_topic():
            outstanding.append(Request.TOPIC)
        if not self.has_rating():
            outstanding.append(Request.RATING)
        return outstanding


    def has_subject(self):

        """
        Check if dream has a subject

        :return: subject found
        """

        if self.dream_to_validate.get_subject() is not None:
            return True
        return False

    def has_topic(self):

        """
        Check if dream has a symbol

        :return: symbol found
        """

        if self.dream_to_validate.get_topics():
            return True
        return False

    def has_rating(self):

        """
        Check if dream has a sentiment

        :return: sentiment found
        """

        if self.dream_to_validate.get_ratings():
            return True
        return False
