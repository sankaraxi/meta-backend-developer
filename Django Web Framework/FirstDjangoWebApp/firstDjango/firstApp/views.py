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

def parameters(request, name): 
    # Get the parameters from the request
    
    items = {
        'sankar': "CEO of the SanKrix Corporation",
        'rakky': "CEO of the Rakky Corporation",
        'prassu': "CEO of the Prassu Corporation",
        'sid': "CEO of the Sid Corporation",
    }

    description = items[name]

    return HttpResponse(f"<h1>{name}</h1>" + description)