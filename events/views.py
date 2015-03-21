from .models import Event
from .serializers import EventSerializer
from rest_framework import generics
import datetime


class EventList(generics.ListCreateAPIView):

    """
    List last 10 events, or create a new one
    """
    queryset = Event.objects.all().order_by('-time')[:10]
    serializer_class = EventSerializer


class EventDetail(generics.RetrieveUpdateDestroyAPIView):

    """
    Retrieve, update or delete a snippet instance.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class EventCategoryList(generics.ListCreateAPIView):

    """
    List of all events by the same category
    """
    serializer_class = EventSerializer

    def get_queryset(self):
        category = self.kwargs['category']
        return Event.objects.filter(category=category)


class EventPersonList(generics.ListCreateAPIView):

    """
    List of all events by the same person
    """
    serializer_class = EventSerializer

    def get_queryset(self):
        person = self.kwargs['person']
        return Event.objects.filter(person=person)


class EventTimeList(generics.ListCreateAPIView):

    """
    List of all events after provided time
    """
    serializer_class = EventSerializer

    def get_queryset(self):
        year = self.kwargs['year']
        month = self.kwargs['month']
        day = self.kwargs['day']
        return Event.objects.filter(time__gte=datetime.date(int(year),
                                                            int(month),
                                                            int(day)))
