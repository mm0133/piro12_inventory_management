from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from management.views import product_list, create_product, product_detail, create_client, client_detail, client_list, \
    modify_client, delete_client, delete_product, modify_product, plus, minus

urlpatterns=[
    path('', product_list, name='product-list'),
    path('<int:pk>/', product_detail, name='product-detail'),
    path('<int:pk>/plus/',plus),
    path('<int:pk>/minus/',minus),

    path('pcreate/', create_product, name='create-product'),
    path('pcreate/<int:pk>/', modify_product, name='modify-product'),


    path('ccreate/', create_client, name='create-client'),
    path('ccreate/<int:pk>/', modify_client, name='modify-client'),
    path('client/<int:pk>/delete/', delete_client),

    path('client/', client_list, name='client-list'),
    path('client/<int:pk>/', client_detail, name='client-detail'),
    path('<int:pk>/delete/',delete_product)
]

urlpatterns  += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)