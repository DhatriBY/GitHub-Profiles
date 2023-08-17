from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
import requests
from django.shortcuts import render
from django.contrib.auth import get_user_model
User = get_user_model()
users = User.objects.all()
# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.DO_NOTHING,
    )
    first_name =models.CharField(max_length=15,default='')
    last_name =models.CharField(max_length=15,default='')

def create_profile(sender,**kwargs):
    if kwargs['created']:
        user_profile=UserProfile.objects.create(user=kwargs['instance'])
def profile(request):
    a =request.user.username
    url="https://api.github.com/users/"+a
    response1 = requests.get(
    url,
    params={'q': 'requests+language:python'},
    )
    
    json_response1 = response1.json()
    response2 = requests.get(
    json_response1['repos_url'],
    params={'q': 'requests+language:python'},
    )

    json_response2 = response2.json()
    l=json_response2
    for i in range(len(l)):
        for j in range(len(l)):
            if i<j:
                if l[i]['stargazers_count']<l[j]['stargazers_count']:
                    temp=l[i]
                    l[i]=l[j]
                    l[j]=temp
            else:
                if l[i]['stargazers_count']>l[j]['stargazers_count']:
                    temp=l[i]
                    l[i]=l[j]
                    l[j]=temp
    name=[]
    star=[]
    dict ={}
    for i in range(len(l)):
        name.append(l[i]['name'])
        star.append(l[i]['stargazers_count'])
        dict[name[i]]=star[i]

    return render(request,'registration/profile.html',{'profile_name':json_response1['login'],'last_updated':json_response1['updated_at'],'followers':json_response1['followers'],'names':name,'stars':star,'length':len(name),'dict':dict.items()},)


def explore(request):
    User = get_user_model()
    users = User.objects.all()
    dict={}
    j=0
    for i in ((users)):
        dict[i]="/accounts/profile/"+str(j)
        j+=1
    print(dict)
    return render(request,'registration/explore.html',{'links':(dict.items())})


def another(request,id):
    a =users[id].username
    url="https://api.github.com/users/"+a
    response1 = requests.get(
    url,
    params={'q': 'requests+language:python'},
    )
    
    json_response1 = response1.json()
    response2 = requests.get(
    json_response1['repos_url'],
    params={'q': 'requests+language:python'},
    )

    json_response2 = response2.json()
    l=json_response2
    for i in range(len(l)):
        for j in range(len(l)):
            if i<j:
                if l[i]['stargazers_count']<l[j]['stargazers_count']:
                    temp=l[i]
                    l[i]=l[j]
                    l[j]=temp
            else:
                if l[i]['stargazers_count']>l[j]['stargazers_count']:
                    temp=l[i]
                    l[i]=l[j]
                    l[j]=temp
    name=[]
    star=[]
    dict ={}
    for i in range(len(l)):
        name.append(l[i]['name'])
        star.append(l[i]['stargazers_count'])
        dict[name[i]]=star[i]

    return render(request,'registration/another.html',{'profile_name':json_response1['login'],'last_updated':json_response1['updated_at'],'followers':json_response1['followers'],'names':name,'stars':star,'length':len(name),'dict':dict.items()},)



 
post_save.connect(create_profile,sender=User)   