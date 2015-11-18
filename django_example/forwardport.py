class XForwardedPort(object):
    """https://mattrobenolt.com/handle-x-forwarded-port-header-in-django/"""
    def process_request(self, request):
        try:
            request.META['SERVER_PORT'] = request.META['HTTP_X_FORWARDED_PORT']
        except KeyError:
            pass
        return None
