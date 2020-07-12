from rest_framework import status
from rest_framework.response import Response


def check_secret(view):
    import functools
    from doublet_app_demo.config import API_SECRET, API_SECRET_NAME

    @functools.wraps(view)
    def decorator(request, *args, **kwargs):
        if request.headers.get(API_SECRET_NAME) != API_SECRET:
            return Response('You should specify API_SECRET in headers', status=status.HTTP_401_UNAUTHORIZED)
        return view(request, *args, **kwargs)

    return decorator