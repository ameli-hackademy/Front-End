from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from dashboard.authhelper import get_signin_url, get_token_from_code, get_access_token
from dashboard.outlookservice import get_me, get_my_messages, get_my_events, get_my_contacts,get_my_rule
import time

# Create your views here.
def gettoken(request):
  auth_code = request.GET['code']
  redirect_uri = request.build_absolute_uri(reverse('dashboard:gettoken'))
  print(redirect_uri)
  token = get_token_from_code(auth_code, redirect_uri)
  access_token = token['access_token']
  user = get_me(access_token)
  refresh_token = token['refresh_token']
  expires_in = token['expires_in']

  # expires_in is in seconds
  # Get current timestamp (seconds since Unix Epoch) and
  # add expires_in to get expiration time
  # Subtract 5 minutes to allow for clock differences
  expiration = int(time.time()) + expires_in - 300

  # Save the token in the session
  request.session['access_token'] = access_token
  request.session['refresh_token'] = refresh_token
  request.session['token_expires'] = expiration

  return HttpResponseRedirect(reverse('dashboard:homepage'))


def index(request):
  redirect_uri = request.build_absolute_uri(reverse('dashboard:gettoken'))
  sign_in_url = get_signin_url(redirect_uri)
  context = { 'signin_url': sign_in_url }
  return render(request, 'dashboard/index.html', context)


def network(request):
    return render(request,'dashboard/network.html')

def suggestion(request):
    return render(request,'dashboard/suggestion.html')

def insight(request):
    return render(request,'dashboard/insight.html')

def attachment(request):
    return render(request,'dashboard/attachment.html')

def homepage(request):
  access_token = get_access_token(request, request.build_absolute_uri(reverse('dashboard:gettoken')))
  # If there is no token in the session, redirect to home
  if not access_token:
    return HttpResponseRedirect(reverse('index'))
  else:
    messages = get_my_messages(access_token)
    context = { 'messages': messages['value'],'total':len(messages['value']) }
    return render(request, 'dashboard/home.html', context)
