from django.urls import path
from .views import EntryCreateView, EntryApi

urlpatterns = [
    path('entries/', EntryCreateView.as_view(), name='entry-create'),
    path('entries/list/', EntryApi, name='entry-list'),
    path('entries/list/<int:iden>', EntryApi, name='entry-list'),
]