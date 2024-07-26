from django import template

from models import Menu

register = template.Library()


@register.inclusion_tag('menu.html', takes_context=True)
def show_menu(context, menu_title):
    request = context.get('request')
    menu = Menu.objects.prefetch_related('items').get(title=menu_title)
    menu_items = menu.items.all()
    return {
        'request': request,
        'menu_items': menu_items
    }
