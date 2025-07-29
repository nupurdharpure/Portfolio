# portfolio/templatetags/__init__.py
# This empty file is needed to make the directory a Python package

# portfolio/templatetags/portfolio_extras.py
from django import template

register = template.Library()

@register.filter
def multiply(value, arg):
    """Multiplies the value by the argument"""
    return value * arg