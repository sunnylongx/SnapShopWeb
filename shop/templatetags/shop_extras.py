from django import template

register = template.Library()

@register.filter
def pretty_price(value_in_cents):
    return "$%.2f" % (int(value_in_cents)/100.0)
