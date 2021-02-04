from django.contrib import admin
from django.urls import path, include

from inventory.views import *
from shipping.views import *
from users.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('user/users', UserCrudAPI.as_view()),
    path('inventory/products', ProductCrudAPI.as_view()),
    path('shipping/delivers', ProductCrudAPI.as_view()),

    path('api-auth/', include('rest_framework.urls')),
]
