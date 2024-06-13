from django.http import JsonResponse
from django.utils.dateparse import parse_date
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from .models import Entry
from .serializers import EntrySerializer
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


class EntryCreateView(generics.CreateAPIView):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer

    def perform_create(self, serializer):
        description = serializer.validated_data.get('description')
        user_mood = serializer.validated_data.get('user_mood')
        analyzer = SentimentIntensityAnalyzer()
        sentiment = analyzer.polarity_scores(description)
        calculated_mood = sentiment['compound']
        if calculated_mood > 0:
            mood = calculated_mood*5 + 5
        else:
            mood = calculated_mood*(-5)
        serializer.save(calculated_mood=mood)


@csrf_exempt
def EntryApi (request, iden=0):
    if request.method == 'GET':
        entries = Entry.objects.all()
        entries_serializer = EntrySerializer(entries, many=True)
        return JsonResponse(entries_serializer.data, safe=False)
    elif request.method == 'DELETE':
        Entry.objects.filter(id=iden).delete()
        return JsonResponse({'status': 'ok'})