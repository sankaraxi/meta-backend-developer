from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse 

def index(request): 

    path = request.path
    scheme = request.scheme
    method = request.method
    address = request.META['REMOTE_ADDR']
    user_agent = request.META['HTTP_USER_AGENT']
    path_info = request.path_info

    response = HttpResponse()
    response.headers['Age'] = 120

    message = f"""<br>
       <br>Path: {path}
         <br>Scheme: {scheme}
            <br>Method: {method}
                <br>Address: {address}
                    <br>User Agent: {user_agent}
                        <br>Path Info: {path_info}
                            <br>Response: {response.headers}
    """

    return HttpResponse(message , content_type='text/html', charset='utf-8') 