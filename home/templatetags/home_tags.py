from django import template
from home.models import VisitorExpressSnippet, AboutSnippet, Click2ParkSnippet, Journey2ShareSnippet, CaseStudySnippet

register = template.Library()


# VisitorExpress snippets
@register.inclusion_tag('home/tags/aboutsnippet.html', takes_context=True)
def AboutSnippets(context):
    return {
        'aboutsnippets': AboutSnippet.objects.filter(active=True),
        'request': context['request'],
    }

@register.inclusion_tag('home/tags/visitorexpresssnippet.html', takes_context=True)
def VisitorExpressSnippets(context):
    return {
        'visitorexpresssnippets': VisitorExpressSnippet.objects.filter(active=True),
        'request': context['request'],
    }

@register.inclusion_tag('home/tags/click2parksnippet.html', takes_context=True)
def Click2ParkSnippets(context):
    return {
        'click2parksnippets': Click2ParkSnippet.objects.filter(active=True),
        'request': context['request'],
    }

@register.inclusion_tag('home/tags/journey2sharesnippet.html', takes_context=True)
def Journey2ShareSnippets(context):
    return {
        'journey2sharesnippets': Journey2ShareSnippet.objects.filter(active=True),
        'request': context['request'],
    }

@register.inclusion_tag('home/tags/casestudysnippet.html', takes_context=True)
def CaseStudySnippets(context):
    return {
        'casestudysnippets': CaseStudySnippet.objects.filter(active=True),
        'request': context['request'],
    }
