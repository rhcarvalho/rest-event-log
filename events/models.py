from django.db import models


def parse_title(event):
    word_list = event.split()
    category = ''
    person = ''
    for i in word_list:
        if i.startswith('@'):
            person = i.strip('@')
        elif i.startswith('#'):
            category = i.strip('#')
    return category, person


class Event(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=100, blank=True, default='')
    person = models.CharField(max_length=100, blank=True, default='')

    class Meta:
        ordering = ('time',)

    def save(self, *args, **kwargs):
        self.category = parse_title(self.title)[0]
        self.person = parse_title(self.title)[1]
        super(Event, self).save(*args, **kwargs)

    def __str__(self):
        return "Event: {title}".format(title=self.title)
