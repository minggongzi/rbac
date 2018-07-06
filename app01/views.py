from django.shortcuts import render,HttpResponse
from rbac.service.permissions import *
# Create your views here.

from rbac.models import *

class Per(object):
    def __init__(self,actions):
        self.actions=actions

    def add(self):
        return 'add' in self.actions

    def delete(self):
        return 'delete'in self.actions

    def edit(self):
        return 'eidt' in self.actions

    def list(self):
        return 'list' in self.actions

def users(request):

    user_list = User.objects.all()
    id =request.session.get('user_id')
    user = User.objects.filter(id=id).first()
    Per(request.actions)

    return render(request,'users.html',locals())
import re
def add_user(request):

    return HttpResponse('add_user')

def edit_user(rquest,id):
    return HttpResponse('编辑')

def delete_user(rquest,id):
    return HttpResponse('delete删除')

def role(request):
    role_list = Role.objects.all()

    return render(request, 'roles.html', locals())

def login(request):

    if request.method=='POST':
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')

        user = User.objects.filter(name=user,pwd=pwd).first()
        if user:

             request.session['user_id'] = user.pk
             initial_session(user,request)
             return HttpResponse('成功')

    return render(request,'login.html',)