from django.shortcuts import render

# Create your views here.
users_list = []


def hello(request):
    return render(request, 'hello.html')


# def users(request):
#     return render(request, 'users.html')

def users(request, name):
    # print(name)
    users_list.append(name)
    check = False if len(users_list) > 3 else True
    return render(request, 'users.html', {'xxx': name, 'users': users_list, 'check':check})
