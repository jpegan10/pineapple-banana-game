from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from wagerapp.forms import UserForm, BettorForm
# Create your views here.
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from wagerapp.models import Bettor, Wager

def index(request):
    
    # index to site will just include a link to contest
    
    return render(request,
                  'wagerapp/index.html',
                  {})

def contest(request):
    pass
    # this will list the contestants
    
def register(request):
    registered = False
    
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        bettor_form=BettorForm(data=request.POST)
        
        #if the forms are vaild
        if user_form.is_valid() and bettor_form.is_valid():
            #Save the user's FORM to the database
            user=user_form.save()
            # I think the user is officially created here?
            # now hash the password
            user.set_password(user.password)
            user.save()
            
            bettor = bettor_form.save(commit=False)
            bettor.user=user
            
            bettor.save()
            registered=True
            #Update the registered variabble to tell the template registration was successful
            
        else:
            print user_form.errors, bettor_form.errors
    
    #not an HTTP POST , its a GET,  so we render our form using two modelform instances
    else:
        user_form=UserForm()
        bettor_form=BettorForm()
    
    return render(request,
                  'wagerapp/register.html',
                  {'user_form':user_form, 'bettor_form':bettor_form, 'registered' : registered})
    
def user_login(request):
    
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        
        #use django's password machinery to check password
        #if it is authenticated, a user object is returned
        
        user=authenticate(username=username, password=password)
        
        #if user is a user object, the authentication was successful
        
        if user:
            # is the account active
            if user.is_active:
                # if account is valid and active, we can log in the user
                #we'll send the user back to the home page.
                
                login(request,user)
                return HttpResponseRedirect('/wagerapp/')
            else:
                return HttpResponse('Your account was disabled')
        else:
            #bad login
            print "Invalid login details: {0}, {1}".format(username,password)
            return HttpResponse("Invalid login details supplied")
    else:
        #no context to send to the template, so
        #a blank dictionary
        return render(request,
                      'wagerapp/login.html',
                      {}
                     )

@login_required
def restricted(request):
    return HttpResponse("Since you are logged in you can see this")

@login_required
def user_logout(request):
    logout(request)
    # Since the decorator tells us that the user is logged in we can just log them out.
    return HttpResponseRedirect('/wagerapp/')


def userprofile(request, profile_name ):
    
    user=User.objects.get(username=profile_name)
    bettor=Bettor.objects.get(user=user)
    
    #wagerlist = bettor
    
    past_wagers = Wager.objects.filter(bettor=bettor)
    
    context_dict = {'past_wagers':past_wagers, 'bettor': bettor}
    return render(request,'wagerapp/userprofile.html', context_dict)
    

def standings(request):
    
    bettor_list = Bettor.objects.order_by('-balance')
    context_dict = {'bettor_list' : bettor_list}
    return render(request, 'wagerapp/standings.html', context_dict)


    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    