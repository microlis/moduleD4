from django import template
from djantimat.helpers import PymorphyProc, RegexpProc

register = template.Library()

@register.filter(name='censor')
def multiply(value):
	without_slang = PymorphyProc.replace(u'мат', repl='')
	return without_slang