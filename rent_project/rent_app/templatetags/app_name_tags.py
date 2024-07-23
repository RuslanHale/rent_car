from django import template


register = template.Library()


@register.filter(name='get_attribute')
def get_attribute(obj, attr):
    return f"{attr} {getattr(obj, attr, '')}"
