import re
import logging
from django.http import HttpResponseForbidden

class WAFMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.patterns = [
            re.compile(r"(select).+from", re.IGNORECASE),
            re.compile(r"<script.*?>", re.IGNORECASE),
            re.compile(r"(\s|;)+(union)(\s|;)+.*select", re.IGNORECASE),
            re.compile(r"--['\"].*$", re.IGNORECASE),
            re.compile(r"on\w+\s*=", re.IGNORECASE),
            re.compile(r"javascript:", re.IGNORECASE),
            re.compile(r"\.\./(\.\.)+", re.IGNORECASE),
            re.compile(r";\s*(cat|ls|pwd|whoami|rm|echo)", re.IGNORECASE),
        ]

        self.logger = logging.getLogger('waf.security')

    def __call__(self, request):
        data = " ".join(request.GET.values()) + " " + " ".join(request.POST.values())
        
        path = request.path
        full_data = data + " " + path
        
        for pattern in self.patterns:
            match = pattern.search(full_data)
            if match:

                self.logger.warning(
                    f"Blocked request from IP={request.META.get('REMOTE_ADDR')}, "
                    f"Pattern={pattern.pattern}, "
                    f"Data={full_data[:100] + '...' if len(full_data) > 100 else full_data}"
                )
                return HttpResponseForbidden("403 Forbidden")
                
        return self.get_response(request)
