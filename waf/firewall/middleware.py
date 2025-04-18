import re
from django.http import HttpResponseForbidden

class WAFMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.patterns = [
            re.compile(r"(select).+from", re.IGNORECASE),
            re.compile(r"<script.*?>", re.IGNORECASE),
        ]

    def __call__(self, request):
        data = " ".join(request.GET.values()) + " " + " ".join(request.POST.values())
        if any(p.search(data) for p in self.patterns):
            return HttpResponseForbidden("Forbidden: Malicious input detected.")
        return self.get_response(request)
