from django.shortcuts import render,redirect
from django.http import JsonResponse
from .forms import form_passwd
import itertools
import string


break_loop = None 

def main_app(request):
    form = form_passwd()

    ctx = {'form':form}

    return render(request,'index.html',context=ctx)

def evaluate(request):
    global break_loop
    passwd = request.GET.get('password', None)
    tmp = request.GET.get('break',None)
    break_loop = tmp 
    print("this is the password : "+str(passwd))
    print('begin brute force')
    founded_password,attempts = guess_password(passwd)
    print("Password is :"+str(founded_password)+". founded in "+str(attempts)+" guesses")
    result = ("Password is: "+str(founded_password)+". founded after "+str(attempts)+" guesses.")
    data = {
        'result' : result
    }
    return JsonResponse(data)

def guess_password(real):
    global break_loop
    chars = string.printable
    attempts = 0
    for guess in itertools.product(chars, repeat=len(real)):
        attempts += 1
        guess = ''.join(guess)
        if guess == real:
            return guess,attempts
            break
        if break_loop == "true":
            break
        print(guess , attempts)
