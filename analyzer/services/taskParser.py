import re
from datetime import datetime, timedelta

class TaskParser:
    @staticmethod
    def parse(text):
        title = text
        now = datetime.now()
        due_date = now

        text = text.lower()

        # Case 1: "tomorrow"
        if "tomorrow" in text:
            due_date = now + timedelta(days=1)

        # Case 2: "in X days"
        match_days = re.search(r"in (\d+) days", text)
        if match_days:
            days = int(match_days.group(1))
            due_date = now + timedelta(days=days)

        # Case 3: "at 5pm"
        match_time = re.search(r"at (\d+)(am|pm)", text)
        if match_time:
            hour = int(match_time.group(1))
            if match_time.group(2) == "pm" and hour < 12:
                hour += 12
            due_date = due_date.replace(hour=hour, minute=0, second=0, microsecond=0)

        return {
            "title": title,
            "description": "",
            "dueDate": due_date
        }
