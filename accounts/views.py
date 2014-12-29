from django.shortcuts import render
from django_tables2   import RequestConfig
from accounts.models  import *
from accounts.tables  import AvailableLineTable
from accounts.forms import WagerForm, AccountForm, UserForm
from django.forms.formsets import formset_factory
from django.contrib.auth import authenticate,login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required


def index(request):
    allaccounts=Account.objects.all()    
    return render(request,
                  'accounts/index.html',
                  {'allaccounts':allaccounts})


def availablelines(request):
    
    lines = AvailableLine.objects.filter(available=True).order_by('-game.gametime')
    games=Game.objects.filter(started=False)
    return render(request, 'accounts/availablelines.html', {'games':games , 'lines':lines})
    #return HttpResponse("What the hell is going in?")

@login_required
def makewager(request, line_slug ):
    
    
    print request.user
    try:
        line=AvailableLine.objects.get(slug=line_slug)
        print line
    except AvailableLine.DoesNotExist:
        line=None
    
    if request.method=='POST':
        wager_form=WagerForm(request.POST)
        if wager_form.is_valid():
            if line:
    
                wagermade=wager_form.save(commit=False)
                wagermade.line=line
                account=Account.objects.get(holder=request.user)
                
                wagermade.account=account
                wagermade.previous_balance=account.balance
                
                account.balance-=wagermade.amount
                wagermade.forward_balance=account.balance
                
                account.save()
                wagermade.save()
                #probably  better to dod a redirect
                #return category(request, category_name_slug )
                return HttpResponseRedirect(
                    
                    '/accounts/wagercomplete/',
                    {'wagermade':wagermade}
                )
        else:
            print form.errors
    else:
        wager_form=WagerForm()
        

    return render(request, 'accounts/makewager.html',
              {'line':line, 'wager_form':wager_form})

def register(request):
   
    registered = False
    
    #if its a request.post, we might have to make changes to the database
    if request.method =='POST':
        
        # get the raw data from the form
        # use both
        user_form=UserForm(data=request.POST)
        account_form=AccountForm(data=request.POST)
        
        # if both the forms are valid
        if user_form.is_valid() and account_form.is_valid():
            
            user=user_form.save() # the new user is saved
            
            user.set_password(user.password) #hash the password
            user.save()
            
            
            account = account_form.save(commit=False)
            account.user=user
            
            account.save()
            
            registered =True
        
        else: #invalid form
            print user_form.errors, account_form.errors
    
    # its not a post, so its a get, so just display the form
    else:
        user_form=UserForm()
        account_form=AccountForm()
    
    return render(request,
                  'accounts/register.html',
                  {'user_form':user_form, 'account_form':account_form, 'registered':registered})



@login_required
def restricted(request):
    return HttpResponse("you can see this because youare logged in")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/accounts/availablelines/')


@login_required
def wagercomplete(request):
    
    return render(request, 'accounts/wagercomplete.html')



@login_required
def myaccount(request):
    user=request.user

    account,created =Account.objects.get_or_create(holder=user)
    
    wagerspaid=WagerPaid.objects.filter(account=account)
    wagersmade=WagerMade.objects.filter(account=account)
    print(user.username)
    return render(request, 'accounts/myaccount.html',{'account':account,'wagersmade':wagersmade, 'wagerspaid': wagerspaid})
    
@login_required
def public_accounts(request,pub_username):
    user=request.user
    holder=User.objects.get(username=pub_username)
    account=Account.objects.get(holder=holder)
    
    
    
    wagerspaid=WagerPaid.objects.filter(account=account).filter(public=True)
    wagersmade=WagerMade.objects.filter(account=account).filter(public=True)

    return render(request, 'accounts/public_accounts.html',{'wagersmade':wagersmade, 'wagerspaid': wagerspaid})
    















#----------------------------------

#def user_login(request):
    
    
    
    # ifthe request is post try to pull out the login information
   # if request.method == 'POST':
        
        #we might be ready to log someone in
      #  username = request.POST['username']
     #   password = request.POST['password']
        
        
        #use django machinery to try to log someone in
    #    user=authenticate(username=username, password = password)
        
        #Ifwe have a user, object,the details are correct
        # If None, no user with matching credentials was found
        
   ##     if user:
            # ok you are a user, but are you activce?
    #        if user.is_active:
                
       #         login(request, user)
      #          return HttpResponseRedirect('/accounts/availablelines')  
     #       else:
     #           return HttpResponse("Your Pineapple account was disabled")
        
    #    else:
            #bad login
    #        return HttpResponse("invalid login")
        
    #else:
        #the request was mot a post
#        return render(request, 'accounts/login.html',{})