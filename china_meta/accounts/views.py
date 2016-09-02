from django.shortcuts import render, redirect

from accounts.forms import SignupForm#, MypageForm
from accounts.models import Profile

from django.contrib.auth.models import User
from django.contrib.auth import login as login_user
from django.contrib.auth import logout as logout_user
from django.contrib.auth.views import login as default_login_view
from django.contrib.auth.decorators import login_required

def signup(request):
	if request.method=="POST":
		userform = SignupForm(request.POST)
		if userform.is_valid():
			user = userform.save(commit=False)
			user.username = userform.cleaned_data['username']
			user.email = userform.cleaned_data['email']
			user.save()
			profile = Profile(user=user)
			profile.save()
			return redirect("signup_ok")
	else:
		userform = SignupForm()
	return render(request, "accounts/signup.html", {
		'userform':userform,
	})

def login(request):
	return default_login_view(request, template_name="accounts/login.html")

def logout(request):
	logout_user(request)
	return redirect("index")

@login_required
def mypage(request):
	return render(request, "accounts/mypage.html", {
	})
