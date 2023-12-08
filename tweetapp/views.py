from django.shortcuts import render, redirect
from . import models
from django.urls import reverse, reverse_lazy
from tweetapp.forms import AddTweetForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
# Create your views here.

def listtweet(request):
    all_tweets = models.tweet.objects.all()
    tweet_dict = {"tweets":all_tweets}
    return render(request,"tweetapp/listtweet.html",context=tweet_dict)


@login_required(login_url="/login")
def addtweet(request):
    if request.POST:
        message = request.POST["message"]
        models.tweet.objects.create(username=request.user ,message=message)
        return redirect(reverse('tweetapp:listtweet'))
    else:   
        return render(request,"tweetapp/addtweet.html")
    
def addTweetbyForm(request):
    if request.method == "POST":
        form = AddTweetForm(request.POST)
        if form.is_valid():
            nickname = form.cleaned_data["nickname_input"]
            message =form.cleaned_data["message_input"]
            models.tweet.objects.create(nickname=nickname,message=message)
            return redirect(reverse('tweetapp:listtweet'))
        else:
            print("error form!")
    else:
        form = AddTweetForm()
        return render(request,'tweetapp/addtweetbyform.html',context={"form":form})

@login_required
def deletetweet(request,id):
    tweet = models.tweet.objects.get(pk=id)
    if request.user == tweet.username:
            models.tweet.objects.filter(id=id).delete()
            return redirect('tweetapp:listtweet')
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"