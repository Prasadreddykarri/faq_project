# faq/tests.py

import pytest
from faq.models import FAQ

@pytest.mark.django_db  # This tells pytest to use the test database
def test_faq_creation():
    # Create an FAQ instance
    faq = FAQ.objects.create(
        question="What is Django?",
        answer="Django is a high-level Python web framework.",
        question_hi="Django क्या है?",
        answer_hi="Django एक उच्च-स्तरीय Python वेब फ्रेमवर्क है।",
    )
    
    # Ensure the FAQ is saved in the database
    assert FAQ.objects.count() == 1
    assert faq.question == "What is Django?"
    assert faq.answer == "Django is a high-level Python web framework."
    assert faq.question_hi == "Django क्या है?"
    assert faq.answer_hi == "Django एक उच्च-स्तरीय Python वेब फ्रेमवर्क है।"
