from django.urls import path
from shopping_list import views as shopping_list_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    #inventory
    # path('', shopping_list_views.index.as_view(), name='home'),
    # path('api/foods/', shopping_list_views.inventory_list, name='inventory_list'),
    #shopping_list
    path('api/shopping_list/', shopping_list_views.get_list),
    path('api/shopping_list/', shopping_list_views.add_item),
    path('api/shopping_list/<int:pk>/', shopping_list_views.edit_item)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)