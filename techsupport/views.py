from django.shortcuts import render
import requests
import json
from support.settings import ORG_ID, OAUTH_ACCESS_TOKEN
# Create your views here.

def index(request):
    return render(request, 'home.html')


def listTkt(request):

    url = "https://desk.zoho.in/api/v1/tickets"

    payload={}
    headers = {
        'orgId': ORG_ID,
    'Authorization': OAUTH_ACCESS_TOKEN,
    'Cookie': '2eed0b67fd=e8c6136db547ffe0d5d28c6af934e94a; _zcsr_tmp=f5be49c4-d4a9-47c1-ad77-cd274b65952c; crmcsr=f5be49c4-d4a9-47c1-ad77-cd274b65952c'
        }

    response = requests.request("GET", url, headers=headers, data=payload)
    data=response.json()
    statuscode=response.status_code

    info=data.get('data')

    return render(request, 'listTicket.html', {'data': data, 'info': info, 'statuscode':statuscode})



def createTkt(request):
    context={}
    url = "https://desk.zoho.in/api/v1/tickets"
    headers = {
                'orgId': ORG_ID,
                'Authorization': OAUTH_ACCESS_TOKEN,
                'Content-Type': 'application/json',
                'Cookie': '2eed0b67fd=f369298bdcaa504163502a5596fe31d7; JSESSIONID=1A1CE5851E15AD44B6F8CF43CA937374; _zcsr_tmp=a302e082-d69d-4951-87b1-c619e3404cbc; crmcsr=a302e082-d69d-4951-87b1-c619e3404cbc'
                }

    if request.method=="POST":

        sub=request.POST['subject']
        desc=request.POST['desc']
        dept=request.POST['dept']
        deptcode=""

        if dept=='Sales':
            deptcode="74850000000134097"
        elif dept=='Marketing':
            deptcode="74850000000140370"

        catgry=request.POST['catgry']
        usrname=request.POST['uname']
        usremail=request.POST['usremail']
        priority=request.POST['priority']



        payload = json.dumps({
                    "subject": sub,
                    "departmentId": deptcode,
                    "description":desc,
                     "priority": priority,
                     "category": catgry,
                        "contact": {
                                    "firstName": usrname,
                                     "email": usremail
                                    }
                            })
        response = requests.request("POST", url, headers=headers, data=payload)
        resdata=response.json()
        rescode= response.status_code

        if rescode==200:
            msg="Your ticket is created successfully"
            context={'msg':msg,
                    'res':resdata}

    return render(request, 'createtkt.html', context)