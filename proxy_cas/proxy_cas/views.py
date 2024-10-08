from django.shortcuts import render
from django_cas_ng.models import ProxyGrantingTicket
from django_cas_ng.utils import get_cas_client
from django.http import JsonResponse
from django.http import HttpRequest, HttpResponse

def home(request: HttpRequest) -> HttpResponse:
    body = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>home</title>
</head>
<body>
<p>Ceci est un test pour un proxy CAS</p>
</body>
</html>
        """
    return HttpResponse(body)

# @csrf_exempt
def get_pt(request):
    """Get Proxy Ticket for a service from Proxy Granting Ticket IOU
    GET /cas/pt

    Parameters
    ----------
    pgtiou : string, required
        Proxy Granting Ticket IOU
    service : string, required
        Target service which the Proxy Ticket for

    Returns
    -------
    pt
        Proxy Ticket
    """
    if request.GET.get('pgtiou') is not None and request.GET.get('service') is not None:
        pgt = ProxyGrantingTicket.objects.get(pgtiou=request.GET.get('pgtiou'))
        if pgt is not None:
            client = get_cas_client(service_url=request.GET.get('service'))
            pt = client.get_proxy_ticket(pgt.pgt)
            if pt is not None:
                #return JsonResponse({'pt': pt})
                print("OK PT")

                body = """<!DOCTYPE html>
                        <html lang="en">
                        <head>
                            <meta charset="UTF-8">
                            <title>Title</title>
                        </head>
                        <body>
                        ça à l'air de marcher
                        </body>
                        </html>
                        """
                return HttpResponse(body)
                #return render(request, "proxy_cas/testok.html")
            else:
                response = JsonResponse({'status':'false','message': 'Invalid pgtiou'})
                response.status_code = 400
                return response
        else:
            response = JsonResponse({'status':'false','message': 'Invalid pgtiou'})
            response.status_code = 400
            return response
    else:
        response = JsonResponse({'status':'false','message': 'Missing required data'})
        response.status_code = 400
        return response