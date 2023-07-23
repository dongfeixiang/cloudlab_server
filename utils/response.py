from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet


class APIResponse(Response):
    '''
    Custom response in server: {"code": 100, "msg": "success", "data": {} }
    * `code` Response type code
    * `msg` Response description
    * `data` JSON data
    '''

    def __init__(self, code=None, msg=None, data=None,
                 status=None, template_name=None, headers=None,
                 exception=False, content_type=None):
        response = {"code": code, "msg": msg, "data": data}
        super().__init__(response, status, template_name, headers, exception, content_type)


class APIModelViewSet(ModelViewSet):
    '''
    Custom ModelViewSet, rewirte `finalize_response()` and `handle_exception()` method.
    '''

    def finalize_response(self, request, response, *args, **kwargs):
        '''
        Format as `code`, `msg`, `data`
        '''
        format_response = super().finalize_response(request, response, *args, **kwargs)
        format_response.data = {
            "code": "100",
            "msg": "success",
            "data": format_response.data
        }
        return format_response

    def handle_exception(self, exc):
        return super().handle_exception(exc)
