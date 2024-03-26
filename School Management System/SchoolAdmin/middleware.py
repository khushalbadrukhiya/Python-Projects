from django.shortcuts import redirect
from django.urls import reverse

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if the user is authenticated
        if request.session.get('is_login',False)==False:
            login_exempt_views = ['login', 'forgotPassword','getTeacher','insTeacher']  # Add your views here

            # Check if the requested view is exempt from login
            if not any(view in request.path for view in login_exempt_views):

                redirect_url = reverse('login')
                return redirect(redirect_url)

        response = self.get_response(request)
        return response