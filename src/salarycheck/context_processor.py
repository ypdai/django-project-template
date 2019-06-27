from django.conf import settings


def system_messages(request):
    """
    返回系统级模板变量
    """
    return {
        'SYSTEM_NAME': settings.SYSTEM_NAME
    }
