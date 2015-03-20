from django import template
from django.template.defaulttags import url as url_tag, URLNode
from django.conf import settings

register = template.Library()
ACTIVE_STRING = 'active'

@register.tag
def url_active(parser, token):
    try:
        tag_name, url_var = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError(
            "{0} tag requires exactly one argument".format(
                token.split_contents()[0]))
    return URLActiveNode(url_var)
        


class URLActiveNode(template.Node):

    def __init__(self, url_var):
        self.url_var = template.Variable(url_var)

    def render(self, context):
        try:
            actual_url = self.url_var.resolve(context)
            if actual_url == context['request'].get_full_path():
                return ACTIVE_STRING
            else:
                return ''
        except template.VariableDoesNotExist as e:
            if settings.DEBUG :
                # it should always find the url variable
                # so raise exception in DEBUG mode.
                raise
            else:
                # silently fail in deployment
                return ''
