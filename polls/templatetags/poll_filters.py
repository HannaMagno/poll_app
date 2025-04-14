from django import template
from django.template.defaultfilters import floatformat

register = template.Library()

@register.simple_tag
def vote_percentage(votes, total):
    try:
        if total > 0:
            return floatformat((votes / total) * 100, 1)
        return 0
    except (ValueError, ZeroDivisionError):
        return 0
