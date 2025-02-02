from django.http import JsonResponse
from .models import FAQ

def faq_list(request):
    # Get the language from the query parameter, default to 'en' (English)
    lang = request.GET.get('lang', 'en')

    # Retrieve all FAQs from the database
    faqs = FAQ.objects.all()
    data = []  # This will store the FAQ data in the appropriate format

    # Loop through each FAQ and add the translated text based on the selected language
    for faq in faqs:
        # Check the requested language and return the appropriate translation or default to English
        if lang == 'hi':  # If language is Hindi
            data.append({
                'question': faq.question_hi or faq.question,  # If Hindi translation exists, use it, otherwise fallback to the original question
                'answer': faq.answer_hi or faq.answer  # Same for the answer
            })
        elif lang == 'bn':  # If language is Bengali
            data.append({
                'question': faq.question_bn or faq.question,
                'answer': faq.answer_bn or faq.answer
            })
        else:  # Default to English
            data.append({
                'question': faq.question,
                'answer': faq.answer
            })

    # Return the FAQ data as a JSON response
    return JsonResponse({'faqs': data})
