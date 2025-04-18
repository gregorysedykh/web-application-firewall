from django.shortcuts import render
from django.http import HttpResponse

def test_form(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        return HttpResponse(f"You entered: {user_input}")
    return render(request, 'form.html')
