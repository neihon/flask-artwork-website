class Artwork:
    def __init__(self, art_id, title, date, image, additional):
        self.art_id = art_id
        self.title = title
        self.date = date
        self.image = image
        self.additional = additional

    def __str__(self):
        return (
            f"Id: {self.art_id}, "
            f"Title: {self.title}, "
            f"Date: {self.date}, "
            f"Image URL: {self.image}"
            f"Additional: {self.additional}"
        )