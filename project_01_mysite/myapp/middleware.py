class LogRequestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Process before
        print(f"[Middleware] Request Path: {request.path}")
        # Process after view
        response = self.get_response(request)
        print(f"[Middleware] Response Status Code: {response.status_code}")
        
        return response
    

class TimerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        import time
        start_time = time.time()
        
        response = self.get_response(request)
        
        end_time = time.time()
        duration = end_time - start_time
        print(f"[Middleware] Request processed in {duration:.4f} seconds")
        
        return response
    
class BlockIPMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.blocked_ips = {}
    def __call__(self, request):
        ip = request.META.get('REMOTE_ADDR')
        if ip in self.blocked_ips:
            from django.http import HttpResponseForbidden
            return HttpResponseForbidden("Your IP is blocked.")
        return self.get_response(request)
                            

                               