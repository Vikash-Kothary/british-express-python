from pprint import pprint


class Picture(object):

    def __init__(self, data):
        self.picture_url = None
        self.thumbnail_url = None
        self.no_of_likes = None
        self.pixel_array = None
        self.predicted_likes = None
        self.tags = None
        self.user_id = None
