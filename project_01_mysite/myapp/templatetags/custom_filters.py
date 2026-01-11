from django import template

register = template.Library()

@register.filter
def currency(value):
    return f"${value}"

@register.filter
def discount(value, percent):
    try:
        discount_amount = (percent / 100) * float(value)
        return float(value) - discount_amount
    except (ValueError, TypeError):
        return value