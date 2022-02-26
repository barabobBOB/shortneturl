from atexit import register
from django import template
from django.utils.html import mark_safe

register = template.Library()

@register.filter(name="email_ma") # -> name 안에 있는 걸로 해야함
def email_masker(value, args):
    email_split = value.split("@")
    print(email_split[0])
    print(args)
    return f"{email_split[0]}@*****.***" if args % 2 == 0 else value

@register.simple_tag(name="text_tag", takes_context=True) # true여야만 context를 볼 수 있음
def test_tags(context):
    for c in context:
        print(c)
        
    tag_html = "<span class='badge badge-primary'>테스트태그</span>"
    return mark_safe(tag_html)
