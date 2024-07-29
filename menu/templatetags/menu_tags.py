from django import template

register = template.Library()


@register.inclusion_tag('menu.html', takes_context=True)
def draw_menu(context, menu_name):
    menu_items = context.get('menu_items', [])
    current_path = context.get('current_path', '')
    return {'menu_items': menu_items, 'current_path': current_path, 'menu_name': menu_name}
