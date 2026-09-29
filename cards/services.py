from .models import Flashcard
from django.utils import timezone
from datetime import timedelta

class ReviewService:
    @staticmethod
    def update_interval(flashcard_id,user,rating):
        flashcard=Flashcard.objects.get(deck__owner=user,id=flashcard_id)
        if rating=="easy":
            flashcard.interval+=5
        elif rating=="good":
            flashcard.interval+=3
        elif rating=="hard":
            flashcard.interval+=1
        flashcard.due_date=timezone.localdate()+timedelta(days=flashcard.interval)
        print("flashcard updated")
        flashcard.save()
