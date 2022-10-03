from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie


from transformers import pipeline

# As a global model, loaded once and used forever in the life of the server
classifier = pipeline('sentiment-analysis', model="distilbert-base-uncased-finetuned-sst-2-english")

def format_response(res):
    response = "<html>"
    for r in res:
        response += f"<br>Label is {r['label']} with score = {r['score']:.4f}"
    response += "<br></html>"

    return response

@ensure_csrf_cookie
def infer(request):
    print(f"Incoming request: {request}")
    if request.method == "GET":
        data = request.GET
        text2analysis = data.get('text')
        res = classifier(text2analysis)
        return HttpResponse(format_response(res), content_type='text/html', charset='utf-8')
    elif request.method == "POST":
        data = request.POST
        text2analysis = data.get('text')
        res = classifier(text2analysis)
        return HttpResponse(format_response(res), content_type='text/html', charset='utf-8')
    else:
        print("Unknown method")
        return HttpResponse("Unknown method")