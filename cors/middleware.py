# a 'one fits all' example good for testing (careful in production!)
# refer to http://www.w3.org/TR/cors for the SPEC
# and nice explanation at: https://developer.mozila.org/En/HTTP_Access_Control for more details
from django.http import HttpResponse


class AllowOriginMiddleware(object):
    def process_request(self, request):
        if request.method == 'OPTIONS':
            response = HttpResponse()
            response['Access-Control-Allow-Credentials'] = 'true'
            response['Access-Control-Allow-Methods']     = 'POST, GET, OPTIONS'
            response['Access-Control-Allow-Headers']     = 'Authorization,DNT,X-Mx-ReqToken,Keep-Alive,User-Agent,X-Requested-With,If-Modified-Since,Cache-Control,Content-Type'
            response['Access-Control-Max-Age']           = 1728000  # 20 days is enough, not?
            return response

    def process_response(self, request, response):
        origin = request.META.get('HTTP_ORIGIN')
        if origin:
            response['Access-Control-Allow-Origin'] = origin
            response['Access-Control-Allow-Methods'] = 'POST, GET, OPTIONS'
            response['Access-Control-Allow-Credentials'] = 'true'
            response['Access-Control-Allow-Headers'] = 'Authorization,DNT,X-Mx-ReqToken,Keep-Alive,User-Agent,X-Requested-With,If-Modified-Since,Cache-Control,Content-Type'
        return response
