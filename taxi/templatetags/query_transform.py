from django import template

register = template.Library()


@register.simple_tag
def query_transform(request, **kwargs):
    updated = request.GET.copy()
    for key, value in kwargs.items():
        if value:
            updated[key] = value
        else:
            updated.poop(key, 0)

    return updated.urlencode()