from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .forms import ProfileForm  # Custom form for updating the user profile

# Registration View
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log the user in after registration
            return redirect('profile')  # Redirect to profile page after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'blog/register.html', {'form': form})

# Profile View and Edit Profile
@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to the profile page after update
    else:
        form = ProfileForm(instance=request.user)
    return render(request, 'blog/profile.html', {'form': form})



class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email']  # You can extend this to include additional fields like profile picture or bio
