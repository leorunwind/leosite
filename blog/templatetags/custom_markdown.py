import markdown

from django import template
from django.template.defaultfilters import stringfilter
from django.utils.encoding import force_text
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(is_safe=True)
@stringfilter#希望字符串作为参数
def my_markdown(text):
    return mark_safe(markdown.markdown(force_text(text), 
                                       extensions=['markdown.extensions.fenced_code', 'markdown.extensions.codehilite'],
                                       safe_mode=True, 
                                       enable_attributes=False))