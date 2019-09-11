from functools import wraps
from django.http import HttpResponse


class AcceptRejected(Exception):
    pass


class ContentRejected(Exception):
    pass


def negotiate_accept(request_accept, server_accept):
    # TODO: Write this logic
    negotiated_type = 'application/json'
    return negotiated_type


def negotiate_content(request_content, server_content):
    # TODO: Write this logic
    negotiated_type = 'application/json'
    return negotiated_type


def negotiate_types(content_types=list(), accept_types=list()):
    def inner_function(function):
        @wraps(function)
        def wrap(request, *args, **kwargs):
            errors = list()
            try:
                content_type = negotiate_content(request.headers['Content-Type'], content_types)
            except ContentRejected:
                errors.append({'status_code': 415: 'message': 'Content Type Rejected, Here are the Supported Types: %s' % content_types})
            try:
                accept_type = negotiate_accept(request.headers['Accept'], accept_types)
            except AcceptRejected:
                errors.append({'status_code': 406, 'message': 'Accept Type Rejected, Here are the Supported Types: %s' % accept_types})
            if not errors:
                return function(request, *args, **kwargs)
            return HttpResponse(errors[0]['message'], status_code=errors[0]['status_code'], content_type='text/plain')
        return wrap
    return inner_function
