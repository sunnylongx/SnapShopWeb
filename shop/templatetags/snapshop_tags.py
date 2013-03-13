from django import template
register = template.Library()

def format_price(value_in_cents):
    return "$%.2f" % (int(value_in_cents)/100.0)

register.filter('format_price', format_price)