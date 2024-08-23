from django.urls import path
from shopping_list import views as shopping_list_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    #path('', tutorials_views.index, name='home'),
    path('', from shopping_list import views as shopping_list_views
.index.as_view(), name='home'),
    path('api/foods/', from shopping_list import views as shopping_list_views
.inventory_list),
    path('api/tutorials/<int:pk>/', from shopping_list import views as shopping_list_views
.tutorial_detail),
    path('api/tutorials/published/', from shopping_list import views as shopping_list_views
.tutorial_list_published)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)