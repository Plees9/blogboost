class BlogModel:
    def __init__(self, id, blogName, topic, subTopic):
        self.id = id
        self.blogName = blogName
        self.topic = topic
        self.subTopic = subTopic

    @classmethod
    def fromJson(cls, json):
        return cls(
            id= json["id"],
            blogName= json["blogName"],
            topic= json["topic"],
            subTopic= json["subTopic"]
        )
