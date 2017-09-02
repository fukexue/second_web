from django.shortcuts import render,HttpResponse
from secondapp.models import People,Article
from django.template import Template,Context

# Create your views here.
def second_try(request):
    person=People(name="scoket",job='blank')
    html_string='''
        <html>
            <head>
                <meta charset="utf-8">
                <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/semantic-ui/2.2.6/semantic.css" media="screen" title="no title">
                <title>firstapp</title>
            </head>
            <body>
                <h1 class="ui center aligned icon header">
                    <i class="hand spock icon"></i>
                    Hello, {{ person.name }}
                </h1>
            </body>
        </html>
    '''
    t=Template(html_string)
    c=Context({'person':person})
    second_web=t.render(c)
    return HttpResponse(second_web)

def index(request):
    context={}
    article_list=Article.objects.all()
    context['article_list']=article_list
    second_web_page = render(request,'first_web_2.html',context)
    return second_web_page
