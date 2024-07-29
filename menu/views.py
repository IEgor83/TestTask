from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Prefetch
from .models import Menu, MenuItem


def dynamic_view(request, menu_name=None, path=None):
    try:
        menu = Menu.objects.prefetch_related(
            Prefetch('items', queryset=MenuItem.objects.prefetch_related('children'))
        ).get(name=menu_name)
        menu_items = menu.items.filter(parent__isnull=True)
        current_path = '/' + (path or '')

        def get_active_menu_items(menu_items, current_path):
            for item in menu_items:
                item.is_active = item.get_url() == current_path
                item.is_expanded = any(child.get_url() == current_path for child in item.children.all())
                get_active_menu_items(item.children.all(), current_path)

        get_active_menu_items(menu_items, current_path)

        context = {
            'menu_items': menu_items,
            'current_path': current_path,
            'menu_name': menu_name,
        }
    except Menu.DoesNotExist:
        context = {
            'menu_items': [],
            'current_path': request.path,
            'menu_name': menu_name,
        }
    return render(request, 'test_template.html', context)
