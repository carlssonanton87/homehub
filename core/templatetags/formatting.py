from django import template

register = template.Library()


@register.filter
def money(value):
    """
    Format numbers consistently for currency-like display.
    Example: 1234.5 -> 1,234.50
    """
    try:
        return f"{float(value):,.2f}"
    except (TypeError, ValueError):
        return value
