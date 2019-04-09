from django.shortcuts import render
from django.http import HttpResponse
from lib.sms import send_sms


def submit_phone(request):
    """获取短信验证码"""
    if not request.method =="POST":
        return HttpResponse('request method error')

    phone = request.POST.get('submit phone')

    return "hello"


def submit_vcode(request):
    """通过验证码登录注册"""
    pass


def get_profile(request):
    """获取个人资料"""
    pass


def set_profile(request):
    """修改个人资料"""
    pass


def upload_avatar(request):
    """头像上传"""
    pass



