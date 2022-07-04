from rest_framework.views import exception_handler

def status_code_handler(exc, context):
    respons = exception_handler(exc, context)

    if respons is not None and respons.status_code == 403:
        respons.status_code = 401

    return respons