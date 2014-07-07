from restclients.canvas import Canvas
from restclients.models.canvas import DiscussionTopic, DiscussionEntry

class Discussions(Canvas):
    def get_discussion_topics_for_sis_course_id(self, sis_course_id):
        url = "/api/v1/courses/sis_course_id:%s/discussion_topics" % sis_course_id
        data = self._get_resource(url)

        topics = []

        for topic_data in data:
            topic = DiscussionTopic()
            topic.topic_id = topic_data["id"]
            topic.html_url = topic_data["url"]
            canvas_course_id = topic_data["url"].split("/")[-3]
            topic.course_id = canvas_course_id
            topics.append(topic)

        return topics

    def get_entries_for_topic(self, topic):
        url = "/api/v1/courses/%s/discussion_topics/%s/entries" % (topic.course_id, topic.topic_id)
        data = self._get_resource(url)

        entries = []
        for entry_data in data:
            entry = DiscussionEntry()
            entry.user_id = entry_data["user_id"]
            entries.append(entry)

        return entries


