from django.shortcuts import render
from django.http import HttpResponse
from django.utils.html import escape

def test_form(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input', '')
        sanitised_input = escape(user_input)
            
        return HttpResponse(f"You entered: {sanitised_input}")
    return render(request, 'form.html')
