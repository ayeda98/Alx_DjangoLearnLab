from django.shortcuts import render
from django.http import *
from django.contrib.auth import authenticate, login , logout
from django.views.generic import TemplateView
from django.conf import settings




def home(request):
    return HttpResponse("Bonjour monde!")


class LoginView(TemplateView):
    template_name = 'front/index.html'

    def post(self, request, **Kwargs):

        username = request.POST.get('username', False)
        Password = request.POST.get('password', False)
        user = authentificat(username = username , password = password)
        if user is not None and user.is_active: 
            login(request, user)
            return HttpResponseRedirect(serrings.LOGIN_REDIRECT_URL)
        return render(request, self.template_name)
    
class LogoutView(TemplateView):
    template_name = 'front/index.html'
    def get(self, request, **kwargs):
        logout(request)
        return render(request, self.template_name)