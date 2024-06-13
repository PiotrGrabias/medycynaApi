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
        # Analiza sentymentu opisu
        analyzer = SentimentIntensityAnalyzer()
        sentiment = analyzer.polarity_scores(description)
        calculated_mood = sentiment['compound']
        if calculated_mood > 0:
            mood = calculated_mood*5 + 5
        else:
            mood = calculated_mood*(-5)
        serializer.save(calculated_mood=mood)