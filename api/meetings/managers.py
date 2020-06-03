from django.db import models


class MeetingManager(models.Manager):
    def get_overview_data(self):
        return self.filter(
        ).order_by(
            'date_published'
        ).values(
            'name', 'description',
            'id',
        )
