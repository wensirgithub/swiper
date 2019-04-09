from lib.sms import send_sms
from lib.http import render_json
from common import errors


def submit_phone(request):
    """获取短信验证码"""
    if not request.method == "POST":
        return render_json('request method error', errors.REQUEST_ERROR)

    phone = request.POST.get('phone')
    result, msg = send_sms(phone)

    return render_json(msg)


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



